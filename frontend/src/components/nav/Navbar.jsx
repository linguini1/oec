import React from "react";
import "./Navbar.css";

export default function Navbar({ children }) {
  return (
    <nav>
      <img src={"images/hhlogo.png"} className="header--image" />
      <div id="nav-links">{children}</div>
    </nav>
  );
}
