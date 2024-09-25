import React from "react";
import { useState } from "react";
import Header from "./components/Header";
import Menu from "./components/Menu";
import Home from "./components/Home";
import Compositions from "./components/Compositions";
import Arrangements from "./components/Arrangements";
import Purchase from "./components/Purchase";
import Bio from "./components/Bio";
import Contact from "./components/Contact";
import stack from "/stack.png";

const App = () => {
  
  var [show_menu, setShowMenu] = useState(false);
  var [show_home, setShowHome] = useState(true);
  var [show_comps, setShowComps] = useState(false);
  var [show_arrs, setShowArrs] = useState(false);
  var [show_purch, setShowPurch] = useState(false);
  var [show_bio, setShowBio] = useState(false);
  var [show_contact, setShowContact] = useState(false);


  const showHome = () => {
    setShowMenu(show_menu = false);
    setShowHome(show_home = true);
    setShowComps(show_comps = false);
    setShowArrs(show_arrs = false);
    setShowPurch(show_purch = false);
    setShowBio(show_bio = false);
    setShowContact(show_contact = false);
  }
  
  const showCompositions = () => {
    setShowMenu(show_menu = false);
    setShowHome(show_home = false);
    setShowComps(show_comps = true);
    setShowArrs(show_arrs = false);
    setShowPurch(show_purch = false);
    setShowBio(show_bio = false);
    setShowContact(show_contact = false);
  }

  const showContact = () => {
    setShowMenu(show_menu = false);
    setShowHome(show_home = false);
    setShowComps(show_comps = false);
    setShowArrs(show_arrs = false);
    setShowPurch(show_purch = false);
    setShowBio(show_bio = false);
    setShowContact(show_contact = true);
  }



  return (
    <div>
      <Header />
      <input onClick={ () => setShowMenu( (currState) => !currState) } className="menubtn" type="image" name="menu" src={ stack } />
      <div>
        {show_menu && <Menu 
          showH={ () => showHome() }
          showComps={ () => showCompositions() }
          showCont={ () => showContact() }
         /> }
        {show_home && <Home /> }
        {show_comps && <Compositions /> }
        {show_arrs && <Arrangements /> }
        {show_purch && <Purchase /> }
        {show_bio && <Bio /> }
        {show_contact && <Contact /> }
      </div>
    </div>
  );
}

export default App
