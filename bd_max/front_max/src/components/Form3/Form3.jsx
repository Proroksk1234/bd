import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";

export const Form3 = () => {
  const navigate = useNavigate();
  const [name, setName] = useState("");

  return (
    <div className="form-page">
      <img
        src={Arrow}
        className="arrow"
        alt="arrow"
        onClick={() => navigate(-1)}
      />
      <h2>Типы сделок</h2>
      <div className="form">
        <form
          className="form-body"
          onSubmit={(event) => {
            event.preventDefault();
          }}
        >
          <input
            className="input"
            placeholder="название"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <button className="form-button">Создать</button>
        </form>
      </div>
    </div>
  );
};
