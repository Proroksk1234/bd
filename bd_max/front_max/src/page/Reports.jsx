import { Link } from "react-router-dom";
import Arrow from "../assets/back-arrow.png";
import { useNavigate } from "react-router-dom";

export const Reposts = () => {
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
        <div className="reports-left">
          <Link className="report-link" to="/reports/request1">
            Список объектов, предлагаемых к продаже
          </Link>
          <Link className="report-link" to="/reports/request2">
            Сальдо по видам объектов
          </Link>
          <Link className="report-link" to="/reports/request3">
            Объекты заданной стоимости
          </Link>
        </div>
        <div className="reports-right">
          <Link className="report-link" to="/reports/request4">
            Динамика продаж по районированию объектов
          </Link>
          <Link className="report-link" to="/reports/request5">
            Общий список покупателей и продавцов
          </Link>
        </div>
      </div>
    </>
  );
};
