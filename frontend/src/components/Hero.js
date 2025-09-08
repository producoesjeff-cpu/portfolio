import React from 'react';
import { Play } from 'lucide-react';
import { usePortfolio } from '../hooks/usePortfolio';

const Hero = () => {
  const { data: portfolioData, loading } = usePortfolio();
  
  if (loading) {
    return (
      <section id="home" className="hero-fullscreen">
        <div className="demo-reel-fullscreen">
          <div className="demo-reel-placeholder-fullscreen">
            <div className="placeholder-content">
              <div style={{ 
                color: '#FFDB67', 
                fontSize: '1.2rem',
                textAlign: 'center' 
              }}>
                Carregando...
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }
  
  const { demoReel } = portfolioData || {};

  return (
    <section id="home" className="hero-fullscreen">
      {/* Demo Reel Fullscreen */}
      <div className="demo-reel-fullscreen">
        {demoReel.videoUrl ? (
          <iframe
            src={demoReel.videoUrl}
            title={demoReel.title}
            width="100%"
            height="100%"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
            style={{ 
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              objectFit: 'cover'
            }}
          ></iframe>
        ) : (
          <div className="demo-reel-placeholder-fullscreen">
            <div className="placeholder-content">
              <Play size={120} />
              <h2 style={{ 
                marginTop: '2rem', 
                color: '#FFDB67',
                fontSize: 'clamp(2rem, 5vw, 3rem)',
                fontFamily: 'var(--font-display)'
              }}>
                Demo Reel 2024
              </h2>
              <p style={{ 
                marginTop: '1rem',
                fontSize: 'clamp(1rem, 2.5vw, 1.3rem)',
                maxWidth: '600px',
                textAlign: 'center'
              }}>
                Principais trabalhos em iluminação cinematográfica
              </p>
              <p style={{ 
                fontSize: '1rem', 
                opacity: 0.8, 
                marginTop: '2rem',
                padding: '1rem 2rem',
                background: 'rgba(0,0,0,0.5)',
                borderRadius: '8px',
                border: '1px solid rgba(255, 219, 103, 0.3)'
              }}>
                Vídeo será adicionado em breve
              </p>
            </div>
          </div>
        )}
        
        {/* Overlay gradiente para legibilidade */}
        <div className="hero-overlay"></div>
      </div>

      {/* Scroll indicator */}
      <div className="scroll-indicator">
        <div className="scroll-arrow">
          <span></span>
          <span></span>
          <span></span>
        </div>
        <p style={{ 
          color: 'white', 
          fontSize: '0.9rem', 
          marginTop: '1rem',
          textShadow: '2px 2px 4px rgba(0,0,0,0.8)'
        }}>
          Role para conhecer o trabalho
        </p>
      </div>
    </section>
  );
};

export default Hero;