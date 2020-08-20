// this components makes a new label for each annotation one makes
import React from 'react';
import { Label } from 'react-konva';

const getStyle = (color) => {

    return {
        backgroundColor: color,
        marginLeft : "0px",
        marginRight : "5px",
        border: "none",
        color: "black",
        padding: ["15px", "32px"],
        textAlign: "center",
        textDecoration: "none",
        display: "inline-block",
        fontSize: "16px",
    }
};

const AnnotationLabel = ({labels, getLabelId}) => {
    //console.log(annotationLabels.length)
    return (
        <div>
            {labels.map((label, idx) => {
                return (
                        <button
                            key={idx}
                            id={idx}
                            style={getStyle(label.color)}
                            onClick={(e) => getLabelId(e.target.id)}
                        >
                            {idx}: {label.label}
                        </button>    
                );
            })}
        </div>
    )
}

export default AnnotationLabel;