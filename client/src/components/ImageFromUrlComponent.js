import React, { useState, useEffect } from "react";
import { Image } from "react-konva";

const ImageFromUrl = ({imageUrl, onDeselect, getStageDimensions}) => {
    const [image, setImage] = useState(null);
    // load the image using side effect
    useEffect(() => {
        // make an image window
        const image = new window.Image();
        image.src = imageUrl;
        // Load the image using an event listner
        image.addEventListener('load', () => {
            /*
            cv['onRuntimeInitialized']=()=>{
                
                try {
                    image = new cv.matFromImageData(image)
                } catch (err) {
                    console.log(cvTranslateError(cv, err))
                }
            };
            */
            setImage(image);
            return getStageDimensions({
                stageWidth: image.width,
                stageHeight: image.height,
            })
        })
        return () => image.removeEventListener('load');
        // imageUrl and setImage here means skip applying changes
        // if the value hasent changed. so if imageUrl and
        // setImage values havent changed, skip the effect
    }, [imageUrl, setImage]);
    
    return (
        <Image 
            onMouseDown={onDeselect} 
            image={image}
        />)
};

export default ImageFromUrl;