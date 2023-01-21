import React from "react";
import "./Form.css";
import { useEffect, useState } from "react";
import Dropdown from 'react-dropdown';

export default function Form(){

    const [options, setOptions] = useState(null);
    const [sex, setSex] = useState("");


    useEffect(() => {
        fetch('http://localhost:8000/api/sex')
        .then(response => response.json())
        .then( (data) => setOptions(data))
    }, []);

    console.log(options)



     //options = sex.map((sex) => (<div className="">{sex}</div>))

    //  const handleSelect = (e) => {
    //     console.log(e.target.value);
    //     setOptionValue(e.target.value);
    //   };

    return(
        <div className = "form-box">
        <label> Patient's Health Information</label>
        <input placeholder = "Name"/>
        <input placeholder = "Age" type = "number"/>

    
    
        </div>

    );

    
}