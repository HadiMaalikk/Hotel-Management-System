import { Routes, Route } from "react-router-dom";
import Hero from "./pages/Hero";

const App = () => {
  return (
    <div className="overflow-x-hidden">
      <Routes>
        <Route path="/" element={<Hero />} />
      </Routes>
    </div>
  );
};

export default App;
