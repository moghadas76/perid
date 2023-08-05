import Button from "react-bootstrap/Button";
import React, {Component } from "react";

class Login extends Component {
    state = { 
        faild_attempts: 0
     }
    render() { 
        return ( 
            <form>
                <label htmlFor="">Email: <input type="email"/></label>
                <label htmlFor="">Password: <input type="password" /></label>
                <Button variant="primary">Login</Button>
            </form>
        );
    }
}
 
export default Login;