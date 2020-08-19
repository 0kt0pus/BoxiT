import React, { useState } from "react";
import ImageCanvas from "./ImageCanvasComponent";
import AnnotationTools from "./AnnotationToolsComponent";
import AnnotationLabel from "./AnnotationLabelComponent";
import DrawAnnotations from "./DrawAnnotationsComponent";

// This components renders the selected components for a annotation job
const WorkSpace = ({getAnnotationLabels}) => {
    // State to hold the tool Id
    const [currentToolId, setCurrentToolId] = useState(null);
    const [validAnnotations, setValidAnnotations] = useState([]);
    const [currentSelectedId, setCurrentSelectedId] = useState(null);
    //const [validAnnotationLabels, setValidAnnotationLabels] = useState([]);
    const [currentLabelId, setCurrentLabelId] = useState(null);
    const [currentColor, setCurrentColor] = useState('black');
    //const [annotationLabels, setannotationLabels] = useState([]);
    // Here hold the ImageCanvas (default) and the selected
    // labeling components
    // for annotatio tools get tool id, this we
    // pass to the ImageCanvas to activate the tool
    const getToolId = (toolId) => {
        setCurrentToolId(toolId);
    };

    const getLabelsToDraw = (annotations) => {
        return annotations.slice().filter(anno => {
            return (anno.width > 0 && anno.height > 0);
                }).map(anno => {
                    return ({
                        id: anno.id,
                        label: labelsMap.labels[anno.id].label,
                        color: labelsMap.labels[anno.id].color,
                    });
                });
    }

    // get all the labels of the annotations
    const getAnnotations = (annotations) => {
        // Since every mouseUp creates an invalid (w:0, h:0) boxes, filter them
        // and get only the valid boxes
        setValidAnnotations(annotations);
        console.log(annotations)
        const validAnnotationLabelList = getLabelsToDraw(annotations);
        //console.log(validAnnotations)
        
        //setValidAnnotationLabels(validAnnotationLabelList);
        
        return getAnnotationLabels(validAnnotationLabelList);
        //console.log(validAnnotations);
    };
    
    // get the label id by click event
    const getLabelId = (labelId) => {
        setCurrentLabelId(labelId);
        setCurrentColor(labelsMap.labels[labelId].color);
    };
    // collect the label names
    const labels = labelsMap.labels.slice().map(label => {
        return label.label;
    });
    // get the annotations after a modification to the list like a deletion
    const getModifiedAnnotations = (modifiedAnnotations) => {
        //console.log(modifiedAnnotations)
        setValidAnnotations(modifiedAnnotations);
        console.log(currentToolId)
        console.log(currentLabelId)
        const validAnnotationLabelList = getLabelsToDraw(modifiedAnnotations);
        // update the dashboard
        return getAnnotationLabels(validAnnotationLabelList);
    }
    const getSelectedId = (shapeId) => {
        
        setCurrentSelectedId(shapeId);
        //console.log(currentSelectedId)
    };
    // Collect all the label Ids of the annotations
    // map to the label name and collect
    //const annotationLabels = validAnnotations.slice().map(anno => anno.id)
    //console.log(annotationLabels.length);
    return (
        <div>
            <p>Box!T</p>
            <ImageCanvas 
                toolId={currentToolId}
                labelId={currentLabelId}
                color={currentColor}
                getAnnotations={getAnnotations}
                getSelectedId={getSelectedId}
                validAnnotations={validAnnotations}
            />
            <AnnotationTools
                validAnnotations={validAnnotations}
                currentSelectedId={currentSelectedId}
                getToolId={getToolId}
                getModifiedAnnotations={getModifiedAnnotations}
            />
            <AnnotationLabel
                labels={labels}
                getLabelId={getLabelId}
            />
            
        </div>
    );
}

const labelsMap = {
    labels: [
        {
            label: "car",
            color: "red",
        },
        {
            label: "fence",
            color: "green",
        },
    ]
}

export default WorkSpace;

