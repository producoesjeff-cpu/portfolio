import React, { useState } from 'react';
import { Mail, Phone, MapPin, Instagram, Linkedin, Youtube, MessageSquare } from 'lucide-react';
import { usePortfolio } from '../hooks/usePortfolio';
import { sendContactMessage } from '../data/mock';
import { useToast } from '../hooks/use-toast';

const Contact = () => {
  const { data: portfolioData, loading } = usePortfolio();
  const { toast } = useToast();
  
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  });
  
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);

    // Simulação de envio (será implementado com EmailJS depois)
    try {
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      toast({
        title: "Mensagem enviada!",
        description: "Entrarei em contato em breve. Obrigado!",
      });
      
      setFormData({
        name: '',
        email: '',
        phone: '',
        subject: '',
        message: ''
      });
    } catch (error) {
      toast({
        title: "Erro ao enviar",
        description: "Tente novamente ou entre em contato diretamente.",
        variant: "destructive"
      });
    } finally {
      setIsSubmitting(false);
    }
  };

  const socialLinks = [
    {
      name: 'Instagram',
      icon: <Instagram size={20} />,
      url: `https://instagram.com/${personal.social.instagram.replace('@', '')}`,
      handle: personal.social.instagram
    },
    {
      name: 'LinkedIn',
      icon: <Linkedin size={20} />,
      url: `https://linkedin.com/in/${personal.social.linkedin}`,
      handle: personal.social.linkedin
    },
    {
      name: 'YouTube',
      icon: <Youtube size={20} />,
      url: `https://youtube.com/${personal.social.youtube}`,
      handle: personal.social.youtube
    },
    {
      name: 'WhatsApp',
      icon: <MessageSquare size={20} />,
      url: `https://wa.me/${personal.social.whatsapp}`,
      handle: personal.phone
    }
  ];

  return (
    <section id="contact" className="section-spacing-large" style={{ 
      background: 'var(--darker-bg)' 
    }}>
      <div className="container-gaffer">
        <div className="fade-in-up">
          <h2 className="section-title">Entre em Contato</h2>
          <p className="body-large" style={{ textAlign: 'center', marginBottom: '3rem' }}>
            Vamos discutir seu projeto e criar a iluminação perfeita
          </p>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))',
          gap: '3rem',
          alignItems: 'start'
        }}>
          {/* Informações de contato */}
          <div className="fade-in-up stagger-1">
            <div style={{
              background: 'var(--card-bg)',
              padding: '2.5rem',
              borderRadius: '12px',
              border: '1px solid #333',
              height: 'fit-content'
            }}>
              <h3 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.8rem',
                color: 'var(--primary-yellow)',
                marginBottom: '1.5rem'
              }}>
                Informações de Contato
              </h3>

              <div style={{ marginBottom: '2rem' }}>
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '1rem',
                  marginBottom: '1rem',
                  padding: '1rem',
                  background: 'var(--darker-bg)',
                  borderRadius: '8px'
                }}>
                  <Mail size={20} style={{ color: 'var(--primary-yellow)' }} />
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      Email
                    </p>
                    <a 
                      href={`mailto:${personal.email}`}
                      style={{ 
                        color: 'var(--text-gray)', 
                        textDecoration: 'none',
                        fontSize: '0.9rem'
                      }}
                    >
                      {personal.email}
                    </a>
                  </div>
                </div>

                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '1rem',
                  marginBottom: '1rem',
                  padding: '1rem',
                  background: 'var(--darker-bg)',
                  borderRadius: '8px'
                }}>
                  <Phone size={20} style={{ color: 'var(--primary-yellow)' }} />
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      Telefone
                    </p>
                    <a 
                      href={`tel:${personal.phone}`}
                      style={{ 
                        color: 'var(--text-gray)', 
                        textDecoration: 'none',
                        fontSize: '0.9rem'
                      }}
                    >
                      {personal.phone}
                    </a>
                  </div>
                </div>

                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: '1rem',
                  padding: '1rem',
                  background: 'var(--darker-bg)',
                  borderRadius: '8px'
                }}>
                  <MapPin size={20} style={{ color: 'var(--primary-yellow)' }} />
                  <div>
                    <p style={{ color: 'var(--text-white)', fontWeight: '500' }}>
                      Localização
                    </p>
                    <p style={{ 
                      color: 'var(--text-gray)', 
                      fontSize: '0.9rem'
                    }}>
                      {personal.location}
                    </p>
                  </div>
                </div>
              </div>

              {/* Redes sociais */}
              <h4 style={{
                color: 'var(--text-white)',
                marginBottom: '1rem',
                fontSize: '1.2rem'
              }}>
                Redes Sociais
              </h4>
              
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(2, 1fr)',
                gap: '0.5rem'
              }}>
                {socialLinks.map((social, index) => (
                  <a
                    key={index}
                    href={social.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="social-link"
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '0.5rem',
                      padding: '0.8rem',
                      background: 'var(--darker-bg)',
                      borderRadius: '8px',
                      color: 'var(--text-gray)',
                      textDecoration: 'none',
                      transition: 'all 0.3s ease',
                      width: '100%',
                      height: 'auto'
                    }}
                    onMouseEnter={(e) => {
                      e.target.style.background = 'var(--primary-yellow)';
                      e.target.style.color = 'var(--dark-bg)';
                    }}
                    onMouseLeave={(e) => {
                      e.target.style.background = 'var(--darker-bg)';
                      e.target.style.color = 'var(--text-gray)';
                    }}
                  >
                    {social.icon}
                    <div>
                      <p style={{ fontSize: '0.8rem', fontWeight: '500' }}>
                        {social.name}
                      </p>
                      <p style={{ fontSize: '0.75rem', opacity: 0.8 }}>
                        {social.handle}
                      </p>
                    </div>
                  </a>
                ))}
              </div>
            </div>
          </div>

          {/* Formulário */}
          <div className="fade-in-up stagger-2">
            <form onSubmit={handleSubmit} style={{
              background: 'var(--card-bg)',
              padding: '2.5rem',
              borderRadius: '12px',
              border: '1px solid #333'
            }}>
              <h3 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.8rem',
                color: 'var(--primary-yellow)',
                marginBottom: '1.5rem'
              }}>
                Envie uma Mensagem
              </h3>

              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
                gap: '1rem',
                marginBottom: '1rem'
              }}>
                <div>
                  <label style={{
                    display: 'block',
                    color: 'var(--text-white)',
                    marginBottom: '0.5rem',
                    fontSize: '0.9rem',
                    fontWeight: '500'
                  }}>
                    Nome *
                  </label>
                  <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleInputChange}
                    required
                    style={{
                      width: '100%',
                      padding: '0.8rem',
                      background: 'var(--darker-bg)',
                      border: '1px solid #333',
                      borderRadius: '6px',
                      color: 'var(--text-white)',
                      fontSize: '0.9rem'
                    }}
                  />
                </div>

                <div>
                  <label style={{
                    display: 'block',
                    color: 'var(--text-white)',
                    marginBottom: '0.5rem',
                    fontSize: '0.9rem',
                    fontWeight: '500'
                  }}>
                    Telefone
                  </label>
                  <input
                    type="tel"
                    name="phone"
                    value={formData.phone}
                    onChange={handleInputChange}
                    style={{
                      width: '100%',
                      padding: '0.8rem',
                      background: 'var(--darker-bg)',
                      border: '1px solid #333',
                      borderRadius: '6px',
                      color: 'var(--text-white)',
                      fontSize: '0.9rem'
                    }}
                  />
                </div>
              </div>

              <div style={{ marginBottom: '1rem' }}>
                <label style={{
                  display: 'block',
                  color: 'var(--text-white)',
                  marginBottom: '0.5rem',
                  fontSize: '0.9rem',
                  fontWeight: '500'
                }}>
                  Email *
                </label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  required
                  style={{
                    width: '100%',
                    padding: '0.8rem',
                    background: 'var(--darker-bg)',
                    border: '1px solid #333',
                    borderRadius: '6px',
                    color: 'var(--text-white)',
                    fontSize: '0.9rem'
                  }}
                />
              </div>

              <div style={{ marginBottom: '1rem' }}>
                <label style={{
                  display: 'block',
                  color: 'var(--text-white)',
                  marginBottom: '0.5rem',
                  fontSize: '0.9rem',
                  fontWeight: '500'
                }}>
                  Assunto *
                </label>
                <input
                  type="text"
                  name="subject"
                  value={formData.subject}
                  onChange={handleInputChange}
                  required
                  placeholder="Ex: Orçamento para gravação comercial"
                  style={{
                    width: '100%',
                    padding: '0.8rem',
                    background: 'var(--darker-bg)',
                    border: '1px solid #333',
                    borderRadius: '6px',
                    color: 'var(--text-white)',
                    fontSize: '0.9rem'
                  }}
                />
              </div>

              <div style={{ marginBottom: '2rem' }}>
                <label style={{
                  display: 'block',
                  color: 'var(--text-white)',
                  marginBottom: '0.5rem',
                  fontSize: '0.9rem',
                  fontWeight: '500'
                }}>
                  Mensagem *
                </label>
                <textarea
                  name="message"
                  value={formData.message}
                  onChange={handleInputChange}
                  required
                  rows="5"
                  placeholder="Conte-me sobre seu projeto, prazo, localização e orçamento..."
                  style={{
                    width: '100%',
                    padding: '0.8rem',
                    background: 'var(--darker-bg)',
                    border: '1px solid #333',
                    borderRadius: '6px',
                    color: 'var(--text-white)',
                    fontSize: '0.9rem',
                    resize: 'vertical',
                    minHeight: '120px'
                  }}
                />
              </div>

              <button
                type="submit"
                disabled={isSubmitting}
                className="btn-cinematic btn-primary"
                style={{
                  width: '100%',
                  padding: '1rem',
                  fontSize: '1rem',
                  opacity: isSubmitting ? 0.7 : 1,
                  cursor: isSubmitting ? 'not-allowed' : 'pointer'
                }}
              >
                {isSubmitting ? 'Enviando...' : 'Enviar Mensagem'}
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;