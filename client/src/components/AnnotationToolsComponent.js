import React from 'react';

const container = {

    width: "100%",
    margin: "0 auto",
    padding: "5px",
}

const button_box = {
    backgroundColor: "#ffa100",
    marginLeft : "0px",
    marginRight : "5px",
    border: "none",
    color: "white",
    padding: ["15px", "32px"],
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
};

const button_poly = {
    backgroundColor: "#0a00ff",
    marginRight : "5px",
    marginLeft : "5px",
    border: "none",
    color: "white",
    padding: ["15px", "32px"],
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
};

const button_delete = {
    backgroundColor: "#ff0025", 
    marginRight : "5px",
    marginLeft : "5px",
    border: "none",
    color: "white",
    padding: ["15px", "32px"],
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
};
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
                onClick={handleDelete}
                style={button_delete}
            >
                Delete
            </button>
        </div>
    );
}

export default AnnotationTools;