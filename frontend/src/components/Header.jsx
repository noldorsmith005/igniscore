import React from "react";
import logo from "/logo.jpg";

const Header = () => {
  return (
    <div>
      <header className="head_container">
        <h1 className="title"> 
          Igniscore
        </h1>
        <img src={ logo } className="logo"/>
      </header>
    </div>
  )
}

export default Header
