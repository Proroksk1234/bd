import { Table } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from "axios";
import Arrow from "../../assets/back-arrow.png";

export const Request4 = () => {
  const navigate = useNavigate();
  const [elements, setElements] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const rows = elements.map((element) => (
    <tr key={element.district}>
      <td>{element.district}</td>
      <td>{element.sales_count}</td>
      <td>{element.year}</td>
    </tr>
  ));
  const getRealEstateObjects = () => {
    axios
      .get("http://localhost:8000/api/dynamic_ceil")
      .then((response) => {
        setElements(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    getRealEstateObjects();
  }, []);
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
          Динамика продаж по районированию объектов
        </h2>
        <Table>
          <thead>
            <tr>
              <th>Район</th>
              <th>Количество продаж</th>
              <th>Год</th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </Table>
      </div>
    </div>
  );
};
