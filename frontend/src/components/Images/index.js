import axios from 'axios';
import React, { Component } from 'react';
import ImageGallery from 'react-image-gallery';

class Images extends Component {

    getInitialState() {
        return {
            images: []
        };
    };

    componentWillMount() {
        axios.get('/shopify/products/')
            .then(function(response){
                this.setState({images: response.data.images});
            }.bind(this));
    };

    handleImageLoad(event) {
        console.log('Image loaded ', event.target)
    }

    render() {
        return (
            <ImageGallery
                items={this.state.images}
                slideInterval={2000}
                onImageLoad={this.handleImageLoad}/>
        );
    }

}

export default Images;