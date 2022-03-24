import React from "react";
import UserForm from "../userForm/UserForm";
import useFormValidation from "../../utils/hooks/useFormValidation";

function EditCommentPopup({
  isOpen,
  onClose,
  getComment,
  id,
  editComment,
  setGetComment,
  text,
}) {
  //const [text, setInput] = useState("");
  const { values, handleChange, errors, isValid } = useFormValidation();

  function handleChangeInput(e) {
    handleChange(e);
    if (getComment.length > 0) {
      setGetComment("");
    }
  }

  return (
    <div className={`popup editPopup ${isOpen ? "popup_is-opened" : ""}`}>
      <div className="popup__container-comment">
        <button
          onClick={onClose}
          className="close-button close-button_form"
        ></button>
        <UserForm
          id={id}
          onSubmit={editComment}
          title="Изменить"
          buttonText="Изменить"
          errors={!isValid}
          disabled={!isValid}
          className="userForm__title-comment
          userForm__title-important"
          paddingOf="userForm__title-comment
          userForm__title-important"
        >
          <label className="userForm__label userForm__label-comment">
            <h2 className="userForm__subtitle">Комментарий</h2>
            <input
              className="userForm__input"
              required
              value={values.getComment}
              placeholder={text}
              title="Название"
              name="text"
              type="text"
              minLength="3"
              maxLength="100"
              onChange={handleChangeInput}
            />
            <div
              className={`Form__input-hidden ${
                errors.getComment ? "Form__input-error" : ""
              }`}
            >
              {errors.getComment}
            </div>
          </label>
        </UserForm>
      </div>
    </div>
  );
}

export default EditCommentPopup;
