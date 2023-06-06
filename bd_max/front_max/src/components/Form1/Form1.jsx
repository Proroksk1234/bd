import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";

export const Form1 = () => {
  const navigate = useNavigate();
  const [area, setArea] = useState("");
  const [adres, setAdres] = useState("");
  const [square, setSqueare] = useState("");
  const [sell, setSell] = useState("");

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
        <form
          className="form-body"
          onSubmit={(event) => {
            event.preventDefault();
          }}
        >
          <input
            className="input"
            placeholder="район"
            value={area}
            onChange={(e) => setArea(e.target.value)}
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
      </div>
    </div>
  );
};
