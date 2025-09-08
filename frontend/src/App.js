import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

// Importar componentes
import Header from "./components/Header";
import Hero from "./components/Hero";
import TitleTransition from "./components/TitleTransition";
import Portfolio from "./components/Portfolio";
import About from "./components/About";
import Services from "./components/Services";
import Clients from "./components/Clients";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import { Toaster } from "./components/ui/toaster";

// Importar estilos
import "./styles/gaffer.css";

const GafferPortfolio = () => {
  return (
    <div style={{ 
      background: 'var(--dark-bg)', 
      minHeight: '100vh',
      color: 'var(--text-white)'
    }}>
      <Header />
      <Hero />
      <TitleTransition />
      <Portfolio />
      <About />
      <Services />
      <Clients />
      <Contact />
      <Footer />
      <Toaster />
    </div>
  );
};

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<GafferPortfolio />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
