import React, { useState } from "react";
import { useParams, useHistory } from "react-router-dom";

function ChangePassword() {
  const [new_password, setNew_password] = useState("");
  const [current_password, setCurrent_password] = useState("");
  const [validationErrors, setValidationErrors] = useState({
    new_password: "",
    current_password: "",
  }); //state of input validation
  const match = useParams();
  const history = useHistory();

  function handleChangePassword(e) {
    const { value } = e.target;
    let errors = validationErrors;
    setNew_password(value);

    if (value.length < 8) {
      errors.new_password = "Минимальное колличество символоа - 2";
    } else {
      errors.new_password = '' && setValidationErrors(errors);
    }
  }

  function handleChangeCurrentPassword(e) {
    const { value } = e.target;
    let errors = validationErrors;
    setCurrent_password(value);

    if (value.length < 8) {
      errors.current_password = "Минимальное колличество символоа - 8";
    } else {
      errors.current_password = '' && setValidationErrors(errors);
    }
  }

  // const handleChangePassword = (e) => {
  //   setNew_password(e.target.value);
  // }

  // const handleChangeCurrentPassword = (e) => {
  //   setCurrent_password(e.target.value);
  // }

  function heandlerSubmit() {
    var myHeaders = new Headers();
    debugger;
    myHeaders.append("Content-Type", "application/json");
    const raw = JSON.stringify({
      uid: match.Ng,
      token: match.id,
      new_password: new_password,
    });
    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow",
    };
    fetch("http://127.0.0.1:8000/users/reset_password_confirm/", requestOptions)
      .then(() => history.push("/sign-in"))
      .catch((error) => console.log("error", error));
  }
  console.log(new_password);
  console.log(current_password);
  return (
    <main className="LinkForm">
      <form className="LinkForm__form">
        <label className="LinkForm__label">
          <h2 className="LinkForm__subtitlte">Новый пороль</h2>
          <input
            className="LinkForm__input"
            required
            value={new_password || ""}
            name="new_password"
            type="password"
            minLength="8"
            placeholder="пароль дожен сотсоять из букв и цифр"
            onChange={handleChangePassword}
          />
          <div
            className={`Comment__input-hidden ${
              validationErrors.new_password ? "Comment__input-error" : ""
            }`}
          >
            {validationErrors.new_password}
          </div>
        </label>
        <label className="LinkForm__label">
          <h2 className="LinkForm__subtitlte">Повторить новый пороль</h2>
          <input
            className="LinkForm__input"
            required
            value={current_password || ""}
            name="current_password"
            placeholder="повторите пожалуйста пароль"
            type="password"
            minLength="8"
            onChange={handleChangeCurrentPassword}
          />
          <div
            className={`Comment__input-hidden ${
              validationErrors.current_password ? "Comment__input-error" : ""
            }`}
          >
            {validationErrors.current_password}
          </div>
        </label>
      </form>
      <button
        className={`LinkForm__button ${
          !new_password.length ||
          !current_password.length ||
          validationErrors.new_passwor ||
          validationErrors.current_password
            ? "Comment__button_disabled"
            : ""
        }`}
        type="submit"
        onClick={heandlerSubmit}
        disabled={
          !new_password.length ||
          !current_password.length ||
          validationErrors.new_passwor ||
          validationErrors.current_password
        }
      >
        Сохранить
      </button>
      <div className="LinkForm__inputHidden LinkForm__inputError"></div>
    </main>
  );
}

export default ChangePassword;
