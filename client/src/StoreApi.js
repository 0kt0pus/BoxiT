import { useStore } from './Store';

const useAnnotationModifier = () => {
    const {state, dispatch} = useStore();
    // api object
    return {
        currentlabelMap: state.labelsMaps,
        currentSelectedId: state.selectedId,
        currentAnnotations: state.annotations,
        // dispatchers
        deleteAnnotations: () => dispatch({type: "delete_annotation"}),
        addAnnotations: (annotations) => dispatch({type: "add_annotation", newAnnotations: annotations}),
        selectAnnotation: (id) => dispatch({type: "select_annotation", currentId: id})
    }
};
export  default useAnnotationModifier;