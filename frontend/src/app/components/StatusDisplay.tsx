// frontend/src/app/components/StatusDisplay.tsx

import { Loader } from 'lucide-react';
import { AppState } from '../types';

interface StatusDisplayProps {
  state: AppState;
}

const StatusDisplay = ({ state }: StatusDisplayProps) => {
  const { status, isLoading, error, questions, totalQuestions } = state;

  if (error) {
    return (
      <div className="mt-6 text-center text-red-600 bg-red-50 p-4 rounded-lg border border-red-200">
        <p className="font-semibold">An Error Occurred</p>
        <p className="text-sm">{error}</p>
      </div>
    );
  }

  if (isLoading) {
    return (
      <div className="mt-6 flex flex-col items-center justify-center gap-4 text-center text-gray-700 bg-gray-50 p-6 rounded-lg border border-gray-200">
        <Loader className="w-8 h-8 animate-spin text-blue-600" />
        <p className="font-medium">{status}</p>
        {totalQuestions > 0 && (
          <p className="text-sm text-gray-500">
            Audit Results ({questions.length} / {totalQuestions})
          </p>
        )}
      </div>
    );
  }

  return null;
};

export default StatusDisplay;
