import React, {useState} from 'react';

const DrawAnnotations = ({validAnnotationLabels}) => {
    
    return (
        <div>
            {validAnnotationLabels.map((anno, idx) => {
                return(
                <p key={idx} style={{color: "white", background: anno.color}}> {anno.id}: {anno.label}</p>
                )
            })
        }
        </div>
    );
};

export default DrawAnnotations;