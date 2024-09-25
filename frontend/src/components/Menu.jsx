import React from "react";

const Menu = ({ showH, showComps, showCont }) => {
  return (
    <div className="menu">
      <ul>
        <button className="textbtn" onClick={ showH }> Home </button>
        <button className="textbtn" onClick={ showComps }> Compositions </button>
        <button className="textbtn"> Arrangements </button>
        <button className="textbtn"> Purchase Music </button>
        <button className="textbtn"> Bio </button>
        <button className="textbtn" onClick={ showCont }> Contact </button>
      </ul>
    </div>
  )
}

export default Menu
