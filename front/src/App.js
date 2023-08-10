import './App.css';
import React  from "react";
import Login  from "./Pages/login";
import AboutPage  from "./Pages/about";
import HomePage  from "./Pages/home";
import Main  from "./Pages/main";
import unauthorizedPage  from "./Pages/unauthorized";
import {AuthProvider}  from "./Context/authProvider";
import {Route, Routes } from 'react-router-dom';
import { RouterProvider } from 'react-router-dom';


function App() {
  return (
    // <div className="App">
      
    // </div>
    <AuthProvider>
    
      <Routes>
          <Route path='/' element={<Main/>} />
          <Route path='/home' element={<HomePage/>}/>
          <Route path='/login' element={<Login/>}/>
          <Route path='/unauthorized' element={<unauthorizedPage/>}/>
          <Route path='*' element={<AboutPage/>}/>
      </Routes>
      
    </AuthProvider>
  );
}

export default App;
