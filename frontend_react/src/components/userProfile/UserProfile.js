import React, { useContext, useEffect, useState } from "react";
//import { NavLink } from "react-router-dom";
import MainContext from "../../context/MainContext";
import AuthContext from "../../context/AuthContext";
import Profile from "../profile/Profile";
import Cards from "../cards/Cards";
//import { Pagination, PaginationItem } from "@mui/material";
import useAxios from "../../utils/useAxios";

function UserProfile() {
  const { userAds, setUserAds } = useContext(MainContext);
  //const [pageQty, setPageQty] = useState(0);
  //const [page, setPage] = useState(
  //  parseInt(props.location.search?.split("=")[1] || 1)
  //);
  const [userInfo, setUserInfo] = useState({});
  const api = useAxios();
  const { user } = useContext(AuthContext);
  const BASE_URL = "/ads/me/?";

  useEffect(() => {
    getUsersAds();
  }, [user]);

  useEffect(() => {
    api
      .get("http://127.0.0.1:8000/users/me/")
      .then((result) => setUserInfo(result.data))
      .catch((error) => console.log("error", error));
  }, [user]);

  const getUsersAds = async () => {
    const response = await api.get(BASE_URL);

    if (response.status === 200) {
      setUserAds(response.data.results);
    }
  };

  return (
    <main className="userProfile">
      <Profile userInfo={userInfo} setUserInfo={setUserInfo} />
      <h2 className="userCards__title">Мои товары</h2>
      <Cards ads={userAds} />
    </main>
  );
}

export default UserProfile;
