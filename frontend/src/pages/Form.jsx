import React from "react";
import "./Form.css";
import { useEffect, useState } from "react";


export default function Form() {
  const [age, setAge] = useState();
  const [sex, setSex] = useState();
  const [symptoms, setSymptoms] = useState();
  const [underlying, setUnderlying] = useState();
  const [location, setLocation] = useState();
  const [latitude, setLatitude] = useState();
  const[longitude, setLongitude] = useState();

  //Gecode 
  

  const handleSubmit = (e) => {

    
    e.preventDefault();
    
    fetch('http://localhost:8000/api', {
      method: 'POST', 
      mode: 'cors', 
      body: JSON.stringify({
        age:age,
        sex: sex,
        underlying: underlying,
        symptoms: symptoms, 
        latitude: latitude,
        longitude: longitude
      })

    })

}


  return (
    <form className="form" onSubmit={handleSubmit}>
      <h2>Patient Information</h2>
      <div className="form-fields">
        <input className="patient-field" placeholder="Name" type="text" 
        />
        <input className="patient-field" placeholder="Age" type="number" min="1" max="130"
        onChange={(e) => setAge(e.target.value)} />
        <input className = "patient-field" placeholder = "Sex" type="text"
        onChange={(e) => setSex(e.target.value)}/>
        <input className="patient-field" placeholder="Underlying Conditions" type= "text"
        onChange={(e) => setUnderlying(e.target.value)}/>
        <input className="patient-field" placeholder="Symptoms" type= "text"
        onChange={(e) => setSymptoms(e.target.value)}/>
        <input className="patient-field" placeholder="Location " type= "text"
        onChange={(e) => setLocation(e.target.value)}/>
        <button className = "form-button"type="submit">Submit Form</button>

      </div>
    </form>
  );
}
