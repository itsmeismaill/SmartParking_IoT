import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Authentification from './pages/Authentification';
import SignUp from './pages/SignUp';
import { ChakraProvider } from '@chakra-ui/react'
import Landing from './pages/Landing';
import HomeClient from './pages/HomeClient';


const App = () => {
  return (
    <ChakraProvider>

    <Router>
      <Routes>
        <Route path="/HomeClient" element={<HomeClient />} />
        <Route path="/Authentification" element={<Authentification />} />
        <Route path="/SignUp" element={<SignUp/>} />
        <Route path="/" element={<Landing/>} />
      </Routes>
    </Router>
    </ChakraProvider>
  );
}

export default App;
