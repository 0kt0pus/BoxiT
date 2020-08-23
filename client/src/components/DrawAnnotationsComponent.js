import React, {useState} from 'react';
import useAnnotationModifier from '../StoreApi';

const DrawAnnotations = ({validAnnotationLabels}) => {
    const {currentAnnotations, currentlabelMap} = useAnnotationModifier();
    console.log(currentAnnotations)
    return (
        <div>
            {currentAnnotations.slice().filter(anno => {
                return (anno.width > 0 && anno.height > 0);
            })
            .map((anno, idx) => {
                return(
                <p 
                    key={idx} 
                    style={
                        {
                            color: "black", 
                            background: anno.stroke,
                            textAlign: "center",
                        }}
                    > 
                        {anno.id}: {currentlabelMap[0].labels[anno.id].label}
                </p>
                )
            })
        }
        </div>
    );
};

export default DrawAnnotations;