import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom'; // Use Routes instead of Switch
import Home from './Home';
import About from './About';
import Form from './Form';
import './styles.css';
import Contact from './Contact'; // assuming you create a Contact.js file



function App() {
  return (
    <BrowserRouter>
      <div>
        <nav>
          <a href="/">Home</a> | <a href="/about">About</a> | <a href="/form">Form</a>
        </nav>

        <Routes>
          <Route path="/" element={<Home />} />  {/* Use element prop for route */}
          <Route path="/about" element={<About />} />
          <Route path="/form" element={<Form />} />
          
<Route path="/contact" component={Contact} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
