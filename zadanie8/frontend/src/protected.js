import React from 'react';
import axios from 'axios';
import {redirect, useNavigate} from "react-router-dom";

function Protected() {

    const navigate = useNavigate();
    const state = window.history.state;

    const handleLogout = async () => {
        try {
            await axios.get('http://localhost:3000/logout');
        } catch (err) {
            console.error('Error logging out:', err);
        }
    };

    if (!state || !state.fromLogin) {
        navigate('/login');
        return null;
    }

    return (
        <div>
            <h2>Protected</h2>
            <p>Welcome to your webapp!</p>
            <p>This can only be seen after logging in ;)</p>
            <button onClick={handleLogout}>Logout</button>
        </div>
    );
}

export default Protected;