//Import StrictMode to help catch potential problems during development
import { StrictMode } from "react";
//Import CreateRoot to attach the react app to the DOM
import { createRoot } from "react-dom/client";
//Main app component
import App from "./App";
//Global styles
import "./index.css"; 

//Create the react app inside the HTML elemet 'root'
createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
