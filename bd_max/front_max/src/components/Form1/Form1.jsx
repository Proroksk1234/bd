import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState, useEffect } from "react";
import { Select } from "@mantine/core";
import axios from "axios";

export const Form1 = () => {
  const navigate = useNavigate();
  const [elements, setElements] = useState([]);
  const [elements2, setElements2] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [objType, setObjType] = useState("");
  const [area, setArea] = useState("");
  const [adres, setAdres] = useState("");
  const [square, setSqueare] = useState("");
  const [sell, setSell] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = {
      address: adres,
      cost: Number(sell),
      square: Number(square),
      district_id: area,
      obj_type_id: objType,
    };
    axios
      .post("http://localhost:8000/api/post_real_estate_objects", data)
      .then((response) => {
        navigate(-1);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const getRealEstateObjects = () => {
    axios
      .get("http://localhost:8000/api/get_all_districts")
      .then((response) => {
        const res = response.data.map((e) => ({
          value: e.id,
          label: e.district,
        }));
        setElements(res);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const getRealEstateObjects2 = () => {
    axios
      .get("http://localhost:8000/api/get_all_type_obj")
      .then((response) => {
        const res = response.data.map((e) => ({
          value: e.id,
          label: e.object_type,
        }));
        setElements2(res);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    getRealEstateObjects();
    getRealEstateObjects2();
  }, []);
  return (
    <div className="form-page">
      <img
        src={Arrow}
        className="arrow"
        alt="arrow"
        onClick={() => navigate(-1)}
      />
      <h2>Объекты недвижимости</h2>
      <div className="form">
        {isLoading ? (
          <></>
        ) : (
          <form className="form-body" onSubmit={handleSubmit}>
            <Select
              placeholder="Район"
              value={area}
              onChange={setArea}
              data={elements}
            />
            <Select
              placeholder="тип объекта"
              value={objType}
              onChange={setObjType}
              data={elements2}
            />
            <input
              className="input"
              placeholder="адрес"
              value={adres}
              onChange={(e) => setAdres(e.target.value)}
            />
            <input
              className="input"
              placeholder="площадь"
              value={square}
              onChange={(e) => setSqueare(e.target.value)}
            />
            <input
              className="input"
              placeholder="стоимость"
              value={sell}
              onChange={(e) => setSell(e.target.value)}
            />
            <button className="form-button">Создать</button>
          </form>
        )}
      </div>
    </div>
  );
};
