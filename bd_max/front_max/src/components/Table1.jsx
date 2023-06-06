import Arrow from "../assets/back-arrow.png";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Table, Button, Input } from "@mantine/core";
import axios from "axios";

export const Table1 = () => {
  const navigate = useNavigate();

  const [elements, setElements] = useState([]);
  const [editingIds, setEditingIds] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const startEditing = (id) => {
    if (!editingIds.includes(id)) {
      setEditingIds((prevIds) => [...prevIds, id]);
    }
  };

  const cancelEditing = (id) => {
    setEditingIds((prevIds) => prevIds.filter((editingId) => editingId !== id));
  };

  const deleteObj = (id) => {
    axios
      .delete(`http://localhost:8000/api/delete_real_estate_objects/${id}`)
      .then((response) => {
        setElements((prevElements) =>
          prevElements.filter((element) => element.id !== id)
        );
      })
      .catch((error) => {
        console.error(error);
      });
  };

  const handleDelete = (id) => {
    deleteObj(id);
  };
  const updateObj = (id, updatedElement) => {
    const district_id = updatedElement.district_id[0].id;
    const obj_type_id = updatedElement.obj_type_id[0].id;
    const { cost, square, sold, address } = updatedElement;
    const data = {
      cost: Number(cost),
      square: Number(square),
      sold: !!sold,
      district_id,
      obj_type_id,
      address,
    };
    console.log(data);
    axios
      .put(`http://localhost:8000/api/update_real_estate_objects/${id}`, data)
      .then((response) => {
        setElements((prevElements) =>
          prevElements.map((element) =>
            element.id === id ? updatedElement : element
          )
        );
      })
      .catch((error) => {
        console.error(error);
      });
  };
  const saveChanges = () => {
    elements.forEach((element) => {
      const isEditing = editingIds.includes(element.id);

      if (isEditing) {
        const rowInputs = document.querySelectorAll(`#row-${element.id} input`);
        let editedElement = { ...element };

        rowInputs.forEach((input) => {
          editedElement[input.name] = input.value;
        });

        updateObj(editedElement.id, editedElement);
      }
    });

    setEditingIds([]);
  };

  const rows = elements.map((element) => {
    const isEditing = editingIds.includes(element.id);

    return (
      <tr key={element.id} id={`row-${element.id}`}>
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
            <Input w={"100px"} name="address" defaultValue={element.address} />
          ) : (
            element.address
          )}
        </td>
        <td>
          {isEditing ? (
            <Input w={"100px"} name="square" defaultValue={element.square} />
          ) : (
            element.square
          )}
        </td>
        <td>
          {isEditing ? (
            <Input w={"100px"} name="cost" defaultValue={element.cost} />
          ) : (
            element.cost
          )}
        </td>
        <td>
          {isEditing ? (
            <Input w={"100px"} name="sold" defaultValue={element.sold} />
          ) : element.sold ? (
            "Да"
          ) : (
            "Нет"
          )}
        </td>
        <td>
          {isEditing ? (
            <Input
              w={"100px"}
              name="object_type"
              defaultValue={element.obj_type_id[0].object_type}
            />
          ) : (
            element.obj_type_id[0].object_type
          )}
        </td>
        <td>
          {isEditing ? (
            <Input
              w={"100px"}
              name="object_type"
              defaultValue={element.district_id[0].district}
            />
          ) : (
            element.district_id[0].district
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

  const getRealEstateObjects = () => {
    axios
      .get("http://localhost:8000/api/get_all_real_estate_objects")
      .then((response) => {
        setElements(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error(error);
      });
  };

  useEffect(() => {
    getRealEstateObjects();
  }, []);

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
        {isLoading ? (
          <></>
        ) : (
          <div className="gap">
            <Table>
              <thead>
                <tr>
                  <th />
                  <th>Адрес</th>
                  <th>Площадь</th>
                  <th>Цена</th>
                  <th>Продано</th>
                  <th>Тип объекта</th>
                  <th>Район</th>
                  <th />
                </tr>
              </thead>
              <tbody>{rows}</tbody>
            </Table>
          </div>
        )}
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
