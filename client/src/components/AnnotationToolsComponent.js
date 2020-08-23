import React from 'react';
import useAnnotationModifier from '../StoreApi';

const container = {
    backgroundColor: "#7bc1c6",
    width: "100%",
    paddingTop: "5px",
    paddingBottom: "5px",
}

const button_box = {
    backgroundColor: "#d7e8f9",
    borderRadius: "8px",
    marginLeft : "34%",
    marginRight : "5px",
    border: "none",
    color: "black",
    padding: "10px 20px",
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
};

const button_poly = {
    backgroundColor: "#d7e8f9",
    borderRadius: "8px",
    marginRight : "5px",
    marginLeft : "5px",
    border: "none",
    color: "black",
    padding: "10px 20px",
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
};

const button_delete = {
    backgroundColor: "#f9d7d7", 
    borderRadius: "8px",
    marginRight : "25px",
    marginLeft : "5px",
    border: "none",
    color: "black",
    padding: "10px 20px",
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
};
const AnnotationTools = ({getToolId}) => {
    // Init contex reducer through store apis
    const {deleteAnnotations} = useAnnotationModifier();
    //const [toolId, setToolId] = useState(1);
    // When box is selected
    const handleBoxClick = (e) => {
        //setToolId(1);
        return getToolId(e.target.id);
    }
    /*
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
    */
    return (
        <div style={container}>
            <button 
                id="1" 
                onClick={handleBoxClick}
                style={button_box}
            >
                Box
            </button>
            <button 
                id="2" 
                onClick={handleBoxClick} 
                style={button_poly}
            >
                Poly
            </button>
            <button 
                onClick={deleteAnnotations}
                style={button_delete}
            >
                Delete
            </button>
        </div>
    );
}

export default AnnotationTools;