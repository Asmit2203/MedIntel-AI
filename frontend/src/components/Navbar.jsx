import { FaHeartbeat } from "react-icons/fa";

function Navbar() {
  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        <div className="flex items-center gap-3">
          <FaHeartbeat
            size={28}
            className="text-red-500"
          />

          <h1 className="text-2xl font-bold text-slate-800">
            MedIntel AI
          </h1>
        </div>

        <div>
          <span className="text-slate-500 text-sm">
            Medical Report Analyzer
          </span>
        </div>

      </div>
    </nav>
  );
}

export default Navbar;