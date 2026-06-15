import { useState } from "react";
import { uploadReport } from "../services/api";
import { FaUpload } from "react-icons/fa";

function UploadReport({ onAnalysisComplete }) {

  const [file, setFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const handleUpload = async () => {

    if (!file) {
      setError("Please select a report first.");
      return;
    }

    try {

      setLoading(true);
      setError("");

      const result = await uploadReport(file);

      onAnalysisComplete(result);

    } catch (err) {

      setError(
        err.response?.data?.message ||
        "Upload failed"
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-semibold mb-4">
        Upload Medical Report
      </h2>

      <input
        type="file"
        accept=".pdf,.png,.jpg,.jpeg"
        className="w-full border rounded-lg p-3"
        onChange={(e) =>
          setFile(e.target.files[0])
        }
      />

      {file && (
        <p className="mt-3 text-green-600 text-sm">
          Selected: {file.name}
        </p>
      )}

      {error && (
        <div className="mt-3 text-red-500 text-sm">
          {error}
        </div>
      )}

      <button
        onClick={handleUpload}
        disabled={loading}
        className="mt-5 bg-blue-600 hover:bg-blue-700 text-white px-5 py-3 rounded-lg flex items-center gap-2 transition"
      >
        <FaUpload />

        {loading
          ? "Analyzing..."
          : "Upload & Analyze"}
      </button>

    </div>
  );
}

export default UploadReport;