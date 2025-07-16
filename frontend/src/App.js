import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const askAI = async () => {
    const res = await fetch('http://localhost:3000/ask', {
      method : 'POST',
      headers : {
        'Content-Type' : 'application/json',
      },
      body : JSON.stringify({ question }),
    });
    const data = await res.json();
    setResponse(data.answer);
  }
  return (
    <div className='App'>
      <h1>AI Legal Assistant</h1>
      <input
      type='text'
      value={question}
      onChange={(event) => setQuestion(event.target.value)}
      placeholder='Ask a legal question'
      />
      <button onClick={askAI}>Submit</button>
      <p>{response}</p>
    </div>
  )
}

export default App;
