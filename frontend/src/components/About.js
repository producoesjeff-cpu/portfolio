import React from 'react';
import { MapPin, Award, Users, Clock } from 'lucide-react';
import { usePortfolio } from '../hooks/usePortfolio';

const About = () => {
  const { data: portfolioData, loading } = usePortfolio();
  
  if (loading) {
    return (
      <section id="about" className="section-spacing-large" style={{ background: 'var(--darker-bg)' }}>
        <div className="container-gaffer">
          <div style={{ textAlign: 'center', padding: '4rem 0' }}>
            <p style={{ color: '#FFDB67', fontSize: '1.2rem' }}>Carregando informações...</p>
          </div>
        </div>
      </section>
    );
  }
  
  const { personal } = portfolioData || {};

  const stats = [
    {
      icon: <Clock size={24} />,
      number: "8+",
      label: "Anos de Experiência"
    },
    {
      icon: <Award size={24} />,
      number: "50+",
      label: "Produções Iluminadas"
    },
    {
      icon: <Users size={24} />,
      number: "6",
      label: "Clientes Premium"
    },
    {
      icon: <MapPin size={24} />,
      number: "2",
      label: "Cidades de Atuação"
    }
  ];

  return (
    <section id="about" className="section-spacing-large" style={{ 
      background: 'var(--darker-bg)',
      position: 'relative'
    }}>
      {/* Background pattern */}
      <div style={{
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23333' fill-opacity='0.1'%3E%3Ccircle cx='30' cy='30' r='1'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
        opacity: 0.3
      }}></div>

      <div className="container-gaffer" style={{ position: 'relative', zIndex: 1 }}>
        <div className="fade-in-up">
          <h2 className="section-title">Sobre Mim</h2>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
          gap: '3rem',
          alignItems: 'center',
          marginTop: '3rem'
        }}>
          {/* Foto e informações básicas */}
          <div className="fade-in-up stagger-1">
            <div style={{
              position: 'relative',
              borderRadius: '12px',
              overflow: 'hidden',
              aspectRatio: '4/5',
              maxWidth: '400px',
              margin: '0 auto'
            }}>
              <img
                src={personal.aboutImage}
                alt={personal.name}
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  filter: 'grayscale(20%) contrast(1.1)'
                }}
              />
              
              {/* Overlay gradiente */}
              <div style={{
                position: 'absolute',
                bottom: 0,
                left: 0,
                right: 0,
                height: '40%',
                background: 'linear-gradient(transparent, rgba(15, 15, 16, 0.9))',
                display: 'flex',
                alignItems: 'flex-end',
                padding: '2rem'
              }}>
                <div>
                  <h3 style={{
                    color: 'var(--primary-yellow)',
                    fontSize: '1.5rem',
                    fontWeight: '600',
                    marginBottom: '0.5rem'
                  }}>
                    {personal.name}
                  </h3>
                  <p style={{
                    color: 'var(--text-gray)',
                    fontSize: '1rem'
                  }}>
                    {personal.role}
                  </p>
                  <p style={{
                    color: 'var(--text-gray)',
                    fontSize: '0.9rem',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '0.5rem',
                    marginTop: '0.5rem'
                  }}>
                    <MapPin size={16} />
                    {personal.location}
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Texto e biografia */}
          <div className="fade-in-up stagger-2">
            <div>
              <h3 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '2rem',
                color: 'var(--text-white)',
                marginBottom: '1.5rem'
              }}>
                Transformando Conceitos em Luz
              </h3>
              
              <p className="body-large" style={{
                marginBottom: '2rem',
                textAlign: 'left'
              }}>
                {personal.bio}
              </p>

              <div style={{
                padding: '2rem',
                background: 'var(--card-bg)',
                borderRadius: '12px',
                border: '1px solid #333',
                marginBottom: '2rem'
              }}>
                <h4 style={{
                  color: 'var(--primary-yellow)',
                  fontSize: '1.2rem',
                  marginBottom: '1rem',
                  fontWeight: '600'
                }}>
                  Especialidades Técnicas
                </h4>
                
                <div style={{
                  display: 'grid',
                  gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                  gap: '1rem'
                }}>
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      • Setup de Iluminação
                    </p>
                    <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                      HMI, LED, Tungsten
                    </p>
                  </div>
                  
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      • Color Temperature
                    </p>
                    <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                      3200K - 6500K
                    </p>
                  </div>
                  
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      • Grip & Electric
                    </p>
                    <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                      Stands, Flags, Diffusion
                    </p>
                  </div>
                  
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      • Power Management
                    </p>
                    <p style={{ color: 'var(--text-gray)', fontSize: '0.9rem' }}>
                      Geradores, Distribuição
                    </p>
                  </div>
                </div>
              </div>

              {/* Estatísticas */}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(2, 1fr)',
                gap: '1rem'
              }}>
                {stats.map((stat, index) => (
                  <div
                    key={index}
                    style={{
                      background: 'var(--card-bg)',
                      padding: '1.5rem',
                      borderRadius: '8px',
                      textAlign: 'center',
                      border: '1px solid #333',
                      transition: 'all 0.3s ease'
                    }}
                    onMouseEnter={(e) => {
                      e.target.style.borderColor = 'var(--primary-yellow)';
                      e.target.style.boxShadow = 'var(--subtle-glow)';
                    }}
                    onMouseLeave={(e) => {
                      e.target.style.borderColor = '#333';
                      e.target.style.boxShadow = 'none';
                    }}
                  >
                    <div style={{
                      color: 'var(--primary-yellow)',
                      marginBottom: '0.5rem'
                    }}>
                      {stat.icon}
                    </div>
                    <h4 style={{
                      fontSize: '2rem',
                      fontWeight: '700',
                      color: 'var(--text-white)',
                      margin: '0.5rem 0'
                    }}>
                      {stat.number}
                    </h4>
                    <p style={{
                      color: 'var(--text-gray)',
                      fontSize: '0.9rem'
                    }}>
                      {stat.label}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;