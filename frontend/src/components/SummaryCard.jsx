function SummaryCard({ summary }) {

  if (!summary) return null;

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-4">
        AI Medical Summary
      </h2>

      <div className="bg-slate-50 rounded-lg p-5">

        <p className="leading-7 text-slate-700">
          {summary}
        </p>

      </div>

    </div>
  );
}

export default SummaryCard;