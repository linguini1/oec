import React from "react";
import "./Form.css";
import { useEffect, useState } from "react";
import Select from "react-select";

export default function Form() {
  const [sex, setSex] = useState([]);
  const [symptoms, setSymptoms] = useState([]);
  const [underlying, setUnderlying] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/sex")
      .then((response) => response.json())

      .then((data) => {
        setSex(data);
      })
      .then((json) => console.log(json));
  }, []);

  useEffect(() => {
    fetch("http://localhost:8000/api/symptoms")
      .then((response) => response.json())

      .then((data) => setSymptoms(data))
      .then((json) => console.log(json));
  }, []);

  useEffect(() => {
    fetch("http://localhost:8000/api/underlying")
      .then((response) => response.json())

      .then((data) => setUnderlying(data))
      .then((json) => console.log(json));
  }, []);

  console.log(sex);
  const sex_options = sex.map((elem) => {
    <option value={elem}>{elem}</option>;
  });

  return (
    <div className="form">
      <h2>Patient Information</h2>
      <div className="form-fields">
        <input className="patient-field" placeholder="Name" />
        <input className="patient-field" placeholder="Age" type="number" />
        <select name="sex" id="sex">
          {sex_options}
        </select>
      </div>
    </div>
  );
}
