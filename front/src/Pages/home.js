import { Link } from "react-router-dom";

import React from 'react'

const HomePage = () => {
  return (
    <div className='App'>
      <header>Links</header>
      <p>You are logged in</p><br/>
      <Link to="/about" className='Link'>About Us</Link><br/>
    </div>
  )
}

export default HomePage