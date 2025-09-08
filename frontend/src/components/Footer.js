import React from 'react';
import { Mail, Phone, MapPin, Instagram, Linkedin, Youtube, MessageSquare, Heart } from 'lucide-react';
import { usePortfolio } from '../hooks/usePortfolio';

const Footer = () => {
  const { data: portfolioData, loading } = usePortfolio();
  
  if (loading) {
    return (
      <footer className="footer-cinematic">
        <div className="container-gaffer">
          <div style={{ textAlign: 'center', padding: '2rem 0' }}>
            <p style={{ color: '#FFDB67' }}>Carregando...</p>
          </div>
        </div>
      </footer>
    );
  }
  
  const { personal } = portfolioData || {};
  
  const currentYear = new Date().getFullYear();

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <footer className="footer-cinematic">
      <div className="container-gaffer">
        <div className="footer-content">
          {/* Informações principais */}
          <div>
            <h3 style={{
              fontFamily: 'var(--font-display)',
              fontSize: '1.5rem',
              color: 'var(--primary-yellow)',
              marginBottom: '1rem'
            }}>
              {personal.name}
            </h3>
            <p style={{
              color: 'var(--text-gray)',
              marginBottom: '1rem',
              fontSize: '0.9rem'
            }}>
              {personal.role}
            </p>
            <p style={{
              color: 'var(--text-gray)',
              fontSize: '0.9rem',
              lineHeight: '1.6',
              maxWidth: '300px'
            }}>
              Criando a iluminação perfeita para suas histórias em São Paulo e Rio de Janeiro.
            </p>
          </div>

          {/* Links de navegação */}
          <div>
            <h4 style={{
              color: 'var(--text-white)',
              marginBottom: '1rem',
              fontSize: '1.1rem'
            }}>
              Navegação
            </h4>
            <ul style={{
              listStyle: 'none',
              padding: 0,
              margin: 0
            }}>
              {[
                { label: 'Início', id: 'home' },
                { label: 'Portfólio', id: 'portfolio' },
                { label: 'Sobre', id: 'about' },
                { label: 'Serviços', id: 'services' },
                { label: 'Contato', id: 'contact' }
              ].map((item) => (
                <li key={item.id} style={{ marginBottom: '0.5rem' }}>
                  <button
                    onClick={() => scrollToSection(item.id)}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: 'var(--text-gray)',
                      cursor: 'pointer',
                      fontSize: '0.9rem',
                      padding: 0,
                      transition: 'color 0.3s ease'
                    }}
                    onMouseEnter={(e) => {
                      e.target.style.color = 'var(--primary-yellow)';
                    }}
                    onMouseLeave={(e) => {
                      e.target.style.color = 'var(--text-gray)';
                    }}
                  >
                    {item.label}
                  </button>
                </li>
              ))}
            </ul>
          </div>

          {/* Contato rápido */}
          <div>
            <h4 style={{
              color: 'var(--text-white)',
              marginBottom: '1rem',
              fontSize: '1.1rem'
            }}>
              Contato
            </h4>
            <div style={{ marginBottom: '1rem' }}>
              <a
                href={`mailto:${personal.email}`}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem',
                  color: 'var(--text-gray)',
                  textDecoration: 'none',
                  marginBottom: '0.5rem',
                  fontSize: '0.9rem',
                  transition: 'color 0.3s ease'
                }}
                onMouseEnter={(e) => {
                  e.target.style.color = 'var(--primary-yellow)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.color = 'var(--text-gray)';
                }}
              >
                <Mail size={16} />
                {personal.email}
              </a>
              
              <a
                href={`tel:${personal.phone}`}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '0.5rem',
                  color: 'var(--text-gray)',
                  textDecoration: 'none',
                  marginBottom: '0.5rem',
                  fontSize: '0.9rem',
                  transition: 'color 0.3s ease'
                }}
                onMouseEnter={(e) => {
                  e.target.style.color = 'var(--primary-yellow)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.color = 'var(--text-gray)';
                }}
              >
                <Phone size={16} />
                {personal.phone}
              </a>
              
              <div style={{
                display: 'flex',
                alignItems: 'center',
                gap: '0.5rem',
                color: 'var(--text-gray)',
                fontSize: '0.9rem'
              }}>
                <MapPin size={16} />
                {personal.location}
              </div>
            </div>
          </div>

          {/* Redes sociais */}
          <div>
            <h4 style={{
              color: 'var(--text-white)',
              marginBottom: '1rem',
              fontSize: '1.1rem'
            }}>
              Siga-me
            </h4>
            <div className="social-links">
              <a
                href={`https://instagram.com/${personal.social.instagram.replace('@', '')}`}
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
                title="Instagram"
              >
                <Instagram size={18} />
              </a>
              
              <a
                href={`https://linkedin.com/in/${personal.social.linkedin}`}
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
                title="LinkedIn"
              >
                <Linkedin size={18} />
              </a>
              
              <a
                href={`https://youtube.com/${personal.social.youtube}`}
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
                title="YouTube"
              >
                <Youtube size={18} />
              </a>
              
              <a
                href={`https://wa.me/${personal.social.whatsapp}`}
                target="_blank"
                rel="noopener noreferrer"
                className="social-link"
                title="WhatsApp"
              >
                <MessageSquare size={18} />
              </a>
            </div>

            <p style={{
              color: 'var(--text-gray)',
              fontSize: '0.8rem',
              marginTop: '1rem',
              lineHeight: '1.5'
            }}>
              Acompanhe meus trabalhos e bastidores das produções no Instagram e YouTube.
            </p>
          </div>
        </div>

        {/* Linha divisória */}
        <div style={{
          borderTop: '1px solid #333',
          marginTop: '2rem',
          paddingTop: '1.5rem',
          textAlign: 'center'
        }}>
          <p style={{
            color: 'var(--text-gray)',
            fontSize: '0.8rem',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '0.5rem',
            flexWrap: 'wrap'
          }}>
            © {currentYear} {personal.name}. Todos os direitos reservados.
            <span style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
              Feito com <Heart size={12} style={{ color: 'var(--primary-yellow)' }} /> para o cinema
            </span>
          </p>
          
          <p style={{
            color: 'var(--text-dark-gray)',
            fontSize: '0.7rem',
            marginTop: '0.5rem'
          }}>
            Portfólio profissional • Gaffer & Direção de Fotografia
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;