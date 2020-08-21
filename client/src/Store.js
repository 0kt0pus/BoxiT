import React, {createContext, useContext, useReducer} from 'react';

// Make a store context
const StoreContext = createContext();
const initialState = {toolId: null};

const reducer = (state, action) => {
    switch(action.type) {
        case "delete_annotation":
            return {
                annotations: state.annotations.map((annotation, i) => {
                    if (annotation.key === action.currentId) {
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
                }),
            }
        case "add_annotation":
            return {
                annotations: state.annotations.push(action.newAnnotations),
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