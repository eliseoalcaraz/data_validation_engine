import { useState } from "react";

const getApiUrl = () => {
  const hostname = window.location.hostname;
  const port = 8000;
  return `http://${hostname}:${port}`;
};

const apiUrl = getApiUrl();

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string>("");

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) return;
    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      console.log(`Fetching from: ${apiUrl}/validate`);
      const response = await fetch(`${apiUrl}/validate`, {
        method: "POST",
        body: formData,
      });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      setResult(data);
    } catch (err: any) {
      console.error("Error:", err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>CSV Validator</h1>
      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleSubmit} disabled={loading || !file}>
        {loading ? "Processing..." : "Submit"}
      </button>

      {error && <div style={{ color: "red" }}>{error}</div>}

      {result && result.status === "pass" && (
        <div style={{ color: "green", marginTop: 20 }}>
          Validation Successful: Data is clean.
        </div>
      )}

      {result && result.status === "fail" && (
        <table border={1} style={{ marginTop: 20 }}>
          <thead>
            <tr>
              <th>ID</th>
              <th>Row Number</th>
              <th>Column</th>
              <th>Error Description</th>
            </tr>
          </thead>
          <tbody>
            {result.errors.map((err: any, idx: number) => (
              <tr key={idx}>
                <td>{err.id ?? ""}</td>
                <td>{err.row_index ?? ""}</td>
                <td>{err.column ?? ""}</td>
                <td>{err.error_message}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
