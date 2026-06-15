import { useState } from "react";

import Navbar from "../components/Navbar";
import UploadReport from "../components/UploadReport";
import RiskCard from "../components/Riskcard";
import SummaryCard from "../components/SummaryCard";
import ReportTable from "../components/ReportTable";
import TrendChart from "../components/TrendChart";
import Recommendations from "../components/Recommendations";
import ChatBot from "../components/ChatBot";
import DownloadButton from "../components/DownloadButton";

function Dashboard() {
  const [analysis, setAnalysis] = useState(null);
  const [darkMode, setDarkMode] = useState(false);

  const demoTrendData = [
    { date: "Jan", glucose: 140 },
    { date: "Feb", glucose: 155 },
    { date: "Mar", glucose: 170 },
    { date: "Apr", glucose: 160 },
    { date: "May", glucose: 180 },
  ];

  return (
    <div
      className={`min-h-screen transition-all duration-300 ${
        darkMode
          ? "bg-slate-900 text-white"
          : "bg-slate-100 text-slate-900"
      }`}
    >
      <Navbar />

      <div className="max-w-7xl mx-auto px-4 md:px-6 py-8">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:justify-between md:items-center gap-4 mb-8">
          <div>
            <h1 className="text-3xl font-bold">
              Medical Report Analyzer
            </h1>

            <p
              className={`mt-2 ${
                darkMode
                  ? "text-slate-300"
                  : "text-slate-600"
              }`}
            >
              AI-powered medical report
              analysis and health risk
              prediction
            </p>
          </div>

          <button
            onClick={() =>
              setDarkMode(!darkMode)
            }
            className="px-4 py-2 rounded-lg bg-slate-800 text-white hover:bg-slate-700 transition"
          >
            {darkMode
              ? "☀ Light Mode"
              : "🌙 Dark Mode"}
          </button>
        </div>

        {/* Upload Section */}
        <UploadReport
          onAnalysisComplete={setAnalysis}
        />

        {/* Empty State */}
        {!analysis && (
          <div
            className={`mt-8 rounded-xl shadow-md p-10 text-center ${
              darkMode
                ? "bg-slate-800"
                : "bg-white"
            }`}
          >
            <h2 className="text-2xl font-bold mb-3">
              Upload a Medical Report
            </h2>

            <p
              className={
                darkMode
                  ? "text-slate-300"
                  : "text-slate-500"
              }
            >
              Upload a PDF or image report to
              receive:
            </p>

            <ul
              className={`mt-4 space-y-2 ${
                darkMode
                  ? "text-slate-300"
                  : "text-slate-600"
              }`}
            >
              <li>✓ OCR Data Extraction</li>
              <li>✓ Risk Prediction</li>
              <li>✓ AI Medical Summary</li>
              <li>✓ Health Recommendations</li>
              <li>✓ Trend Visualization</li>
            </ul>
          </div>
        )}

        {/* Analysis Results */}
        {analysis && (
          <div className="mt-8 space-y-6">
            {/* Risk */}
            <RiskCard
              riskLevel={
                analysis.risk_level ||
                "Unknown"
              }
              riskScore={
                analysis.risk_score || 0
              }
            />

            {/* Summary */}
            <SummaryCard
              summary={
                analysis.summary ||
                "No summary available."
              }
            />

            {/* Blood Parameters */}
            <ReportTable
              parameters={
                analysis.parameters || []
              }
            />

            {/* Trend Graph */}
            <TrendChart
              data={
                analysis.trend_data ||
                demoTrendData
              }
            />

            {/* Recommendations */}
            <Recommendations
              recommendations={
                analysis.recommendations ||
                []
              }
            />

            {/* AI Chat */}
            <ChatBot />

            {/* Download */}
            <div className="flex justify-end">
              <DownloadButton
                analysis={analysis}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;