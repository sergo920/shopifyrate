import axios from 'axios';
import React, { Component } from 'react';
import logo from '../../images/logo.svg';
import '../../style/index.css';
import '../../style/App.css';

class Root extends Component {
    componentWillMount() {
        axios.get('/shopify/products/')
            .then(function(response){
                console.log(response.data); // ex.: { user: 'Your User'}
                console.log(response.status); // ex.: 200
            });
    };


    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h2>Welcome to React</h2>
                </div>
                <p className="App-intro">
                    To get started, edit <code>src/App.js</code> and save to reload.
                </p>
            </div>
        );
    }
}

export default Root;