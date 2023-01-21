import React from "react";

export default function Navbar({ children }) {
  return (
    <header className="header">
      <img src={"images/hhlogo.png"} className="header--image" />
      <div id="nav-links">{children}</div>
    </header>
  );
}
