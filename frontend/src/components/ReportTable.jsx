function ReportTable({ parameters }) {

  if (!parameters || parameters.length === 0)
    return null;

  const getStatusColor = (status) => {

    switch (status?.toLowerCase()) {

      case "high":
        return "text-red-500";

      case "low":
        return "text-yellow-500";

      default:
        return "text-green-600";
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">

      <h2 className="text-xl font-bold mb-4">
        Blood Parameters
      </h2>

      <div className="overflow-x-auto">

        <table className="w-full border-collapse">

          <thead>

            <tr className="bg-slate-100">

              <th className="text-left p-3">
                Parameter
              </th>

              <th className="text-left p-3">
                Value
              </th>

              <th className="text-left p-3">
                Status
              </th>

            </tr>

          </thead>

          <tbody>

            {parameters.map((item, index) => (

              <tr
                key={index}
                className="border-b"
              >

                <td className="p-3">
                  {item.name}
                </td>

                <td className="p-3">
                  {item.value}
                </td>

                <td
                  className={`p-3 font-semibold ${getStatusColor(item.status)}`}
                >
                  {item.status}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default ReportTable;