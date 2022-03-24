import React from "react";
import {useLocation} from "react-router-dom";


function UserForm(props) {
  let location = useLocation().pathname

  return (
    <div className={location === "/profile" ? "userForm-profile" : location === `/ads/${props.id}` ? "userForm-editPopup" :"userForm"}>
      <h1 className={`userForm__title ${props.className}`}>
        {props.title}<span className="userForm__margin">{props.userName}</span>
      </h1>
      <form name="form-data" className="userForm__form" onSubmit={props.onSubmit}>
        {props.children}
        <button
          type="submit"
          className={`userForm__button userForm__button-text ${props.paddingOf} ${
          props.errors ? "userForm__button_disabled" : null
          }`}
          disabled={props.disabled}
        >
          {props.buttonText}
        </button>
      </form>
    </div>
  );
}

export default UserForm;
