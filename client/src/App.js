import React from 'react';
import './App.css';
import WindowLayout from './components/WindowLayoutComponent';
import { StoreProvider } from './Store';

function App() {
  return (
    <StoreProvider>
      <WindowLayout />
    </StoreProvider>
  );
}

export default App;

