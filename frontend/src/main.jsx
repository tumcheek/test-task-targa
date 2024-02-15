import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './styles/index.scss';

const rootElement = document.getElementById('root');

ReactDOM
    .createRoot(rootElement)
    .render(<App />);
