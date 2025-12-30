import { Routes, Route } from "react-router-dom";
import Hero from "./pages/Hero";
import Dashboard from "./pages/Dashboard";

const App = () => {
  return (
    <div className="overflow-x-hidden">
      <Routes>
        <Route path="/" element={<Hero />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
    </div>
  );
};

export default App;
