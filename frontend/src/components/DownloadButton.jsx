function DownloadButton({ analysis }) {

  const downloadReport = () => {

    const blob = new Blob(
      [
        JSON.stringify(
          analysis,
          null,
          2
        )
      ],
      {
        type: "application/json"
      }
    );

    const url =
      URL.createObjectURL(blob);

    const a =
      document.createElement("a");

    a.href = url;

    a.download =
      "medical_analysis.json";

    a.click();
  };

  return (
    <button
      onClick={downloadReport}
      className="bg-green-600 text-white px-5 py-3 rounded-lg"
    >
      Download Report
    </button>
  );
}

export default DownloadButton;