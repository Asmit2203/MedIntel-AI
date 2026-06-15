import { useState } from "react";
import API from "../services/api";

function ChatBot() {

  const [question, setQuestion] =
    useState("");

  const [answer, setAnswer] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const askQuestion = async () => {

    if (!question.trim()) return;

    try {

      setLoading(true);

      const res = await API.post(
        "/chat",
        {
          question
        }
      );

      setAnswer(res.data.answer);

    } catch {

      setAnswer(
        "Unable to process question."
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-4">
        Ask AI About Your Report
      </h2>

      <textarea
        rows={4}
        value={question}
        onChange={(e) =>
          setQuestion(e.target.value)
        }
        className="w-full border p-3 rounded-lg"
        placeholder="Why is my glucose high?"
      />

      <button
        onClick={askQuestion}
        className="mt-4 bg-blue-600 text-white px-5 py-2 rounded-lg"
      >
        {loading
          ? "Thinking..."
          : "Ask AI"}
      </button>

      {answer && (

        <div className="mt-5 bg-slate-50 p-4 rounded-lg">

          <p>{answer}</p>

        </div>

      )}

    </div>
  );
}

export default ChatBot;