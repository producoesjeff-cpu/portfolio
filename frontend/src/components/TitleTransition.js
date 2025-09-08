import React, { useState, useEffect } from 'react';
import { usePortfolio } from '../hooks/usePortfolio';

const TitleTransition = () => {
  const { data: portfolioData, loading } = usePortfolio();
  const { personal } = portfolioData || {};
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY;
      const windowHeight = window.innerHeight;
      
      // Mostrar quando passar de 70% da primeira tela
      if (scrollPosition > windowHeight * 0.7) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Don't render if data is still loading or personal data is not available
  if (loading || !personal) {
    return null;
  }

  return (
    <section 
      className={`title-transition ${isVisible ? 'visible' : ''}`}
      style={{
        padding: '4rem 0',
        background: 'var(--dark-bg)',
        position: 'relative',
        overflow: 'hidden'
      }}
    >
      {/* Background pattern */}
      <div style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundImage: `url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%23FFDB67' fill-opacity='0.05'%3E%3Cpath d='M20 20c0 2.8-2.2 5-5 5s-5-2.2-5-5 2.2-5 5-5 5 2.2 5 5zm15 0c0 2.8-2.2 5-5 5s-5-2.2-5-5 2.2-5 5-5 5 2.2 5 5z'/%3E%3C/g%3E%3C/svg%3E")`,
        opacity: 0.3
      }}></div>

      <div className="container-gaffer" style={{ position: 'relative', zIndex: 1 }}>
        <div style={{ textAlign: 'center' }}>
          <h1 style={{
            fontFamily: 'var(--font-display)',
            fontSize: 'clamp(3rem, 8vw, 6rem)',
            fontWeight: '700',
            color: 'var(--text-white)',
            marginBottom: '1rem',
            textShadow: '2px 2px 4px rgba(0, 0, 0, 0.7)',
            lineHeight: '0.9'
          }}>
            Jeferson Rodrigues
          </h1>
          
          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '2rem',
            flexWrap: 'wrap',
            marginTop: '2rem'
          }}>
            <div style={{
              height: '2px',
              width: '60px',
              background: 'var(--primary-yellow)',
              opacity: 0.8
            }}></div>
            
            <p style={{
              fontFamily: 'var(--font-body)',
              fontSize: 'clamp(1.2rem, 3vw, 1.8rem)',
              fontWeight: '300',
              color: 'var(--primary-yellow)',
              letterSpacing: '3px',
              textTransform: 'uppercase',
              margin: 0
            }}>
              {personal?.role || 'Gaffer | Iluminação Audiovisual'}
            </p>
            
            <div style={{
              height: '2px',
              width: '60px',
              background: 'var(--primary-yellow)',
              opacity: 0.8
            }}></div>
          </div>

          <p style={{
            marginTop: '2rem',
            fontSize: 'clamp(1.1rem, 2.5vw, 1.4rem)',
            color: 'var(--text-gray)',
            maxWidth: '700px',
            margin: '2rem auto 0',
            lineHeight: '1.6'
          }}>
            Especialista em iluminação cinematográfica para grandes produções
          </p>
          
          <p style={{
            marginTop: '1rem',
            fontSize: '1.1rem',
            color: 'var(--primary-yellow)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '0.5rem'
          }}>
            📍 {personal.location}
          </p>
        </div>
      </div>
    </section>
  );
};

export default TitleTransition;