// this components makes a new label for each annotation one makes
import React from 'react';
import { Label } from 'react-konva';

const AnnotationLabel = ({labels, getLabelId}) => {
    //console.log(annotationLabels.length)
    return (
        <div>
            {labels.map((label, idx) => {
                return (
                        <button
                            key={idx}
                            id={idx}
                            onClick={(e) => getLabelId(e.target.id)}
                        >
                            {idx}: {label}
                        </button>    
                );
            })}
        </div>
    )
}

export default AnnotationLabel;