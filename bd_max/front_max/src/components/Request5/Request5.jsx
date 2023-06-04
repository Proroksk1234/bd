import { Table } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";

export const Request5 = () => {
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
      <div className="wrapper">
        <h2 style={{ textAlign: "center" }}>
          Общий список покупателей и продавцов
        </h2>
        <Table>
          <thead>
            <tr>
              <th>Element position</th>
              <th>Element name</th>
              <th>Symbol</th>
              <th>Atomic mass</th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </Table>
      </div>
    </div>
  );
};
