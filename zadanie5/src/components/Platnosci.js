import React, {useState} from 'react';

const Platnosci = () => {
    const [paymentData, setPaymentData] = useState({
        amount: '',
        cardNumber: '',
        expiryDate: '',
        cvv: ''
    });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setPaymentData({ ...paymentData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        let formData = new FormData();
        formData.append('product', paymentData.amount);

        fetch('http://localhost:1323/products', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => console.log('Payment successful:', data))
            .catch(error => console.error('Error making payment:', error));
    };

    return (
        <div>
            <h2>Payments</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Kwota:
                    <input type="text" name="amount" value={paymentData.amount} onChange={handleInputChange} />
                </label>
                <button type="submit">Pay</button>
            </form>
        </div>
    );
};

export default Platnosci;