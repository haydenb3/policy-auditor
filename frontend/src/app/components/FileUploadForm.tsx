import { useState } from 'react';
import { FileUp, SendHorizonal, FileText } from 'lucide-react';

interface Props {
  handleAudit: (file: File) => void;
  isLoading: boolean;
  fileName: string | null;
  onFileSelect: (file: File | null) => void;
}

export default function FileUploadForm({ handleAudit, isLoading, fileName, onFileSelect }: Props) {
  const [f, setF] = useState<File | null>(null);

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0] || null;
    setF(file);
    onFileSelect(file);
  };

  const useExample = async () => {
    try {
      const res = await fetch('/Audit Questions.pdf');
      const blob = await res.blob();
      const file = new File([blob], 'Audit Questions.pdf', { type: 'application/pdf' });
      setF(file);
      onFileSelect(file);
    } catch (err) {
      console.error('Failed to load example PDF:', err);
    }
  };

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (f) handleAudit(f);
  };

  return (
    <form onSubmit={onSubmit} className="flex gap-6 items-start bg-gray-50 p-6 rounded-lg shadow-sm border">
      <div className="flex-1">
        <label htmlFor="upload" className="flex flex-col items-center justify-center w-full h-32 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-white hover:bg-gray-100 transition">
          <div className="flex flex-col items-center justify-center pt-3 pb-4">
            <FileUp className="w-8 h-8 mb-2 text-gray-400" />
            <p className="mb-1 text-sm text-gray-500">
              <span className="font-semibold">Click to upload</span> or drag and drop
            </p>
            <p className="text-xs text-gray-500">Audit Questions PDF</p>
          </div>
          <input id="upload" type="file" className="hidden" onChange={onChange} accept=".pdf" />
        </label>
        {fileName && (
          <div className="mt-3 text-sm font-medium text-gray-600 text-center">
            Selected: <span className="text-blue-600">{fileName}</span>
          </div>
        )}
        <div className="mt-3 text-center">
          <button
            type="button"
            onClick={useExample}
            disabled={isLoading}
            className="text-sm text-blue-600 hover:text-blue-700 hover:underline disabled:text-gray-400 flex items-center gap-1 mx-auto"
          >
            <FileText className="w-4 h-4" />
            Use example (64 question audit pdf)
          </button>
        </div>
      </div>
      <div className="flex items-center">
        <button
          type="submit"
          disabled={!fileName || isLoading}
          className="px-6 py-3 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:ring-2 focus:ring-blue-500 disabled:bg-gray-400 disabled:cursor-not-allowed transition flex items-center gap-2"
        >
          <SendHorizonal className="w-4 h-4" />
          {isLoading ? 'Auditing...' : 'Run Audit'}
        </button>
      </div>
    </form>
  );
}