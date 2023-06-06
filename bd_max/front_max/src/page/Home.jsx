import { Link } from "react-router-dom";

export const Home = () => {
  return (
    <div>
      <div className="home-bg" />
      <div className="body">
        <div className="home-left">
          <p>Выполнил студент группы 992441</p>
          <p>Жерносек Максим Николаевич</p>
        </div>
        <div className="home-right">
          <Link className="home-link" to="tables">
            Таблицы
          </Link>
          <Link className="home-link" to="forms">
            Формы
          </Link>
          <Link className="home-link" to="reports">
            Отчеты
          </Link>
        </div>
      </div>
    </div>
  );
};
