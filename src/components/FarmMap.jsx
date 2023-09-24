"use client";
import React, { useState, useEffect } from "react";
    import { MapContainer, TileLayer, Marker, Popup, Polyline} from "react-leaflet";
    import L from "leaflet";
    import "leaflet/dist/leaflet.css";

function FarmMap({ farmLocations, iconURL, setDelivery}) {
    const [midPoint, setMidPoint] = useState();
    
    useEffect(() => {
        if (farmLocations.length === 0) return;

        // Calculate the midpoint
        let latSum = 0;
        let lngSum = 0;

        farmLocations.forEach(location => {
            latSum += location.lat;
            lngSum += location.lng;
        });

        const midLat = latSum / farmLocations.length;
        const midLng = lngSum / farmLocations.length;

        setMidPoint({ lat: midLat, lng: midLng });
        console.log("midpoitn after set");
    },[]);

    const onDragEnd = (e) => {
        console.log("Dragged", e);
        const newLat = e.target.getLatLng().lat;
        const newLng = e.target.getLatLng().lng;
        console.log("calculating midpoint");
        setMidPoint({lat: newLat, lng: newLng });
        setDelivery([newLat, newLng]);
    };

    const customIcon = new L.Icon({
        iconUrl: iconURL,
        iconSize: [38, 95], // Customize this based on your icon size
    });

    return (
        <div style={{ display: "flex", justifyContent: "center", height: "50vh", width:"100%"}}>
        {console.log("midpoitn div")}
        {midPoint ? <MapContainer center = {midPoint} zoom={15} style={{ width: "80%", height: "400px" }}>
        
        <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {farmLocations.map((location, index) => (
            <Marker key={index} position={[location.lat, location.lng]} icon={customIcon}>
                <Popup>{`${location.name}\nLat: ${location.lat}\nLong: ${location.lng}`}</Popup>
                <Polyline positions={[[location.lat, location.lng], [midPoint.lat, midPoint.lng]]} color="blue" />
            </Marker>
        ))}
        {midPoint && (
            <Marker
                position={[midPoint.lat, midPoint.lng]}
                draggable={true}  
                eventHandlers={{
                    dragend: onDragEnd
                }}
            >         
                <Popup>Mid Point</Popup>
            </Marker>
        )}
        
    </MapContainer> : null }
    </div>
    );
}

export default FarmMap;