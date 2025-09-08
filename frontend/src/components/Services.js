import React from 'react';
import { Lightbulb, Camera, Settings, Palette } from 'lucide-react';
import { usePortfolio } from '../hooks/usePortfolio';

const Services = () => {
  const { services } = portfolioData;

  const getIcon = (iconName) => {
    const icons = {
      lightbulb: <Lightbulb size={32} />,
      camera: <Camera size={32} />,
      settings: <Settings size={32} />,
      palette: <Palette size={32} />
    };
    return icons[iconName] || <Lightbulb size={32} />;
  };

  return (
    <section id="services" className="section-spacing" style={{ 
      background: 'var(--dark-bg)',
      position: 'relative'
    }}>
      <div className="container-gaffer">
        <div className="fade-in-up">
          <h2 className="section-title">Serviços</h2>
          <p className="body-large" style={{ textAlign: 'center', marginBottom: '3rem' }}>
            Soluções completas em iluminação e produção audiovisual
          </p>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
          gap: '2rem',
          marginTop: '3rem'
        }}>
          {services.map((service, index) => (
            <div
              key={index}
              className={`fade-in-up stagger-${index + 1}`}
              style={{
                background: 'var(--card-bg)',
                padding: '2.5rem',
                borderRadius: '12px',
                border: '1px solid #333',
                transition: 'all 0.3s ease',
                textAlign: 'center'
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-10px)';
                e.currentTarget.style.borderColor = 'var(--primary-yellow)';
                e.currentTarget.style.boxShadow = 'var(--subtle-glow)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.borderColor = '#333';
                e.currentTarget.style.boxShadow = 'none';
              }}
            >
              <div style={{
                color: 'var(--primary-yellow)',
                marginBottom: '1.5rem'
              }}>
                {getIcon(service.icon)}
              </div>
              
              <h3 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.5rem',
                color: 'var(--text-white)',
                marginBottom: '1rem',
                fontWeight: '600'
              }}>
                {service.title}
              </h3>
              
              <p className="body-text" style={{
                color: 'var(--text-gray)',
                lineHeight: '1.6'
              }}>
                {service.description}
              </p>
            </div>
          ))}
        </div>

        {/* Seção adicional com processo de trabalho */}
        <div className="fade-in-up" style={{ 
          marginTop: '4rem',
          background: 'var(--darker-bg)',
          padding: '3rem',
          borderRadius: '12px',
          border: '1px solid #333'
        }}>
          <h3 style={{
            fontFamily: 'var(--font-display)',
            fontSize: '2rem',
            color: 'var(--primary-yellow)',
            textAlign: 'center',
            marginBottom: '2rem'
          }}>
            Processo de Trabalho
          </h3>
          
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '2rem'
          }}>
            <div style={{ textAlign: 'center' }}>
              <div style={{
                width: '60px',
                height: '60px',
                background: 'var(--primary-yellow)',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1rem',
                color: 'var(--dark-bg)',
                fontSize: '1.5rem',
                fontWeight: '700'
              }}>
                1
              </div>
              <h4 style={{
                color: 'var(--text-white)',
                marginBottom: '0.5rem',
                fontSize: '1.2rem'
              }}>
                Briefing & Planejamento
              </h4>
              <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                Análise do roteiro, locação e necessidades técnicas
              </p>
            </div>

            <div style={{ textAlign: 'center' }}>
              <div style={{
                width: '60px',
                height: '60px',
                background: 'var(--primary-yellow)',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1rem',
                color: 'var(--dark-bg)',
                fontSize: '1.5rem',
                fontWeight: '700'
              }}>
                2
              </div>
              <h4 style={{
                color: 'var(--text-white)',
                marginBottom: '0.5rem',
                fontSize: '1.2rem'
              }}>
                Setup & Teste
              </h4>
              <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                Montagem dos equipamentos e ajustes técnicos
              </p>
            </div>

            <div style={{ textAlign: 'center' }}>
              <div style={{
                width: '60px',
                height: '60px',
                background: 'var(--primary-yellow)',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1rem',
                color: 'var(--dark-bg)',
                fontSize: '1.5rem',
                fontWeight: '700'
              }}>
                3
              </div>
              <h4 style={{
                color: 'var(--text-white)',
                marginBottom: '0.5rem',
                fontSize: '1.2rem'
              }}>
                Execução
              </h4>
              <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                Direção de iluminação durante as gravações
              </p>
            </div>

            <div style={{ textAlign: 'center' }}>
              <div style={{
                width: '60px',
                height: '60px',
                background: 'var(--primary-yellow)',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1rem',
                color: 'var(--dark-bg)',
                fontSize: '1.5rem',
                fontWeight: '700'
              }}>
                4
              </div>
              <h4 style={{
                color: 'var(--text-white)',
                marginBottom: '0.5rem',
                fontSize: '1.2rem'
              }}>
                Finalização
              </h4>
              <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                Supervisão de color grading e entrega final
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Services;