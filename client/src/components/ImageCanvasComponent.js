import React, { useState } from "react";
import ReactDOM from "react-dom";
import { Stage, Layer } from "react-konva";
import Rectangle from "./RectangleComponent";
import ImageFromUrl from "./ImageFromUrlComponent";

const ImageCanvas = ({toolId, labelId, color, getAnnotations, getSelectedId, validAnnotations}) => {
    //console.log(toolId)
    const [annotations, setAnnotations] = useState([]);
    const [newAnnotation, setNewAnnotation] = useState([]);
    const [selectedId, selectShape] = useState(null);
    const [stageDimensions, setStageDimensions] = useState({
      stageWidth: 900,
      stageHeight: 700,
    })

    const getEmptyBox = () => {
      const emptyBox = {
        x: 0,
        y: 0,
        width: 0,
        height: 0,
        key: "0",
        id: 0,
      }
      return emptyBox;
    };

    const checkDeselect = (e) => {
        // deselect when clicked on empty area
        const clickedOnEmpty = e.target === e.target.name;
        //console.log(e.target.getStage().children[0]._id)
        if (clickedOnEmpty) {
        selectShape(null);
        }
    };
  
    const handleMouseDown = event => {
        console.log("mousedwn")
        console.log(selectedId)
        // update the annotations state with the modified annotations
        setAnnotations(validAnnotations);
        if (selectedId == null) {
            if (newAnnotation.length === 0) {
                const { x, y } = event.target.getStage().getPointerPosition();
                let annotationToAdd = getEmptyBox();
                if (toolId === "1" && labelId !== null) {
                  annotationToAdd = { x, y, width: 0, height: 0, key: "0" };
                  setNewAnnotation([annotationToAdd]);
                }
            }      
        }
    };
  
    const handleMouseUp = event => {
      console.log("mousedwn")
        if (selectedId == null) {
            if (newAnnotation.length === 1) {
                const sx = newAnnotation[0].x;
                const sy = newAnnotation[0].y;
                const { x, y } = event.target.getStage().getPointerPosition();
                let annotationToAdd = getEmptyBox();
                if (toolId === "1" && labelId !== null) {
                  annotationToAdd = {
                    x: sx,
                    y: sy,
                    width: x - sx,
                    height: y - sy,
                    key: annotations.length + 1,
                    id: labelId,
                    fill:"transparent",
                    stroke:color,
                  };
                  annotations.push(annotationToAdd);
                  setNewAnnotation([]);
                  setAnnotations(annotations); 
                }
            }    
        }
        return getAnnotations(annotations);
    };
  
    const handleMouseMove = event => {
        if (selectedId == null) {
            if (newAnnotation.length === 1) {
                const sx = newAnnotation[0].x;
                const sy = newAnnotation[0].y;
                const { x, y } = event.target.getStage().getPointerPosition();
                let annotationToAdd = getEmptyBox();
                if (toolId === "1" && labelId !== null) {
                  annotationToAdd = {
                    x: sx,
                    y: sy,
                    width: x - sx,
                    height: y - sy,
                    key: "0",
                    fill:"transparent",
                    stroke:color,
                  }
                }
                setNewAnnotation([
                    annotationToAdd
                ]);
            }
        }
    };

    const getStageDimensions = (stageDims) => {
      setStageDimensions(stageDims)
    }

    const annotationsToDraw = [...validAnnotations, ...newAnnotation];
    
    //console.log(validAnnotations)
    return (
      <Stage
        onMouseDown={handleMouseDown}
        onMouseUp={handleMouseUp}
        onMouseMove={handleMouseMove}
        width={stageDimensions.stageWidth}
        height={stageDimensions.stageHeight}
      >
        <Layer>
          <ImageFromUrl
            onDeselect={() => selectShape(null)}
            getStageDimensions={getStageDimensions}
            imageUrl="https://storage.googleapis.com/afs-prod/media/afs:Medium:8059513008/1024.png"
          />
        </Layer>
        <Layer>
          {annotationsToDraw.map((annotation, i) => {
            return (
                <Rectangle
                key={i}
                shapeProps={annotation}
                isSelected={annotation.key === selectedId}
                onSelect={() => {
                    console.log("Select")
                  selectShape(annotation.key);
                  return getSelectedId(annotation.key);
                }}
                onChange={(newAttrs) => {
                  const annotations = annotationsToDraw.slice();
                  annotations[i] = newAttrs;
                  setAnnotations(annotations);
                }}
                />
            );
          })}
        </Layer>
      </Stage>
    );
  };

export default ImageCanvas;

/**
 * <Rect
                x={value.x}
                y={value.y}
                width={value.width}
                height={value.height}
                fill="transparent"
                stroke="black"
                draggable={true}
              />
 */