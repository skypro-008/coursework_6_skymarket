import React, { useState, createContext } from "react";
import useAxios from "../utils/useAxios";

const MainContext = createContext();

export default MainContext;

export const MainContextStates = ({ children }) => {
  const [ads, setAds] = useState([]);
  const [userAds, setUserAds] = useState([]);
  const [isEditPopupOpen, setIsEditPopupOpen] = useState(false);
  const [isComPopupOpen, setIsComPopupOpen] = useState(false);
  const api = useAxios();

  //Open/close navigation when page's size max-width 840px

  const handleOpenEditPopup = () => {
    setIsEditPopupOpen(true);
  };

  const handleEditCommPopupOpen = () => {
    setIsComPopupOpen(true);
  };

  const closePopup = () => {
    setIsComPopupOpen(false);
    setIsEditPopupOpen(false);
  };

  const getUsersAds = async () => {
    const response = await api.get("/ads/me/");

    if (response.status === 200) {
      setUserAds(response.data.results);
    }
  };

  const mainData = {
    ads: ads,
    userAds: userAds,
    setUserAds: setUserAds,
    setAds: setAds,
    getUsersAds: getUsersAds,
    isEditPopupOpen: isEditPopupOpen,
    isComPopupOpen: isComPopupOpen,
    handleOpenEditPopup: handleOpenEditPopup,
    handleEditCommPopupOpen: handleEditCommPopupOpen,
    closePopup: closePopup,
  };

  return (
    <MainContext.Provider value={mainData}>{children}</MainContext.Provider>
  );
};
