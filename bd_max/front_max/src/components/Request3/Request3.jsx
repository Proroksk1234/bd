import { Table } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";

export const Request3 = () => {
  const [saleFrom, setSaleFrom] = useState("");
  const [saleTo, setSaleTo] = useState("");
  const navigate = useNavigate();
  const elements = [
    { position: 6, mass: 12.011, symbol: "C", name: "Carbon" },
    { position: 7, mass: 14.007, symbol: "N", name: "Nitrogen" },
    { position: 39, mass: 88.906, symbol: "Y", name: "Yttrium" },
    { position: 56, mass: 137.33, symbol: "Ba", name: "Barium" },
    { position: 58, mass: 140.12, symbol: "Ce", name: "Cerium" },
  ];
  const rows = elements.map((element) => (
    <tr key={element.name}>
      <td>{element.position}</td>
      <td>{element.name}</td>
      <td>{element.symbol}</td>
      <td>{element.mass}</td>
    </tr>
  ));
  return (
    <div className="req">
      <img
        src={Arrow}
        className="arrow"
        alt="arrow"
        onClick={() => navigate(-1)}
      />
      <h2 style={{ textAlign: "center" }}>Объекты заданной стоимости</h2>
      <div className="wrapper">
        <div className="req-flex">
          <form
            className="form-body"
            onSubmit={(event) => {
              event.preventDefault();
            }}
          >
            <input
              className="input"
              placeholder="Цена от"
              value={saleFrom}
              onChange={(e) => setSaleFrom(e.target.value)}
            />
            <input
              className="input"
              placeholder="Цена до"
              value={saleTo}
              onChange={(e) => setSaleTo(e.target.value)}
            />
            <button className="form-button">Создать</button>
          </form>
        </div>
      </div>
    </div>
  );
};
