import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState, useEffect } from "react";
import { Select } from "@mantine/core";
import axios from "axios";

export const Form6 = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(true);
  const [deal, setDeal] = useState("");
  const [object, setObject] = useState("");
  const [buyer, setBuyer] = useState("");
  const [seller, setSeller] = useState("");
  const [date, setDate] = useState("");
  const [select1, setSelect1] = useState([]);
  const [select2, setSelect2] = useState([]);
  const [select3, setSelect3] = useState([]);
  const [select4, setSelect4] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = {
      deal_type_id: deal,
      real_estate_object_id: object,
      buyer_id: buyer,
      salesman_id: seller,
      date,
    };
    console.log(data);
    axios
      .post("http://localhost:8000/api/post_deals", data)
      .then((response) => {
        navigate(-1);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const getSelect1 = () => {
    axios
      .get("http://localhost:8000/api/get_all_deal_types")
      .then((response) => {
        const res = response.data.map((e) => ({
          value: e.id,
          label: e.deal_type,
        }));
        setSelect1(res);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const getSelect2 = () => {
    axios
      .get("http://localhost:8000/api/get_all_real_estate_objects")
      .then((response) => {
        const res = response.data.map((e) => ({
          value: e.id,
          label: `${e.obj_type_id[0].object_type} ${e.district_id[0].district} ${e.address} ${e.cost} ${e.square}`,
        }));
        setSelect2(res);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const getSelect3 = () => {
    axios
      .get("http://localhost:8000/api/get_all_buyers")
      .then((response) => {
        const res = response.data.map((e) => ({
          value: e.id,
          label: `${e.name} ${e.surname}`,
        }));
        setSelect3(res);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const getSelect4 = () => {
    axios
      .get("http://localhost:8000/api/get_all_salesman")
      .then((response) => {
        const res = response.data.map((e) => ({
          value: e.id,
          label: `${e.name} ${e.surname}`,
        }));
        setSelect4(res);
      })
      .catch((error) => {
        console.error(error);
      });
  };
  useEffect(() => {
    getSelect1();
    getSelect2();
    getSelect3();
    getSelect4();
  }, []);

  return (
    <div className="form-page">
      <img
        src={Arrow}
        className="arrow"
        alt="arrow"
        onClick={() => navigate(-1)}
      />
      <h2>Сделки</h2>
      <div className="form"></div>
      {isLoading ? (
        <></>
      ) : (
        <form className="form-body" onSubmit={handleSubmit}>
          <Select
            placeholder="тип сделки"
            value={deal}
            onChange={setDeal}
            data={select1}
          />
          <Select
            placeholder="объект недвижимости"
            value={object}
            onChange={setObject}
            data={select2}
          />
          <Select
            placeholder="покупатель"
            value={buyer}
            onChange={setBuyer}
            data={select3}
          />
          <Select
            placeholder="Продавец"
            value={seller}
            onChange={setSeller}
            data={select4}
          />
          <input
            className="input"
            placeholder="дата"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
          <button className="form-button">Создать</button>
        </form>
      )}
    </div>
  );
};
