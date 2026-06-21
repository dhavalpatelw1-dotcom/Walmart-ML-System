import { useState } from "react";

function App() {

  const [form, setForm] = useState({
    Store: 1,
    Holiday_Flag: 0,
    Temperature: 45,
    Fuel_Price: 3.5,
    CPI: 200,
    Unemployment: 7,
    Year: 2012,
    Month: 5,
    Week: 20,
    Quarter: 2,
    Lag1: 15000,
    Lag2: 14000,
    Lag3: 13000,
    Rolling_Mean: 14500
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: Number(e.target.value)
    });
  };

  const predict = async () => {

    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    const data = await res.json();

    setResult(data.prediction);
  };

  return (

    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">

      <h1 className="text-3xl font-bold mb-6">
        Walmart Sales Prediction Dashboard
      </h1>

      <div className="bg-white p-6 rounded-2xl shadow-lg w-full max-w-3xl">

        <div className="grid grid-cols-2 gap-4">

          {Object.keys(form).map((key) => (

            <div key={key}>

              <label className="block text-sm font-semibold">
                {key}
              </label>

              <input
                className="w-full border rounded-lg p-2"
                name={key}
                value={form[key]}
                onChange={handleChange}
              />

            </div>

          ))}

        </div>

        <button
          onClick={predict}
          className="mt-6 w-full bg-blue-600 text-white p-3 rounded-xl hover:bg-blue-700"
        >
          Predict Sales
        </button>

        {result && (

          <div className="mt-6 text-center">

            <h2 className="text-xl font-bold text-green-600">
              Prediction: {result}
            </h2>

          </div>

        )}

      </div>

    </div>

  );
}

export default App;