import { Table } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import Arrow from "../../assets/back-arrow.png";
import axios from "axios";

export const Request2 = () => {
  const navigate = useNavigate();
  const [elements, setElements] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const rows = elements.map((element) => (
    <tr key={element.name}>
      <td>{element.object_type}</td>
      <td>{element.sum}</td>
    </tr>
  ));
  const getRealEstateObjects = () => {
    axios
      .get("http://localhost:8000/api/saldo")
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
        <h2 style={{ textAlign: "center" }}>Сальдо по видам объектов</h2>
        {isLoading ? (
          <></>
        ) : (
          <Table>
            <thead>
              <tr>
                <th>Типы объектов</th>
                <th>Сальдо</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </Table>
        )}
      </div>
    </div>
  );
};
