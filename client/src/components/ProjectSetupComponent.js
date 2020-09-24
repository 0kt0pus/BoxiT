import React, {useState} from 'react';
import useAnnotationModifier from '../StoreApi';
import { Container, Row, Col } from 'react-grid-system';

const button_submit = {
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

const header = {
    padding: "5px",
    textAlign: "center",
    background: "#474753",
    color: "white",
    fontSize: "30px",
};

const ProjectSetup = () => {
    // states to hold the setup data
    
    const [projectName, setProjectName] = useState("");
    const [projectDescription, setProjectDescription] = useState("");
    const [projectPath, setProjectPath] = useState("");
    // window setter
    const {setWindow} = useAnnotationModifier();

    const handleName = (e) => {
        setProjectName(e.target.value)
    }
    const handleDescription = (e) => {
        setProjectDescription(e.target.value)
    }
    const handlePath = (e) => {
        setProjectPath(e.target.value)
    }
    // on submit of the setup, submit to api endpoint
    // and set the new window
    const submitSetup = () => {
        const projectSetup = {
            name: projectName,
            description: projectDescription,
            path: projectPath,
        }
        // payload to the server
        const options = {
            method: "post",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(projectSetup)
        }
        // submit the payload
        //if (projectName && projectDescription && projectPath) {
        // send data to the server
        fetch("http://127.0.0.1:5000/api/create", options)
        // get the response from the server
        .then(res => {
            return res.json();
        })
        // catch any errors
        .catch(err => console.log(err))
        //}
        // if the form is empty
        //else {
        //    console.log("Setup is not valid")
        //}
        setWindow("workspace")
    }
    return (
        <div>
            <h1 style={header}>Project Setup</h1>
            <p>Please enter the image folder path</p>
            <div>
                <input type="text" onChange={handleName} placeholder="Project Name" required />
            </div>
            <div>
                <input type="text" onChange={handleDescription} placeholder="Project Description" required />
            </div>
            <div>
                <input type="text" onChange={handlePath} placeholder="Project Path" required />
            </div>
            <div>
                <button style={button_submit} onClick={submitSetup}>Submit</button>
            </div>
        </div>
    )
}

export default ProjectSetup;