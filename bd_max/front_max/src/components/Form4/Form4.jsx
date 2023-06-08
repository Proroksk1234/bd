import { useNavigate } from "react-router-dom";
import Arrow from "../../assets/back-arrow.png";
import { useState } from "react";
import axios from "axios";

export const Form4 = () => {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [lastName, setLastName] = useState("");
  const [patronymic, setPatronymic] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!name) {
      alert("Пожалуйста, введите имя");
      return;
    }

    if (!lastName) {
      alert("Пожалуйста, введите фамилию");
      return;
    }
    if (!patronymic) {
      alert("Пожалуйста, введите отчество");
      return;
    }
    if (!email || !email.includes("@")) {
      alert("Пожалуйста, введите правильную почту");
      return;
    }

    if (!phone || !/^\d+$/.test(phone)) {
      alert("Пожалуйста, введите правильный номер телефона");
      return;
    }
    const data = {
      name: name,
      surname: lastName,
      patronymic,
      people_type_id: 1,
      email: email,
      number_phone: phone,
    };
    axios
      .post("http://localhost:8000/api/post_peoples", data)
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
      <h2>Продавцы</h2>
      <div className="form">
        <form className="form-body" onSubmit={handleSubmit}>
          <input
            className="input"
            placeholder="имя"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <input
            className="input"
            placeholder="фамилия"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
          />
          <input
            className="input"
            placeholder="отчество"
            value={patronymic}
            onChange={(e) => setPatronymic(e.target.value)}
          />
          <input
            className="input"
            placeholder="почта"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            className="input"
            placeholder="телефон"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          <button className="form-button">Создать</button>
        </form>
      </div>
    </div>
  );
};
