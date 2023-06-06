import Arrow from "../assets/back-arrow.png";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Table, Button, Input } from "@mantine/core";
import axios from "axios";
export const Table6 = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(true);

  const [elements, setElements] = useState([]);
  const [editingIds, setEditingIds] = useState([]);

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
      .delete(`http://localhost:8000/api/delete_deals/${id}`)
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
  console.log(updatedElement)
          const buyer_id = updatedElement.buyer_id[0].id;
    const deal_type_id = updatedElement.deal_type_id[0].id;
    const real_estate_object_id = updatedElement.real_estate_object_id[0].id;
    const salesman_id = updatedElement.salesman_id[0].id;
    const date=updatedElement.date.split("T")[0]
    const data = {
    buyer_id,
    deal_type_id,
    real_estate_object_id,
    salesman_id,
    date,
    };
    console.log(data);
    axios
      .put(`http://localhost:8000/api/update_deals/${id}`, data)
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
            <Input
              w={"100px"}
              name="deal_type"
              defaultValue={element.deal_type_id[0].deal_type}
            />
          ) : (
            element.deal_type_id[0].deal_type
          )}
        </td>
        <td>
          {isEditing ? (
            <Input
              w={"100px"}
              name="object_type"
              defaultValue={
                element.real_estate_object_id[0].obj_type_id[0].object_type
              }
            />
          ) : (
            element.real_estate_object_id[0].obj_type_id[0].object_type
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="district"
              defaultValue={
                element.real_estate_object_id[0].district_id[0].district
              }
            />
          ) : (
            element.real_estate_object_id[0].district_id[0].district
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="address"
              defaultValue={element.real_estate_object_id[0].address}
            />
          ) : (
            element.real_estate_object_id[0].address
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="square"
              defaultValue={element.real_estate_object_id[0].square}
            />
          ) : (
            element.real_estate_object_id[0].square
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="cost"
              defaultValue={element.real_estate_object_id[0].cost}
            />
          ) : (
            element.real_estate_object_id[0].cost
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="sold"
              defaultValue={element.real_estate_object_id[0].sold}
            />
          ) : element.real_estate_object_id[0].sold ? (
            "Да"
          ) : (
            "Нет"
          )}
        </td>
        <td>
          {isEditing ? (
            <Input
              w={"100px"}
              name="name"
              defaultValue={element.buyer_id[0].name}
            />
          ) : (
            element.buyer_id[0].name
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="surname"
              defaultValue={element.buyer_id[0].surname}
            />
          ) : (
            element.buyer_id[0].surname
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="patronymic"
              defaultValue={element.buyer_id[0].patronymic}
            />
          ) : (
            element.buyer_id[0].patronymic
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="email"
              defaultValue={element.buyer_id[0].email}
            />
          ) : (
            element.buyer_id[0].email
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="cost"
              defaultValue={element.buyer_id[0].number_phone}
            />
          ) : (
            element.buyer_id[0].number_phone
          )}
        </td>
        <td>
          {isEditing ? (
            <Input
              w={"100px"}
              name="name"
              defaultValue={element.salesman_id[0].name}
            />
          ) : (
            element.salesman_id[0].name
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="surname"
              defaultValue={element.salesman_id[0].surname}
            />
          ) : (
            element.salesman_id[0].surname
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="patronymic"
              defaultValue={element.salesman_id[0].patronymic}
            />
          ) : (
            element.salesman_id[0].patronymic
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="email"
              defaultValue={element.salesman_id[0].email}
            />
          ) : (
            element.salesman_id[0].email
          )}
          <br />
          {isEditing ? (
            <Input
              w={"100px"}
              name="cost"
              defaultValue={element.salesman_id[0].number_phone}
            />
          ) : (
            element.salesman_id[0].number_phone
          )}
        </td>
        <td>
          {isEditing ? (
            <Input w={"100px"} name="date" defaultValue={element.date.split("T")[0]} />
          ) : (
            element.date.split("T")[0]
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
      .get("http://localhost:8000/api/get_all_deals")
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
        <h2 style={{ textAlign: "center" }}>Сделки</h2>
        <div className="gap">
          {isLoading ? (
            <></>
          ) : (
            <Table>
              <thead>
                <tr>
                  <th />
                  <th>Тип сделки</th>
                  <th>Объект недвижимости</th>
                  <th>Покупатель</th>
                  <th>Продавец</th>
                  <th>Дата</th>
                  <th />
                </tr>
              </thead>
              <tbody>{rows}</tbody>
            </Table>
          )}
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
