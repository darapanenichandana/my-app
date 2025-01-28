import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter } from 'react-router-dom';  // Import BrowserRouter

const root = ReactDOM.createRoot(document.getElementById('root'));

// Wrap App with BrowserRouter for React Router to handle routing
root.render(
  <BrowserRouter>   
    <App />    {/* Your main App component */}
  </BrowserRouter>
);


