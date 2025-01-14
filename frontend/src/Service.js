import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Services = () => {
    const [services, setServices] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/v1/services/')
            .then(response => {
                setServices(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the services!', error);
            });
    }, []);

    return (
        <div>
            <h1>Our Services</h1>
            <ul>
                {services.map(service => (
                    <li key={service.id}>{service.title} - {service.price}</li>
                ))}
            </ul>
        </div>
    );
};

export default Services;
