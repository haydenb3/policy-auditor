// frontend/src/app/components/FileUploadForm.tsx

import { FileUp, SendHorizonal } from 'lucide-react';

interface FileUploadFormProps {
  handleAudit: (file: File) => void;
  isLoading: boolean;
  fileName: string | null;
  setFile: (file: File | null) => void;
}

const FileUploadForm = ({ handleAudit, isLoading, fileName, setFile }: FileUploadFormProps) => {
  const onFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setFile(file);
    }
  };

  const onFormSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const fileInput = event.currentTarget.elements.namedItem('file-upload') as HTMLInputElement;
    const file = fileInput.files?.[0];
    if (file) {
      handleAudit(file);
    }
  };

  return (
    <form onSubmit={onFormSubmit} className="flex flex-col items-center gap-4 rounded-lg bg-gray-50 p-6 shadow-sm border border-gray-200">
      <label
        htmlFor="file-upload"
        className="flex flex-col items-center justify-center w-full h-48 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-white hover:bg-gray-100 transition-colors"
      >
        <div className="flex flex-col items-center justify-center pt-5 pb-6">
          <FileUp className="w-10 h-10 mb-3 text-gray-400" />
          <p className="mb-2 text-sm text-gray-500">
            <span className="font-semibold">Click to upload</span> or drag and drop
          </p>
          <p className="text-xs text-gray-500">Audit Questions PDF</p>
        </div>
        <input id="file-upload" name="file-upload" type="file" className="hidden" onChange={onFileChange} accept=".pdf" />
      </label>

      {fileName && (
        <div className="text-sm font-medium text-gray-600">
          Selected file: <span className="text-blue-600">{fileName}</span>
        </div>
      )}

      <button
        type="submit"
        disabled={!fileName || isLoading}
        className="w-full flex items-center justify-center gap-2 px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-gray-400 disabled:cursor-not-allowed transition-all"
      >
        <SendHorizonal className="w-4 h-4" />
        {isLoading ? 'Auditing...' : 'Run Audit'}
      </button>
    </form>
  );
};

export default FileUploadForm;
