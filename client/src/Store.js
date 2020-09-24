import React, {createContext, useContext, useReducer} from 'react';

// Make a store context
const StoreContext = createContext();
const initialState = {
    window: "project_setup",
    labelsMaps: [{
        labels: [
            {
                label: "car",
                color: "#0bd8f1",
            },
            {
                label: "fence",
                color: "#38cc19",
            },
        ]
    }],
    selectedId: null,
    annotations: []
};
//console.log(initialState)
const reducer = (state, action) => {
    switch(action.type) {
        case "delete_annotation":
            return {
                window: state.window,
                labelsMaps: state.labelsMaps,
                selectedId: state.selectedId,
                annotations: state.annotations.map((annotation, i) => {
                    if (annotation.key === state.selectedId) {
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
                }).filter(anno => {
                    return (anno.width > 0 && anno.height > 0)
                  }),
            }
        case "add_annotation":
            return {
                window: state.window,
                labelsMaps: state.labelsMaps,
                selectedId: state.selectedId,
                annotations: action.newAnnotations,
            }
        case "select_annotation":
            return {
                window: state.window,
                labelsMaps: state.labelsMaps,
                selectedId: action.currentId,
                annotations: state.annotations,
            }
        case "set_window":
            return {
                window: action.currentWindow,
                labelsMaps: state.labelsMaps,
                selectedId: state.currentId,
                annotations: state.annotations,
            }
        default:
            throw new Error(`Unhandled action type: ${action.type}`);
        }    
    };

export const StoreProvider = ({ children }) => {
    const [state, dispatch] = useReducer(reducer, initialState);
    
    return (
        <StoreContext.Provider value={{state, dispatch}}>
        {children}
        </StoreContext.Provider>
    );
}
      
export const useStore = () => useContext(StoreContext);