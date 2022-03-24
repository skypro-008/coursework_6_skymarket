import React, { useState, useEffect, useContext } from "react";
import useAxios from "../../utils/useAxios";
import AuthContext from "../../context/AuthContext";
import MainContext from "../../context/MainContext";
import Promo from "../promo/Promo";
//import SearchForm from "../searchForm/SearchForm";
import Cards from "../cards/Cards";
import { Pagination, PaginationItem } from "@mui/material";

function Main(props) {
  const [pageQty, setPageQty] = useState(0);
  const [adsDefault, setAdsDefault] = useState([]);
  //const [ad, setAd] = useState("");
  const [page, setPage] = useState(
    parseInt(props.location.search?.split("=")[1] || 1)
  );
  let { user } = useContext(AuthContext);
  let { ads, setAds } = useContext(MainContext);
  const BASE_URL_OPEN = "http://127.0.0.1:8000/ads/?";
  const BASE_URL = "/ads/?";
  let api = useAxios();

  useEffect(() => {
    user ? getAllAds() : getAds();
  }, [page, props.history]);

  const getAllAds = async () => {
    const response = await api.get(BASE_URL + `&page=${page}`);

    if (response.status === 200) {
      setAds(response.data.results);
      setPageQty(Math.round(response.data.count / 3.2));
      if (Math.round(response.data.count / 3.2) < page) {
        setPageQty(1);
        props.history.replace("/");
      } else if (response.status === 500) {
        console.log("На сервере произошел сбой");
      } else {
        console.log(response.status);
      }
    }
  };

  const getAds = async () => {
    const response = await fetch(BASE_URL_OPEN + `&page=${page}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setAdsDefault(data.results);
      setPageQty(Math.round(data.count / 3.2));
      if (Math.round(data.count / 3.2) < page) {
        setPage(1);
        props.history.replace("/");
      }
    } else if (response.status === 500) {
      console.log("На сервере произошел сбой");
    } else {
      console.log(response.status);
    }
  };

  const filteredAds = user ? ads : adsDefault;

  //function handleFilteredAds(ad) {
  //return filteredAds.filter((value) =>
  // value.title.toLowerCase().includes(ad.toLowerCase())
  //);
  //}

  return (
    <main className="Main">
      <Promo
        Pagination={Pagination}
        PaginationItem={PaginationItem}
        pageQty={pageQty}
        page={page}
        setPage={setPage}
      />
      <Cards ads={filteredAds} />
    </main>
  );
}

export default Main;
