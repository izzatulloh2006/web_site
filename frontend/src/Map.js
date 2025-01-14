import React from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
    width: '100%',
    height: '400px'
};

const center = {
    lat: 55.751244,
    lng: 37.618423
};

const Map = () => {
    return (
        <LoadScript
            googleMapsApiKey="YOUR_GOOGLE_MAPS_API_KEY"
        >
            <GoogleMap
                mapContainerStyle={containerStyle}
                center={center}
                zoom={10}
            >
                <Marker position={center} />
            </GoogleMap>
        </LoadScript>
    );
}

export default Map;
