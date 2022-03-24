import React, { useState, useEffect, useContext } from "react";
import { useParams, useHistory } from "react-router-dom";
import useAxios from "../../utils/useAxios";
import AuthContext from "../../context/AuthContext";
import MainContext from "../../context/MainContext";
import CommentContainer from "../commentContainer/CommentContainer";
import EditPopup from "../editAdPopup/EditAdPopup";
import Buttons from "../buttons/Buttons";

function SinglePage() {
  const { id } = useParams();
  const [product, setProduct] = useState({});
  const [comments, setComments] = useState([]);
  const api = useAxios();
  let ad_pk = id;
  let { authTokens, user } = useContext(AuthContext);
  const { isEditPopupOpen, closePopup, setAds, handleOpenEditPopup } =
    useContext(MainContext);
  let history = useHistory();

  useEffect(() => {
    setTimeout(() => {
      Promise.all([getComments(), getProduct()]);
    }, 700);
  }, [user]);

  const getProduct = async () => {
    const response = await api.get(`/ads/${id}/`);

    if (response.status === 200) {
      setProduct(response.data);
    }
  };

  const getComments = async () => {
    const response = await api.get(`/ads/${ad_pk}/comments/`);

    if (response.status === 200) {
      setComments(response.data.results);
    }
  };

  const deleteAdd = async (e) => {
    e.preventDefault();
    const response = await fetch(`http://127.0.0.1:8000/ads/${id}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    if (response.status === 204) {
      setAds((ads) => ads.filter((ad) => ad.id !== product.id));
      history.push("/");
    } else if (response.statusText === "Unauthorized") {
      console.log("error!");
    }
  };

  const addComment = async (e) => {
    let response = await fetch(`http://127.0.0.1:8000/ads/${id}/comments/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
      body: JSON.stringify({
        text: e.target.text.value,
      }),
    });
    let newComment = await response.json();

    if (response.status === 201) {
      setComments([newComment, ...comments]);
      window.location.reload();
    } else if (response.statusText === "Unauthorized") {
      console.log("error!");
    }
  };
  return (
    <main className="cardInformation">
      {product && (
        <>
          <h1 className="cardInformation__title">{product.title}</h1>
          <div className="cardInformation__container">
            {user.user_id !== product.author_id ? null : (
              <Buttons
                user={user}
                product={product}
                onOpen={handleOpenEditPopup}
                className="buttons"
                classButton="buttons-item"
                onSubmit={deleteAdd}
              />
            )}
            {product.image === null ? (
              <div className="cardInformation__img-null" />
            ) : (
              <img
                src={product.image}
                className="cardInformation__img"
                alt="product img"
              />
            )}
            <div className="cardInformation__box">
              <p className="cardInformation__price">{product.price} &#8381;</p>

              <p className="cardInformation__description">
                {product.description}
              </p>
            </div>
            <div className="cardInformation__box box-2">
              <div className="cardInformation__box_second">
                <p className="cardInformation__tel">{product.phone}</p>
                <p className="cardInformation__tel">
                  {product.author_first_name}
                </p>
              </div>
            </div>
            <CommentContainer
              comments={comments}
              addComment={addComment}
              setComments={setComments}
              user={user}
            />
          </div>
          <EditPopup
            isEditPopupOpen={isEditPopupOpen}
            onClose={closePopup}
            id={id}
            product={product}
          />
        </>
      )}
    </main>
  );
}

export default SinglePage;
