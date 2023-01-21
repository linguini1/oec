import "./Map.css";

import React, {useEffect, useState} from 'react';


import { useMap } from 'react-leaflet/hooks'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import markerIconPng from "leaflet/dist/images/marker-icon.png";
import {Icon} from 'leaflet';

// const RecenterAutomatically = ({lat,lng}) => {
//     const map = useMap();
//      useEffect(() => {
//        map.setView([lat, lng]);
//      }, [lat, lng]);
//      return null;
// }

// const position = [51.505, -0.09]
// //Creates the map componenet 
// function MyComponent() {
//     const map = useMap()
//     console.log('map center:', map.getCenter());//console the lat & long
//     return null;
// }


export default function Map() {

    return(
        <p1></p1>

    );
    
    // return(
    //     <MapContainer center={position} zoom={13} >
    //           <MyComponent/>
    //             {<TileLayer
    //               attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    //               url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"/> }
    //             <Marker position={position} icon={new Icon({iconUrl: markerIconPng, iconSize: [25, 41], iconAnchor: [12, 41]})}>
    //                 <Popup>Location of the rocket 
    //                     Lat: {position[0]}  
    //                     Long: {position[1]} 
    //                 </Popup>
    //             </Marker>
    //             <RecenterAutomatically lat={position[0]} lng={position[1]}/>
    //     </MapContainer>
    //   );
        

}
