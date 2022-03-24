import React, { useState, useContext } from "react";
import AuthContext from "../../context/AuthContext";
//import MainContext from "../../context/MainContext";
import UserForm from "../userForm/UserForm";
import useFormValidation from "../../utils/hooks/useFormValidation";

function Profile({ userInfo, setUserInfo}) {
  const [input, setInput] = useState("");
  const { values, handleChange, errors, isValid } = useFormValidation();
  let {authTokens} = useContext(AuthContext)

  function handleChangeInput(e) {
    handleChange(e);
    if (input.length > 0) {
      setInput("");
    }
  }
  const handleUpdateUser = async (e) => {
    e.preventDefault();
    let response = await fetch("http://127.0.0.1:8000/users/me/", {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
      body: JSON.stringify({
        first_name: e.target.first_name.values,
        last_name: e.target.last_name.values,
        phone: e.target.phone.values,
      }),
    });

    let data = await response.json();

    if (response.status === 200) {
      setUserInfo({
        ...userInfo,
        first_name: data.first_name.value,
        last_name: data.last_name.value,
        phone: data.phone.value,
      });
      localStorage.setItem("userPers", JSON.stringify(userInfo));
      window.location.reload();
    } else if (response.statusText === "Unauthorized") {
      console.log("error!");
    }
  };

  console.log(userInfo)
  
  return (
    <UserForm
      title="Привет,"
      userName={userInfo.first_name}
      onSubmit={handleUpdateUser}
      buttonText="Сохранить"
      errors={!isValid}
      disabled={!isValid}
    >
      <div className="userForm__form-container">
        <label className="userForm__label">
          <h2 className="userForm__subtitle">Имя</h2>
          <input
            value={values.first_name || ""}
            placeholder={userInfo.first_name}
            title="Имя"
            name="first_name"
            type="text"
            minLength="3"
            autoComplete="on"
            className="userForm__input"
            maxLength="30"
            onChange={handleChangeInput}
          />
          <div
            className={`Form__input-hidden ${
              errors.first_name ? "Form__input-error" : ""
            }`}
          >
            {errors.first_name}
          </div>
        </label>
        <label className="userForm__label">
          <h2 className="userForm__subtitle">Фамилия</h2>
          <input
            value={values.last_name || ""}
            placeholder={userInfo.last_name}
            title="Фамилия"
            name="last_name"
            type="text"
            minLength="3"
            autoComplete="on"
            className="userForm__input"
            maxLength="30"
            onChange={handleChangeInput}
          />
          <div
            className={`Form__input-hidden ${
              errors.last_name ? "Form__input-error" : ""
            }`}
          >
            {errors.last_name}
          </div>
        </label>
      </div>
      <label className="userForm__label">
        <h2 className="userForm__subtitle">Телефон</h2>
        <input
          value={values.phone || ""}
          placeholder={userInfo.phone}
          title="Телефон"
          type="tel"
          name="phone"
          pattern="\+7\s?[\(]{0,1}9[0-9]{2}[\)]{0,1}\s?\d{3}[-]{0,1}\d{2}[-]{0,1}\d{2}"
          autoComplete="on"
          className="userForm__input"
          onChange={handleChangeInput}
        />
        <div
          className={`Form__input-hidden ${
            errors.phone ? "Form__input-error" : ""
          }`}
        >
          {errors.phone}
        </div>
      </label>
    </UserForm>
  );
}

export default Profile;
