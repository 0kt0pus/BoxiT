import React from 'react';
import DrawAnnotations from './DrawAnnotationsComponent';

const header = {
    padding: "5px",
    textAlign: "center",
    background: "#686baa",
    color: "black",
    fontSize: "15px",
  };

const Dashboard = ({validAnnotationLabels}) => {
    return (
        <div>
            <h3 style={header}>Label Monitor</h3>
            <DrawAnnotations
                validAnnotationLabels={validAnnotationLabels}
            />
        </div>
    );
}

export default Dashboard