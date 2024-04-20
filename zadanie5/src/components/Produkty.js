import React, {useEffect, useState} from 'react';

const Produkty = ({ addToCart }) => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        fetch('http://localhost:1323/products')
            .then(response => response.json())
            .then(data => setProducts(data))
            .catch(error => console.error('Error fetching products:', error));
    }, []);

    const handleAddToCart = (product) => {
        addToCart(product);
    };

    return (
        <div>
            <h2>Products</h2>
            <ul>
                {products.map(product => (
                    <li>
                        {product.valueOf()}
                        <button onClick={() => handleAddToCart(product)}>Dodaj do koszyka</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Produkty;