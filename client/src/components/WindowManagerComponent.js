import React from 'react';
import useAnnotationModifier from '../StoreApi';
import ProjectSetup from './ProjectSetupComponent';
import WindowLayout from './WindowLayoutComponent';

const WindowManager = () => {
    const {currentWindow} = useAnnotationModifier();
    switch (currentWindow) {
        case "workspace": {
            return (
                <React.Fragment>
                    <WindowLayout />
                </React.Fragment>
            )
        }
        case "project_setup": {
            return (
                <React.Fragment>
                    <ProjectSetup />
                </React.Fragment>
            )
        }
        
    }
}

export default WindowManager;