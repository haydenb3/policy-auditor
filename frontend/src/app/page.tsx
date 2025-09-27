"use client";

import { useState, useRef, useEffect, useCallback } from 'react';
import { AppState, SocketMessage } from './types';
import FileUploadForm from './components/FileUploadForm';
import StatusDisplay from './components/StatusDisplay';
import ResultsDisplay from './components/ResultsDisplay';

const initialState: AppState = {
  fileName: null,
  status: 'Ready to audit.',
  questions: [],
  isLoading: false,
  error: null,
  totalQuestions: 0,
};

export default function Home() {
  const [state, setState] = useState<AppState>(initialState);
  const [file, setFile] = useState<File | null>(null);
  const socketRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    setState(prevState => ({ ...prevState, fileName: file ? file.name : null }));
  }, [file]);

  const handleAudit = useCallback((selectedFile: File) => {
    setState({
      ...initialState,
      fileName: selectedFile.name,
      isLoading: true,
      status: 'Connecting to the audit service...',
    });

    if (socketRef.current) {
      socketRef.current.close();
    }

    const wsUrl = process.env.NODE_ENV === 'development' 
      ? 'ws://localhost:8000/ws/audit' 
      : process.env.NEXT_PUBLIC_WEBSOCKET_URL || 'ws://localhost:8000/ws/audit';
    const socket = new WebSocket(wsUrl);
    socketRef.current = socket;

    socket.onopen = () => {
      setState(prevState => ({ ...prevState, status: 'Uploading PDF and starting audit...' }));
      socket.send(selectedFile);
    };

    socket.onmessage = (event: MessageEvent) => {
      try {
        const data: SocketMessage = JSON.parse(event.data);
        handleSocketMessage(data);
      } catch (error) {
        console.error("Failed to parse WebSocket message:", event.data);
        setState(prevState => ({
          ...prevState,
          error: 'Received an invalid message from the server.',
          isLoading: false,
        }));
      }
    };

    socket.onclose = () => {
      setState(prevState => ({ ...prevState, isLoading: false, status: prevState.error ? prevState.status : 'Audit complete.' }));
    };

    socket.onerror = (event: Event) => {
      console.error('WebSocket Error:', event);
      setState(prevState => ({
        ...prevState,
        error: 'A connection error occurred. Please check the backend server and your network connection.',
        isLoading: false,
      }));
    };
  }, []);

  const handleSocketMessage = (data: SocketMessage) => {
    switch (data.type) {
      case 'status':
        if (data.message) {
          setState(prevState => ({ ...prevState, status: data.message! }));
        }
        break;
      case 'questions_found':
        if (data.count !== undefined) {
          setState(prevState => ({
            ...prevState,
            totalQuestions: data.count!,
            status: `${data.count!} questions found. Starting analysis...`,
          }));
        }
        break;
      case 'result':
        if (data.data) {
          setState(prevState => ({
            ...prevState,
            questions: [...prevState.questions, data.data!].sort((a, b) => {
              const numA = parseInt(a.question.split('.')[0]);
              const numB = parseInt(b.question.split('.')[0]);
              return numA - numB;
            }),
          }));
        }
        break;
      case 'error':
        if (data.message) {
          setState(prevState => ({ ...prevState, error: data.message!, isLoading: false }));
        }
        break;
    }
  };

  return (
    <main className="min-h-screen bg-gray-100 font-sans">
      {/* Header at top */}
      <div className="w-full bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-6xl mx-auto px-8 py-6 flex items-center justify-between">
          <h1 className="text-3xl font-bold text-gray-800 tracking-tight">
            Healthcare Policy Compliance Auditor
          </h1>
          <div className="flex items-center justify-center bg-gray-100 rounded-full px-4 py-1 border">
            <p className="text-xs font-medium text-gray-600">Powered by Gemini 2.0 Flash</p>
          </div>
        </div>
      </div>
  
      {/* Main content */}
      <div className="flex flex-col items-center p-8 pt-12">
        <div className="w-full max-w-6xl">
          <FileUploadForm
            handleAudit={handleAudit}
            isLoading={state.isLoading}
            fileName={state.fileName}
            onFileSelect={setFile}
          />
          <StatusDisplay state={state} />
        </div>
  
        {state.questions.length > 0 && (
          <div className="w-full max-w-6xl mt-12">
            <ResultsDisplay questions={state.questions} totalQuestions={state.totalQuestions} />
          </div>
        )}
      </div>
    </main>
  );
}