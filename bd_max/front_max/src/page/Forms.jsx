import { Link } from "react-router-dom";
import Arrow from "../assets/back-arrow.png";
import { useNavigate } from "react-router-dom";

export const Forms = () => {
  const navigate = useNavigate();
  return (
    <>
      <img
        src={Arrow}
        className="arrow"
        alt="arrow"
        onClick={() => navigate(-1)}
      />
      <div className="forms">
        <div className="forms-left">
          <Link className="home-link" to="/forms/objects">
            Объекты недвижимости
          </Link>
          <Link className="home-link" to="/forms/objects-types">
            Типы объектов
          </Link>
          <Link className="home-link" to="/forms/deal-types">
            Типы сделок
          </Link>
          <Link className="home-link" to="/forms/buyers">
            Покупатели
          </Link>
        </div>
        <div className="forms-right">
          <Link className="home-link" to="/forms/sellers">
            Продавцы
          </Link>
          <Link className="home-link" to="/forms/deals">
            Сделки
          </Link>
          <Link className="home-link" to="/forms/areas">
            Районы
          </Link>
        </div>
      </div>
    </>
  );
};
