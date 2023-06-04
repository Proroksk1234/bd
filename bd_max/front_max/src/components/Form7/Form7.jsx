import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";

export const Form7 = () => {
  const navigate = useNavigate();
  const [area, setArea] = useState("");

  return (
    <div className="form-page">
      <img
        src={Arrow}
        className="arrow"
        alt="arrow"
        onClick={() => navigate(-1)}
      />
      <h2>Районы</h2>
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
          <button className="form-button">Создать</button>
        </form>
      </div>
    </div>
  );
};
