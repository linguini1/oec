import './App.css';

//Pages 
import Home from "./pages/Home";
import Form from "./pages/Form";
import Map from "./pages/Map"; 

//Component
import { Routes, Route } from "react-router-dom";
import PageLink from "./components/nav/PageLink";
import Navbar from "./components/nav/Navbar";

function App() {
  return (
    <div id="App">
      <Navbar>
      <PageLink to="/">Home</PageLink>
        <PageLink to="/form">Form</PageLink>
        <PageLink to="/map">Map</PageLink>
      </Navbar>
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/form" element={<Form />}></Route>
        <Route path="/map" element={<Map />}></Route>
      </Routes>
    </div>
      
  );
}

export default App;
