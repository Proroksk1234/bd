import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";
import axios from "axios";

export const Form2 = () => {
  const navigate = useNavigate();
  const [name, setName] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = { object_type: name };
    axios
      .post("http://localhost:8000/api/post_object_types", data)
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
      <h2>Типы объектов</h2>
      <div className="form">
        <form className="form-body" onSubmit={handleSubmit}>
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
