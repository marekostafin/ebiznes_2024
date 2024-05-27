import {useEffect, useState} from "react";

const Koszyk = ({ shoppingCartItems }) => {
    return (
        <div>
            <h2>Koszyk</h2>
            <ul>
                {shoppingCartItems.map(item => (
                    <li>
                        {item.valueOf()}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Koszyk;