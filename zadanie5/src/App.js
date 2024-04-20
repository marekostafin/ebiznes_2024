import './App.css';
import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Link, Route, Routes } from "react-router-dom";
import Produkty from './components/Produkty';
import Platnosci from './components/Platnosci';
import Koszyk from './components/Koszyk';



function App() {
    const [cartItems, setCartItems] = useState([]);

    const addToCart = (product) => {
        setCartItems([...cartItems, product]);
    };

    return (
        <Router>
            <div>
                <nav>
                    <Link to="/produkty">Produkty</Link>
                    <br/>
                    <Link to="/platnosci">Płatności</Link>
                    <br/>
                    <Link to="/koszyk">Koszyk</Link>
                </nav>
                <Routes>
                    <Route path="/produkty" element={<Produkty addToCart={addToCart} />} />
                    <Route path="/platnosci" element={<Platnosci/>} />
                    <Route path="/koszyk" element={<Koszyk shoppingCartItems={cartItems}/>} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
