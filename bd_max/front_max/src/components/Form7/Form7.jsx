import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";
import axios from "axios";

export const Form7 = () => {
  const navigate = useNavigate();
  const [area, setArea] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = { district: area };
    axios
      .post("http://localhost:8000/api/post_districts", data)
      .then((response) => {
        navigate(-1);
      })
      .catch((error) => {
        console.error(error);
      });
  };

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
        <form className="form-body" onSubmit={handleSubmit}>
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
