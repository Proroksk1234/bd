import { Table } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState, useEffect } from "react";
import axios from "axios";

export const Request5 = () => {
  const navigate = useNavigate();
  const [elements, setElements] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const rows = elements.map((element) => (
    <tr key={element.name}>
      <td>{element.name}</td>
      <td>{element.surname}</td>
      <td>{element.patronymic}</td>
      <td>{element.people_type_id[0].people_type}</td>
    </tr>
  ));
  const getRealEstateObjects = () => {
    axios
      .get("http://localhost:8000/api/buyers_salesman")
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
          Общий список покупателей и продавцов
        </h2>
        {isLoading ? (
          <></>
        ) : (
          <Table>
            <thead>
              <tr>
                <th>Имя</th>
                <th>Фамилия</th>
                <th>Отчество</th>
                <th>Кто</th>
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </Table>
        )}
      </div>
    </div>
  );
};
