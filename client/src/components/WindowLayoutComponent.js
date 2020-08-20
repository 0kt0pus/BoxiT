import React, {useState} from 'react';
import WorkSpace from './WorkSpaceComponent';
import Dashboard from './DashboardComponent';
import { Container, Row, Col } from 'react-grid-system';

const divStyle = {
    margin: '40px',
    border: '5px solid pink'
};
  
const rightPannel = {
    position: "relative",
};
  
const leftPannel = {
    width: "200px",
    padding: "10px",
};
  
const header = {
    padding: "5px",
    textAlign: "center",
    background: "#474753",
    color: "white",
    fontSize: "30px",
  };

const WindowLayout = () => {
    const [annotationLabels, setAnnotationLabels] = useState([]);
    
    return(
        <div>
             <h1 style={header}>Box!T</h1>
       <Row>
           <Col sm={2}>
                <div style={leftPannel}>
                    <Dashboard
                        validAnnotationLabels={annotationLabels}
                    />
                </div>
           </Col>
           <Col sm={4}>
                <div style={rightPannel}>
                    <WorkSpace 
                        getAnnotationLabels={(annoLables) => setAnnotationLabels(annoLables)}
                    />
                </div>
           </Col>
       </Row> 
       </div>
    );
};

export default WindowLayout;

/**
 * <div>
            <div style={leftPannel}>
                <Dashboard />
            </div>
            <div style={rightPannel}>
                <WorkSpace />
            </div>
        </div>
 */