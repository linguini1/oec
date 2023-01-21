import React from "react";

export default function Navbar({ children }) {
  return (
    <nav className="my_nav">
    <header className = "header">
      <img style={{ width: 200, height: 200 }} src={("images/hhlogo.png")} />
      <div id="nav-links">{children}</div>
    </header>
      
    </nav>
  );
}