import React from 'react';

const AnnotationTools = ({validAnnotations, currentSelectedId, getToolId, getModifiedAnnotations}) => {
    //const [toolId, setToolId] = useState(1);
    // When box is selected
    const handleBoxClick = (e) => {
        //setToolId(1);
        return getToolId(e.target.id);
    }
    // using the selectedId delete the annotation (set the param to zero, dont mutate the list)
    const handleDelete = () => {
        //console.log(selectedId);
        const annotations = validAnnotations
        const modifiedAnnotations = annotations.map((annotation, i) => {
            if (annotation.key === currentSelectedId) {
                const key = annotation.key
                const id = annotation.id
                annotation = {
                    x: 0,
                    y: 0,
                    width: 0,
                    height: 0,
                    key: key,
                    id: id,
                }
                return annotation;
            }
            return annotation;
        });
        //console.log(modifiedAnnotations)
        return getModifiedAnnotations(modifiedAnnotations);
    };

    return (
        <div>
            <button id="1" onClick={handleBoxClick}>Box</button>
            <button id="2" onClick={handleBoxClick} >Poly</button>
            <button onClick={handleDelete}>Delete</button>
        </div>
    );
}

export default AnnotationTools;