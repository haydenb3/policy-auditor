// frontend/src/app/components/ResultsDisplay.tsx

import { AuditQuestion } from '../types';
import { CheckCircle, XCircle, AlertCircle, HelpCircle } from 'lucide-react';

interface ResultsDisplayProps {
  questions: AuditQuestion[];
  totalQuestions: number;
}

const getComplianceInfo = (status: string, confidence: number) => {
    const default_color = 'text-gray-500';
    if (confidence < 0.7) return { Icon: HelpCircle, color: default_color };
    
    switch (status) {
      case 'Yes':
        return { Icon: CheckCircle, color: 'text-green-600' };
      case 'No':
        return { Icon: XCircle, color: 'text-red-600' };
      case 'Uncertain':
        return { Icon: AlertCircle, color: 'text-yellow-600' };
      default:
        return { Icon: HelpCircle, color: default_color };
    }
};

const ResultsDisplay = ({ questions, totalQuestions }: ResultsDisplayProps) => {
  if (questions.length === 0) {
    return null;
  }

  return (
    <div className="mt-8">
      <h2 className="text-xl font-semibold text-gray-800 mb-4">
        Audit Results ({questions.length} / {totalQuestions})
      </h2>
      <div className="space-y-6">
        {questions.map((q, index) => {
          const { Icon, color } = getComplianceInfo(q.compliance_status, q.confidence);
          return (
            <div key={index} className="p-5 rounded-lg bg-white shadow-md border border-gray-200">
              <p className="text-sm font-medium text-gray-700 mb-3">{index + 1}. {q.question}</p>
              
              <div className="flex items-center gap-2">
                <Icon className={`w-6 h-6 ${color}`} />
                <p className={`text-lg font-bold ${color}`}>
                  {q.compliance_status}
                  <span className="text-sm font-normal text-gray-500 ml-2">
                    (Confidence: {(q.confidence * 100).toFixed(0)}%)
                  </span>
                </p>
              </div>
              
              <p className="text-sm text-gray-600 mt-2 mb-3 leading-relaxed">{q.explanation}</p>

              {q.relevant_sections.length > 0 && (
                <div className="mt-4">
                  <h4 className="text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">Relevant Sections</h4>
                  <ul className="list-disc list-inside space-y-2 text-sm text-gray-700 bg-gray-50 p-3 rounded">
                    {q.relevant_sections.map((section, i) => (
                      <li key={i} className="leading-snug">"{section}"</li>
                    ))}
                  </ul>
                </div>
              )}
              
              {q.documents.length > 0 && (
                <div className="mt-4 text-xs text-gray-400">
                  <span className="font-semibold">Sources:</span> {q.documents.join(', ')}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ResultsDisplay;