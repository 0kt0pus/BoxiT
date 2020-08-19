import React from 'react';
import DrawAnnotations from './DrawAnnotationsComponent';

const Dashboard = ({validAnnotationLabels}) => {
    return (
        <div>
            <p>I am a Dashboard</p>
            <DrawAnnotations
                validAnnotationLabels={validAnnotationLabels}
            />
        </div>
    );
}

export default Dashboard