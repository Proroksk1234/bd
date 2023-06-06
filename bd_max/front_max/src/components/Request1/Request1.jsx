import { useState, useEffect } from "react";
import { Table } from "@mantine/core";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";

export const Request1 = () => {
  const navigate = useNavigate();
    const [elements, setElements] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const rows = elements.map((element) => {
    return (
      <tr key={element.id} id={`row-${element.id}`}>
        <td>{element.address}
        </td>
        <td>{element.square}
        </td>
        <td>{element.cost}
        </td>
        <td>{ element.sold?"Да":"Нет"}
        </td>
        <td>
            {element.obj_type_id[0].object_type}
        </td>
        <td>
            {element.district_id[0].district}
        </td>
      </tr>
    );
  });

  const getRealEstateObjects = () => {
    axios
      .get("http://localhost:8000/api/all_object_sales")
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
          Список объектов, предлагаемых к продаже
        </h2>
        {isLoading?<></>:<Table>
          <thead>
            <tr>
              <th></th>
              <th></th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </Table> }

      </div>
    </div>
  );
};
