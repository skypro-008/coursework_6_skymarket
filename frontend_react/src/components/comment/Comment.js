import React, { useState, useEffect, useContext } from "react";
import MainContext from "../../context/MainContext";
import AuthContext from "../../context/AuthContext";
import useAxios from "../../utils/useAxios";
import Buttons from "../buttons/Buttons";
import EditCommentPopup from "../editCommentPopup/EditCommentPopup";

function Comment(comment, { setComments }) {
  const [getComment, setGetComment] = useState({});
  const { handleEditCommPopupOpen, closePopup, isComPopupOpen } =
    useContext(MainContext);
  const { authTokens, user } = useContext(AuthContext);
  let api = useAxios();

  useEffect(() => {
    handleGetComment();
  }, [user]);

  const handleGetComment = async () => {
    const response = await api.get(
      `/ads/${comment.adId}/comments/${comment.commentId}/`
    );
    if (response.status === 200) {
      setGetComment(response.data);
    }
  };

  const editComment = async (e) => {
    e.preventDefault();
    let response = await fetch(
      `http://127.0.0.1:8000/ads/${comment.adId}/comments/${comment.commentId}/`,
      {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String(authTokens.access),
        },
        body: JSON.stringify({
          text: e.target.text.value,
        }),
      }
    );
    let data = await response.json();

    if (response.status === 200) {
      setGetComment(data);
      window.location.reload();
    } else if (response.statusText === "Unauthorized") {
      console.log("error!");
    }
  };

  const deleteComment = async () => {
    let response = await fetch(
      `http://127.0.0.1:8000/ads/${comment.adId}/comments/${comment.commentId}/`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + String(authTokens.access),
        },
      }
    );

    if (response.status === 204) {
      window.location.reload();
      setComments((comments) =>
        comments.filter((i) => i.id !== comment.commentId)
      );
    } else if (response.statusText === "Unauthorized") {
      console.log("error!");
    }
  };

  return (
    <>
      <li className="comment" key={comment.pk}>
        <p className="comment-text comment__author-text">
          {comment.authorName}
        </p>
        <div className="commentBox">
          <p className="comment-text comment-message">{comment.text}</p>
          {user.user_id === comment.userId ? (
            <Buttons
              className="comment-buttons"
              classButton="comment-button"
              onOpen={handleEditCommPopupOpen}
              onSubmit={deleteComment}
            />
          ) : null}
        </div>
      </li>
      <EditCommentPopup
        onClose={closePopup}
        isOpen={isComPopupOpen}
        getComment={getComment}
        text={getComment.text}
        id={comment.adId}
        editComment={editComment}
        setGetComment={setGetComment}
      />
    </>
  );
}

export default Comment;
