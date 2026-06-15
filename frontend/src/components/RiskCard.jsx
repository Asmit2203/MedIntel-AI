function RiskCard({ riskLevel, riskScore }) {
  const getColor = () => {
    switch (riskLevel?.toLowerCase()) {
      case "low":
        return "bg-green-500";
      case "moderate":
        return "bg-yellow-500";
      case "high":
        return "bg-red-500";
      default:
        return "bg-blue-500";
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-xl font-bold mb-4">
        Health Risk Assessment
      </h2>

      <div className="flex items-center gap-6">
        <div
          className={`w-24 h-24 rounded-full flex items-center justify-center text-white text-2xl font-bold ${getColor()}`}
        >
          {riskScore}
        </div>

        <div>
          <h3 className="text-lg font-semibold">
            {riskLevel} Risk
          </h3>

          <p className="text-slate-500 mt-1">
            AI-generated health risk prediction
          </p>
        </div>
      </div>
    </div>
  );
}

export default RiskCard;