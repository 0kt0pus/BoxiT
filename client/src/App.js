import React from 'react';
import './App.css';
//import WindowLayout from './components/WindowLayoutComponent';
import WindowManager from './components/WindowManagerComponent';
import { StoreProvider } from './Store';

function App() {
  return (
    <StoreProvider>
      <WindowManager />
    </StoreProvider>
  );
}

export default App;

