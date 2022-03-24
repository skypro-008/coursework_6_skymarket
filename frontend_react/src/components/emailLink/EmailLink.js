import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import useFormValidation from "../../utils/hooks/useFormValidation";

function EmailLink() {
  const [email, setEmail] = useState("");
  const { values, handleChange, errors, isValid } = useFormValidation();
  const history = useHistory();

  const handleChangeEmail = (e) => {
    handleChange(e);
    if (email.length > 0) {
      setEmail("");
    }
  };

  function heandlerSubmit(e) {
    e.preventDefault();
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const raw = JSON.stringify({
      email: values.email,
    });
    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow",
    };
    fetch("http://127.0.0.1:8000/users/reset_password/", requestOptions)
      .then(() => history.push("/sign-in"))
      .catch((error) => console.log("error", error));
  }
  console.log(values.email);
  return (
    <main className="LinkForm">
      <form className="LinkForm__form">
        <label className="LinkForm__label">
          <h2 className="LinkForm__subtitlte">Ваш электронный адрес</h2>
          <input
            className="LinkForm__input"
            required
            value={email.values}
            placeholder="введите ваш e-mail"
            name="email"
            type="email"
            pattern="^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
            onChange={handleChangeEmail}
          />
          <div
            className={`LinkForm__inputHidden ${
              errors.email ? "LinkForm__inputError" : ""
            }`}
          >
            {errors.email}
          </div>
        </label>
      </form>
      <button
        className={`LinkForm__button ${
          !isValid ? "Comment__button_disabled" : ""
        }`}
        disabled={!isValid}
        onClick={heandlerSubmit}
      >
        Отправить
      </button>
      <div className="LinkForm__inputHidden LinkForm__inputError"></div>
    </main>
  );
}

export default EmailLink;
