import React, { useState } from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSubmit = async () => {
    const res = await fetch('http://localhost:8080/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(input)
    });
    const data = await res.text();
    setResponse(data);
  };

  return (
      <div className="App">
        <header className="App-header">
          <h1>Chat with AI</h1>
          <textarea value={input} onChange={handleInputChange} rows="4" cols="50" />
          <br />
          <button onClick={handleSubmit}>Send</button>
          <p>Please wait for the response. Since it is being generated on my local machine it may take it a couple minutes to arrive.</p>
          <p>Response:</p>
          <pre>{response}</pre>
        </header>
      </div>
  );
}

export default App;