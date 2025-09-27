"use client";

import { useState, useRef, useEffect, useCallback } from 'react';
import { AppState } from './types';
import FileUploadForm from './components/FileUploadForm';
import StatusDisplay from './components/StatusDisplay';
import ResultsDisplay from './components/ResultsDisplay';

/**
 * Initial state for the application's state management.
 */
const initialState: AppState = {
  fileName: null,
  status: 'Ready to audit.',
  questions: [],
  isLoading: false,
  error: null,
  totalQuestions: 0,
};

/**
 * Main component for the Healthcare Policy Compliance Auditor application.
 * This component manages the application's state, handles WebSocket communication
 * with the backend, and orchestrates the rendering of child components.
 */
export default function Home() {
  const [state, setState] = useState<AppState>(initialState);
  const [file, setFile] = useState<File | null>(null);
  const socketRef = useRef<WebSocket | null>(null);

  /**
   * Effect to update the file name in the state when a new file is selected.
   */
  useEffect(() => {
    if (file) {
      setState(prevState => ({ ...prevState, fileName: file.name }));
    }
  }, [file]);

  /**
   * Main function to handle the audit process.
   * It establishes a WebSocket connection and sends the selected file to the backend.
   */
  const handleAudit = useCallback((selectedFile: File) => {
    // Reset state for a new audit, keeping the filename for the UI.
    setState({
      ...initialState,
      fileName: selectedFile.name,
      isLoading: true,
      status: 'Connecting to the audit service...',
    });

    // Ensure any existing WebSocket connection is closed before creating a new one.
    if (socketRef.current) {
      socketRef.current.close();
    }

    const wsUrl = process.env.NEXT_PUBLIC_WEBSOCKET_URL || 'ws://localhost:8000/ws/audit';
    const socket = new WebSocket(wsUrl);
    socketRef.current = socket;

    socket.onopen = () => {
      setState(prevState => ({ ...prevState, status: 'Uploading PDF and starting audit...' }));
      socket.send(selectedFile);
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      handleSocketMessage(data);
    };

    socket.onclose = () => {
      setState(prevState => ({ ...prevState, isLoading: false, status: 'Audit complete.' }));
    };

    socket.onerror = (error) => {
      console.error('WebSocket Error:', error);
      setState(prevState => ({
        ...prevState,
        error: 'A connection error occurred. Please try again.',
        isLoading: false,
      }));
    };
  }, []); // useCallback to memoize the function.

  /**
   * Handles incoming messages from the WebSocket and updates the application state.
   */
  const handleSocketMessage = (data: any) => {
    switch (data.type) {
      case 'status':
        setState(prevState => ({ ...prevState, status: data.message }));
        break;
      case 'questions_found':
        setState(prevState => ({
          ...prevState,
          totalQuestions: data.count,
          status: `${data.count} questions found. Starting analysis...`,
        }));
        break;
      case 'result':
        setState(prevState => ({
          ...prevState,
          // Sort results by question number to ensure they appear in order.
          questions: [...prevState.questions, data.data].sort((a, b) => {
            const numA = parseInt(a.question.split('.')[0]);
            const numB = parseInt(b.question.split('.')[0]);
            return numA - numB;
          }),
        }));
        break;
      case 'error':
        setState(prevState => ({ ...prevState, error: data.message, isLoading: false }));
        break;
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center p-8 sm:p-12 md:p-24 bg-gray-100 font-sans">
      <div className="z-10 w-full max-w-4xl items-center justify-between text-sm lg:flex mb-12">
        <h1 className="text-3xl font-bold text-gray-800 tracking-tight text-center lg:text-left">
          Healthcare Policy Compliance Auditor
        </h1>
        <div className="hidden lg:flex items-center justify-center bg-white rounded-full px-4 py-1 border">
          <p className="text-xs font-medium text-gray-600">Powered by Gemini 2.0 Flash</p>
        </div>
      </div>

      <div className="w-full max-w-xl">
        <FileUploadForm
          handleAudit={handleAudit}
          isLoading={state.isLoading}
          fileName={state.fileName}
          setFile={setFile}
        />
        <StatusDisplay state={state} />
      </div>

      {!state.isLoading && state.questions.length > 0 && (
        <div className="w-full max-w-4xl mt-8">
          <ResultsDisplay questions={state.questions} totalQuestions={state.totalQuestions} />
        </div>
      )}
    </main>
  );
}
