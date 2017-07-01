import axios from 'axios';
import React, { Component } from 'react';
import logo from '../../images/logo.svg';
import '../../style/index.css';
import '../../style/App.css';
import 'react-image-gallery/styles/css/image-gallery.css';

import Images from '../Images';

class Root extends Component {
    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <h2>Welcome to React</h2>
                </div>

                <Images/>
            </div>
        );
    }
}

export default Root;