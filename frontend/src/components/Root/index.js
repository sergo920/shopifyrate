import '../../style/index.css';
import '../../style/App.css';

import React, { Component } from 'react';
import FacebookButton from "../FacebookButton";

class Root extends Component {
    render() {
        return (
            <div className="App">
                <FacebookButton/>
            </div>
        );
    }
}

export default Root;