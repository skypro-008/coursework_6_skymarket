import React, { useState } from "react";
import useFormValidation from "../../utils/hooks/useFormValidation";

function CommentForm({addComment}) {
  const [text, setText] = useState("");
  const { values, handleChange, errors, isValid} = useFormValidation();

  function handleChangeInput(e) {
    handleChange(e);
    if (text.length > 0) {
      setText("");
    }
  }

  return (
    <form className="Comment__form" onSubmit={addComment}>
      <label className="Comment__label">
        <h2 className="Comment__form-title">Оставьте отзыв</h2>
        <textarea
          value={values.text}
          type="text"
          name="text"
          className="Comment__input"
          rows="5"
          minLength="8"
          maxLength="200"
          required="required"
          onChange={handleChangeInput}
        />
        <div
          className={`Comment__input-hidden ${
            errors.text ? "Comment__input-error" : ""
          }`}
        >
          {errors.text}
        </div>
      </label>
      <button
        className={`Comment__button Comment__button-text ${
          !isValid ? "Comment__button_disabled" : ""
        }`}
        disabled={!isValid}
        type="submit"
      >
        Отправить
      </button>
      <div className="Comment__input-error Comment__input-hidden"></div>
    </form>
  );
}

export default CommentForm;
