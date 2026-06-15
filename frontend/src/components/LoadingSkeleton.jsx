function LoadingSkeleton() {

  return (

    <div className="animate-pulse bg-white p-6 rounded-xl shadow">

      <div className="h-6 bg-slate-200 rounded mb-4"></div>

      <div className="h-4 bg-slate-200 rounded mb-2"></div>

      <div className="h-4 bg-slate-200 rounded mb-2"></div>

      <div className="h-4 bg-slate-200 rounded"></div>

    </div>

  );
}

export default LoadingSkeleton;