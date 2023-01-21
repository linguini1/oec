import React from "react";
import "./Form.css";
import { useEffect, useState } from "react";
import Dropdown from 'react-dropdown';

export default function Form(){

    const [sex, setSex] = useState([]);
    // const [options, setOptions] = useState(null);

    useEffect(() => {
        fetch('http://localhost:8000/api/sex')
        .then(response => response.json())
        
        .then( (data) => setSex(data))
        .then(json => console.log(json))
    }, []);

     //options = sex.map((sex) => (<div className="">{sex}</div>))

     const handleChange = (event) => {

        setSex(event.target.value);
     
    };
    return(
        <div className = "form-box">
        <label> Patient's Health Information</label>
        <input placeholder = "Name"/>
        <input placeholder = "Age" type = "number"/>
        <Dropdown
        label = "Sex"
        options = {sex}
        onChange= {handleChange}
        value = {sex[0]}

        />
    
    
        </div>

    );

    
}