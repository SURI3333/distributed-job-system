import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import SubmitJob from "./pages/SubmitJob";

function App() {
  return (
    <Router>
      <div style={{ padding: "20px" }}>
        <h1>Distributed Job Queue System</h1>

        <nav>
          <Link to="/">Dashboard</Link> |{" "}
          <Link to="/submit">Submit Job</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/submit" element={<SubmitJob />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;