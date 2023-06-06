import { Table } from "@mantine/core";
import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";
import axios from "axios";

export const Request3 = () => {
  const [saleFrom, setSaleFrom] = useState("");
  const [saleTo, setSaleTo] = useState("");
  const [elements, setElements] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();
  const rows = elements.map((element) => (
    <tr key={element.id}>
      <td>{element.address}</td>
      <td>{element.square}</td>
      <td>{element.cost}</td>
      <td>{element.sold ? "Да" : "Нет"}</td>
      <td>{element.obj_type_id[0].object_type}</td>
      <td>{element.district_id[0].district}</td>
    </tr>
  ));
  const handleSubmit = (event) => {
    event.preventDefault();
    axios
      .get(
        `http://localhost:8000/api/real_estate_objects_min_max_cost?min_cost=${saleFrom}&max_cost=${saleTo}`
      )
      .then((response) => {
        setElements(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  };

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
          {isLoading ? (
            <form className="form-body" onSubmit={(e) => handleSubmit(e)}>
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
          ) : (
            <Table>
              <thead>
                <tr>
                  <th>Адрес</th>
                  <th>Площадь</th>
                  <th>Цена</th>
                  <th>Продано</th>
                  <th>Тип объекта</th>
                  <th>Район</th>
                </tr>
              </thead>
              <tbody>{rows}</tbody>
            </Table>
          )}
        </div>
      </div>
    </div>
  );
};
