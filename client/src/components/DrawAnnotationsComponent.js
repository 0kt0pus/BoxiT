import React, {useState} from 'react';

const DrawAnnotations = ({validAnnotationLabels}) => {
    
    return (
        <div>
            {validAnnotationLabels.map((anno, idx) => {
                return(
                <p 
                    key={idx} 
                    style={
                        {
                            color: "black", 
                            background: anno.color,
                            textAlign: "center",
                        }}
                    > 
                        {anno.id}: {anno.label}
                </p>
                )
            })
        }
        </div>
    );
};

export default DrawAnnotations;