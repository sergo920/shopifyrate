import axios from 'axios';
import React, { Component } from 'react';
import ImageGallery from 'react-image-gallery';

class Images extends Component {

    constructor(props) {
        super(props);
        this.state = {images: []};
    }

    componentWillMount() {
        axios.get('/shopify/products/')
            .then(function(response) {
                console.log(response.data.images);
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