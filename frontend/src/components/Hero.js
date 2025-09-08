import React from 'react';
import { Play } from 'lucide-react';
import { portfolioData } from '../data/mock';

const Hero = () => {
  const { personal, demoReel } = portfolioData;

  const scrollToPortfolio = () => {
    const element = document.getElementById('portfolio');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const scrollToContact = () => {
    const element = document.getElementById('contact');
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section id="home" className="hero-cinematic">
      <div className="hero-background"></div>
      <div className="hero-spotlight"></div>
      
      <div className="container-gaffer">
        <div className="hero-content">
          <div className="fade-in-up">
            <h1 className="hero-title">{personal.name}</h1>
          </div>
          
          <div className="fade-in-up stagger-1">
            <p className="gaffer-role">{personal.role}</p>
          </div>
          
          <div className="fade-in-up stagger-2" style={{ marginTop: '2rem' }}>
            <p className="body-large">
              Especialista em iluminação cinematográfica para grandes produções
            </p>
          </div>
          
          <div className="fade-in-up stagger-3" style={{ marginTop: '1rem' }}>
            <p className="body-text" style={{ textAlign: 'center', color: '#FFDB67' }}>
              📍 {personal.location}
            </p>
          </div>

          {/* Demo Reel Section */}
          <div className="fade-in-up stagger-4" style={{ marginTop: '3rem' }}>
            <div className="demo-reel-container">
              {demoReel.videoUrl ? (
                <iframe
                  src={demoReel.videoUrl}
                  title={demoReel.title}
                  width="100%"
                  height="100%"
                  frameBorder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              ) : (
                <div className="demo-reel-placeholder">
                  <Play size={80} />
                  <h3 style={{ marginTop: '1rem', color: '#FFDB67' }}>Demo Reel 2024</h3>
                  <p style={{ marginTop: '0.5rem' }}>
                    Principais trabalhos em iluminação cinematográfica
                  </p>
                  <p style={{ fontSize: '0.8rem', opacity: 0.7, marginTop: '1rem' }}>
                    Vídeo será adicionado em breve
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Action Buttons */}
          <div className="fade-in-up stagger-4" style={{ 
            marginTop: '3rem', 
            display: 'flex', 
            gap: '1rem', 
            justifyContent: 'center',
            flexWrap: 'wrap'
          }}>
            <button 
              onClick={scrollToPortfolio}
              className="btn-cinematic btn-primary"
            >
              Ver Portfólio
            </button>
            <button 
              onClick={scrollToContact}
              className="btn-cinematic"
            >
              Entrar em Contato
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;