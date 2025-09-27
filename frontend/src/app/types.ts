// frontend/src/app/types.ts

export interface AuditQuestion {
  question: string;
  documents: string[];
  compliance_status: 'Yes' | 'No' | 'Uncertain' | 'Unable to determine' | 'Error';
  confidence: number;
  explanation: string;
  relevant_sections: string[];
}

export interface AppState {
  fileName: string | null;
  status: string;
  questions: AuditQuestion[];
  isLoading: boolean;
  error: string | null;
  totalQuestions: number;
}
