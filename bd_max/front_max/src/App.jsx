import "./App.css";
import { Routes, Route } from "react-router-dom";
import { Home } from "./page/Home";
import { Tables } from "./page/Tables";
import { Forms } from "./page/Forms";
import { Reposts } from "./page/Reports";
import { Form1 } from "./components/Form1/Form1";
import { Form2 } from "./components/Form2/Form2";
import { Form3 } from "./components/Form3/Form3";
import { Form4 } from "./components/Form4/Form4";
import { Form5 } from "./components/Form5/Form5";
import { Form6 } from "./components/Form6/Form6";
import { Form7 } from "./components/Form7/Form7";
import { Request1 } from "./components/Request1/Request1";
import { Request5 } from "./components/Request5/Request5";
import { Request2 } from "./components/Request2/Request2";
import { Request3 } from "./components/Request3/Request3";
import { Request4 } from "./components/Request4/Request4";
import { Table1 } from "./components/Table1";
import { Table2 } from "./components/Table2";
import { Table3 } from "./components/Table3";
import { Table4 } from "./components/Table4";
import { Table5 } from "./components/Table5";
import { Table6 } from "./components/Table6";
import { Table7 } from "./components/Table7";

function App() {
  return (
    <div className="layout">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/tables" element={<Tables />} />
        <Route path="/forms" element={<Forms />} />
        <Route path="/reports" element={<Reposts />} />
        <Route path="/forms/objects" element={<Form1 />} />
        <Route path="/forms/objects-types" element={<Form2 />} />
        <Route path="/forms/deal-types" element={<Form3 />} />
        <Route path="/forms/buyers" element={<Form4 />} />
        <Route path="/forms/sellers" element={<Form5 />} />
        <Route path="/forms/deals" element={<Form6 />} />
        <Route path="/forms/areas" element={<Form7 />} />
        <Route path="/reports/request1" element={<Request1 />} />
        <Route path="/reports/request2" element={<Request2 />} />
        <Route path="/reports/request3" element={<Request3 />} />
        <Route path="/reports/request4" element={<Request4 />} />
        <Route path="/reports/request5" element={<Request5 />} />
        <Route path="/tables/objects" element={<Table1 />} />
        <Route path="/tables/objects-types" element={<Table2 />} />
        <Route path="/tables/deal-types" element={<Table3 />} />
        <Route path="/tables/buyers" element={<Table4 />} />
        <Route path="/tables/sellers" element={<Table5 />} />
        <Route path="/tables/deals" element={<Table6 />} />
        <Route path="/tables/areas" element={<Table7 />} />
      </Routes>
    </div>
  );
}

export default App;
