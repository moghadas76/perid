import React from 'react'
import { Link } from 'react-router-dom'

const Main = () => {
  return (
    <div className="App">
      <h1>Welcome Main, what would you like to do</h1>
      <Link to='/login'>Signin</Link><br/>
    </div>
  )
}

export default Main