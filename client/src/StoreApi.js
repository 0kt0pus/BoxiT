import { useStore } from './Store';

export const useAnnotationModifier = () => {
    const {state, dispatch} = useStore();
    // api object
    return {
        annotations: state.annotations,
        // dispatchers
        delete: (id) => dispatch({type: "delete_annotation", currentId: id}),
        add: (annotation) => dispatch({type: "add_annotation", newAnnotations: annotation}),
    }
};