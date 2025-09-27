import { useState } from 'react';
import { FileUp, SendHorizonal } from 'lucide-react';

interface FileUploadFormProps {
  handleAudit: (file: File) => void;
  isLoading: boolean;
  fileName: string | null;
  onFileSelect: (file: File | null) => void;
}

const FileUploadForm = ({ handleAudit, isLoading, fileName, onFileSelect }: FileUploadFormProps) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const onFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0] || null;
    setSelectedFile(file);
    onFileSelect(file);
  };

  const onFormSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (selectedFile) {
      handleAudit(selectedFile);
    }
  };

  return (
    <form onSubmit={onFormSubmit} className="flex gap-6 items-start bg-gray-50 p-6 rounded-lg shadow-sm border border-gray-200">
      {/* File drop area - shorter and wider */}
      <div className="flex-1">
        <label
          htmlFor="file-upload"
          className="flex flex-col items-ceter justify-center wn-full h-32 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-white hover:bg-gray-100 transition-colors"
        >
          <div className="flex flex-col items-center justify-center pt-3 pb-4">
            <FileUp className="w-8 h-8 mb-2 text-gray-400" />
            <p className="mb-1 text-sm text-gray-500">
              <span className="font-semibold">Click to upload</span> or drag and drop
            </p>
            <p className="text-xs text-gray-500">Audit Questions PDF</p>
          </div>
          <input id="file-upload" name="file-upload" type="file" className="hidden" onChange={onFileChange} accept=".pdf" />
        </label>
  
        {fileName && (
          <div className="mt-3 text-sm font-medium text-gray-600 text-center">
            Selected file: <span className="text-blue-600">{fileName}</span>
          </div>
        )}
      </div>
  
      {/* Run Audit button */}
      <div className="flex flex-col justify-center">
        <button
          type="submit"
          disabled={!fileName || isLoading}
          className="px-6 py-3 text-sm font-medium text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-gray-400 disabled:cursor-not-allowed transition-all flex items-center gap-2"
        >
          <SendHorizonal className="w-4 h-4" />
          {isLoading ? 'Auditing...' : 'Run Audit'}
        </button>
      </div>
    </form>
  );
};

export default FileUploadForm;