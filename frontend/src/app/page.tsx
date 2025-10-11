"use client";

import { useState, useRef, useEffect, useCallback } from 'react';
import { Loader } from 'lucide-react';
import { AppState, SocketMessage } from './types';
import FileUploadForm from './components/FileUploadForm';
import ResultsDisplay from './components/ResultsDisplay';

const init: AppState = {
  fileName: null,
  status: 'Ready to audit.',
  questions: [],
  isLoading: false,
  error: null,
  totalQuestions: 0,
};

export default function Home() {
  const [state, setState] = useState<AppState>(init);
  const [file, setFile] = useState<File | null>(null);
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    setState(s => ({ ...s, fileName: file?.name || null }));
  }, [file]);

  const handleAudit = useCallback((f: File) => {
    setState({ ...init, fileName: f.name, isLoading: true, status: 'Connecting...' });
    if (ws.current) ws.current.close();

    const url = process.env.NODE_ENV === 'development' 
      ? 'ws://localhost:8000/ws/audit' 
      : process.env.NEXT_PUBLIC_WEBSOCKET_URL || 'ws://localhost:8000/ws/audit';
    
    const socket = new WebSocket(url);
    ws.current = socket;

    socket.onopen = () => {
      setState(s => ({ ...s, status: 'Uploading PDF...' }));
      socket.send(f);
    };

    socket.onmessage = (e: MessageEvent) => {
      try {
        handleMsg(JSON.parse(e.data));
      } catch {
        setState(s => ({ ...s, error: 'Invalid response', isLoading: false }));
      }
    };

    socket.onclose = () => {
      setState(s => ({ ...s, isLoading: false, status: s.error ? s.status : 'Complete' }));
    };

    socket.onerror = () => {
      setState(s => ({ ...s, error: 'Connection error', isLoading: false }));
    };
  }, []);

  const handleMsg = (data: SocketMessage) => {
    switch (data.type) {
      case 'status':
        if (data.message) setState(s => ({ ...s, status: data.message! }));
        break;
      case 'questions_found':
        if (data.count) {
          setState(s => ({
            ...s,
            totalQuestions: data.count!,
            status: `Found ${data.count} questions`,
          }));
        }
        break;
      case 'result':
        if (data.data) {
          setState(s => ({
            ...s,
            questions: [...s.questions, data.data!].sort((a, b) => 
              parseInt(a.question.split('.')[0]) - parseInt(b.question.split('.')[0])
            ),
          }));
        }
        break;
      case 'error':
        if (data.message) setState(s => ({ ...s, error: data.message!, isLoading: false }));
        break;
    }
  };

  return (
    <main className="min-h-screen bg-gray-100">
      <div className="w-full bg-white shadow-sm border-b">
        <div className="max-w-6xl mx-auto px-8 py-6 flex items-center justify-between">
          <h1 className="text-3xl font-bold text-gray-800">
            Healthcare Policy Compliance Auditor
          </h1>
          <div className="bg-gray-100 rounded-full px-4 py-1 border">
            <p className="text-xs font-medium text-gray-600">Powered by Gemini 2.5 Flash</p>
          </div>
        </div>
      </div>
      <div className="flex flex-col items-center p-8 pt-12">
        <div className="w-full max-w-6xl">
          <FileUploadForm
            handleAudit={handleAudit}
            isLoading={state.isLoading}
            fileName={state.fileName}
            onFileSelect={setFile}
          />
          {state.error && (
            <div className="mt-6 text-center text-red-600 bg-red-50 p-4 rounded-lg border border-red-200">
              <p className="font-semibold">Error</p>
              <p className="text-sm">{state.error}</p>
            </div>
          )}
          {state.isLoading && (
            <div className="mt-6 flex flex-col items-center gap-4 text-center bg-gray-50 p-6 rounded-lg border">
              <Loader className="w-8 h-8 animate-spin text-blue-600" />
              <p className="font-medium text-gray-700">{state.status}</p>
              {state.totalQuestions > 0 && (
                <p className="text-sm text-gray-500">{state.questions.length} / {state.totalQuestions} complete</p>
              )}
            </div>
          )}
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