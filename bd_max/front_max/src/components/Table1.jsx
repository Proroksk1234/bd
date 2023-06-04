import Arrow from "../assets/back-arrow.png";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Table, Button, Input } from "@mantine/core";

export const Table1 = () => {
  const navigate = useNavigate();

  const [elements, setElements] = useState([
    { id: 1, position: 6, mass: 12.011, symbol: "C", name: "Carbon" },
    { id: 2, position: 7, mass: 14.007, symbol: "N", name: "Nitrogen" },
    { id: 3, position: 39, mass: 88.906, symbol: "Y", name: "Yttrium" },
    { id: 4, position: 56, mass: 137.33, symbol: "Ba", name: "Barium" },
    { id: 5, position: 58, mass: 140.12, symbol: "Ce", name: "Cerium" },
  ]);
  const [editingIds, setEditingIds] = useState([]);

  const startEditing = (id) => {
    setEditingIds((prevIds) => [...prevIds, id]);
  };

  const cancelEditing = (id) => {
    setEditingIds((prevIds) => prevIds.filter((editingId) => editingId !== id));
  };
  const handleDelete = (id) => {
    setElements((prevElements) =>
      prevElements.filter((element) => element.id !== id)
    );
  };
  const saveChanges = () => {
    const newElements = [...elements];

    editingIds.forEach((id) => {
      const rowInputs = document.querySelectorAll(`#row-${id} input`);
      const editedElement = { ...elements.find((e) => e.id === id) };

      rowInputs.forEach((input) => {
        editedElement[input.name] = input.value;
      });

      newElements[id - 1] = editedElement;
    });

    setElements(newElements);
    setEditingIds([]);
  };

  const rows = elements.map((element) => {
    const isEditing = editingIds.includes(element.id);

    return (
      <tr key={element.name} id={`row-${element.id}`}>
        <td>
          {isEditing ? (
            <Button color="green" onClick={() => cancelEditing(element.id)}>
              Отменить
            </Button>
          ) : (
            <Button color="green" onClick={() => startEditing(element.id)}>
              Редактировать
            </Button>
          )}
        </td>

        <td>
          {isEditing ? (
            <Input w={"100px"} name="name" defaultValue={element.name} />
          ) : (
            element.name
          )}
        </td>
        <td>
          {isEditing ? (
            <Input w={"100px"} name="symbol" defaultValue={element.symbol} />
          ) : (
            element.symbol
          )}
        </td>
        <td>
          {isEditing ? (
            <Input w={"100px"} name="mass" defaultValue={element.mass} />
          ) : (
            `${element.mass}`
          )}
        </td>
        <td>
          <Button color="red" onClick={() => handleDelete(element.id)}>
            Удалить
          </Button>
        </td>
      </tr>
    );
  });

  return (
    <div className="tables">
      <div className="wrapper">
        <img
          src={Arrow}
          className="arrow"
          alt="arrow"
          onClick={() => navigate(-1)}
        />
        <h2 style={{ textAlign: "center" }}>Объекты недвижимости</h2>
        <div className="gap">
          <Table>
            <thead>
              <tr>
                <th />
                <th>Element position</th>
                <th>Element name</th>
                <th>Symbol</th>
                <th />
              </tr>
            </thead>
            <tbody>{rows}</tbody>
          </Table>
        </div>

        {editingIds.length > 0 && (
          <div className="actions">
            <Button
              className="save-changes"
              color="orange"
              onClick={saveChanges}
            >
              Сохранить изменения
            </Button>
          </div>
        )}
      </div>
    </div>
  );
};
