// this components makes a new label for each annotation one makes
import React from 'react';
import { Label } from 'react-konva';

const container = {
    backgroundColor: "#e2e2e2",
    width: "100%",
    paddingTop: "5px",
    paddingBottom: "5px",
}

const getStyle = (color) => {

    return {
        backgroundColor: color,
        borderRadius: "8px",
        marginLeft : "5px",
        marginRight : "5px",
        border: "none",
        color: "black",
        padding: "8px 25px",
        textAlign: "center",
        textDecoration: "none",
        display: "inline-block",
        fontSize: "20px",
    }
};

const AnnotationLabel = ({labels, getLabelId}) => {
    //console.log(annotationLabels.length)
    return (
        <div style={container}>
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