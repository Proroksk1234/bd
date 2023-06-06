import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";

export const Form6 = () => {
  const navigate = useNavigate();
  const [deal, setDeal] = useState("");
  const [object, setObject] = useState("");
  const [buyer, setBuyer] = useState("");
  const [seller, setSeller] = useState("");
  const [date, setDate] = useState("");

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
      <form
        className="form-body"
        onSubmit={(event) => {
          event.preventDefault();
        }}
      >
        <input
          className="input"
          placeholder="тип сделки"
          value={deal}
          onChange={(e) => setDeal(e.target.value)}
        />
        <input
          className="input"
          placeholder="объект недвижимости"
          value={object}
          onChange={(e) => setAdres(e.target.value)}
        />
        <input
          className="input"
          placeholder="покупатель"
          value={buyer}
          onChange={(e) => setBuyer(e.target.value)}
        />
        <input
          className="input"
          placeholder="Продавец"
          value={seller}
          onChange={(e) => setSeller(e.target.value)}
        />
        <input
          className="input"
          placeholder="дата"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
        <button className="form-button">Создать</button>
      </form>
    </div>
  );
};
