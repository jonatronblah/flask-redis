import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [gotData, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:1337/timeseries').then(res => res.json()).then(data => {
      setData(data);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">

        ... no changes in this part ...

        <ul>
            {JSON.stringify(gotData)}
        </ul>
      </header>
    </div>
  );
}

export default App;
