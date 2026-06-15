function Recommendations({ recommendations }) {

  if (!recommendations || recommendations.length === 0)
    return null;

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-4">
        Health Recommendations
      </h2>

      <ul className="space-y-3">

        {recommendations.map((item, index) => (

          <li
            key={index}
            className="bg-slate-50 p-4 rounded-lg"
          >
            • {item}
          </li>

        ))}

      </ul>

    </div>
  );
}

export default Recommendations;