import React, { useState, useEffect } from 'react';

const Header = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMobileMenuOpen(false);
    }
  };

  return (
    <header className={`header-cinematic ${isScrolled ? 'scrolled' : ''}`}>
      <div className="container-gaffer">
        <nav className="nav-cinematic">
          <a href="#home" className="logo-gaffer" onClick={(e) => {
            e.preventDefault();
            scrollToSection('home');
          }}>
            Jeferson Rodrigues
          </a>
          
          <ul className="nav-links">
            <li>
              <a href="#home" className="nav-link" onClick={(e) => {
                e.preventDefault();
                scrollToSection('home');
              }}>
                Início
              </a>
            </li>
            <li>
              <a href="#portfolio" className="nav-link" onClick={(e) => {
                e.preventDefault();
                scrollToSection('portfolio');
              }}>
                Portfólio
              </a>
            </li>
            <li>
              <a href="#about" className="nav-link" onClick={(e) => {
                e.preventDefault();
                scrollToSection('about');
              }}>
                Sobre
              </a>
            </li>
            <li>
              <a href="#services" className="nav-link" onClick={(e) => {
                e.preventDefault();
                scrollToSection('services');
              }}>
                Serviços
              </a>
            </li>
            <li>
              <a href="#contact" className="nav-link" onClick={(e) => {
                e.preventDefault();
                scrollToSection('contact');
              }}>
                Contato
              </a>
            </li>
          </ul>

          {/* Mobile menu button - implementar depois se necessário */}
          <button 
            className="mobile-menu-btn"
            style={{ display: 'none' }}
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            ☰
          </button>
        </nav>
      </div>
    </header>
  );
};

export default Header;