import { Link } from "react-router-dom";
import Arrow from "../assets/back-arrow.png";
import { useNavigate } from "react-router-dom";

export const Tables = () => {
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
          <Link className="home-link" to="/tables/objects">
            Объекты недвижимости
          </Link>
          <Link className="home-link" to="/tables/objects-types">
            Типы объектов
          </Link>
          <Link className="home-link" to="/tables/deal-types">
            Типы сделок
          </Link>
          <Link className="home-link" to="/tables/buyers">
            Покупатели
          </Link>
        </div>
        <div className="forms-right">
          <Link className="home-link" to="/tables/sellers">
            Продавцы
          </Link>
          <Link className="home-link" to="/tables/deals">
            Сделки
          </Link>
          <Link className="home-link" to="/tables/areas">
            Районы
          </Link>
        </div>
      </div>
    </>
  );
};
