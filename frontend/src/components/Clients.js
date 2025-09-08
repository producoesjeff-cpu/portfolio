import React from 'react';
import { usePortfolio } from '../hooks/usePortfolio';

const Clients = () => {
  const { clients } = portfolioData;

  return (
    <section className="section-spacing" style={{ 
      background: 'var(--dark-bg)',
      borderTop: '1px solid #333',
      borderBottom: '1px solid #333'
    }}>
      <div className="container-gaffer">
        <div className="fade-in-up">
          <h2 className="section-title" style={{ fontSize: '2rem', marginBottom: '1rem' }}>
            Clientes & Parceiros
          </h2>
          <p className="body-large" style={{ 
            textAlign: 'center', 
            marginBottom: '3rem',
            maxWidth: '600px'
          }}>
            Trabalhei com grandes marcas e produtoras criando a iluminação perfeita para suas histórias
          </p>
        </div>

        <div className="clients-grid fade-in-up stagger-1">
          {clients.map((client) => (
            <div
              key={client.id}
              className="client-logo"
              onClick={() => {
                if (client.website && client.website !== '#') {
                  window.open(client.website, '_blank');
                }
              }}
              style={{
                cursor: client.website && client.website !== '#' ? 'pointer' : 'default'
              }}
            >
              {client.name}
            </div>
          ))}
        </div>

        {/* Nota sobre edição */}
        <div className="fade-in-up stagger-2" style={{
          textAlign: 'center',
          marginTop: '2rem',
          padding: '1.5rem',
          background: 'var(--card-bg)',
          borderRadius: '8px',
          border: '1px solid #333'
        }}>
          <p style={{
            color: 'var(--text-gray)',
            fontSize: '0.9rem',
            fontStyle: 'italic'
          }}>
            💡 Os logos dos clientes serão personalizáveis através do painel administrativo
          </p>
        </div>

        {/* Estatísticas adicionais */}
        <div className="fade-in-up stagger-3" style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '2rem',
          marginTop: '3rem',
          textAlign: 'center'
        }}>
          <div>
            <h3 style={{
              fontSize: '2.5rem',
              fontWeight: '700',
              color: 'var(--primary-yellow)',
              marginBottom: '0.5rem'
            }}>
              100%
            </h3>
            <p style={{ color: 'var(--text-gray)' }}>
              Projetos entregues no prazo
            </p>
          </div>

          <div>
            <h3 style={{
              fontSize: '2.5rem',
              fontWeight: '700',
              color: 'var(--primary-yellow)',
              marginBottom: '0.5rem'
            }}>
              24h
            </h3>
            <p style={{ color: 'var(--text-gray)' }}>
              Tempo de resposta médio
            </p>
          </div>

          <div>
            <h3 style={{
              fontSize: '2.5rem',
              fontWeight: '700',
              color: 'var(--primary-yellow)',
              marginBottom: '0.5rem'
            }}>
              8+
            </h3>
            <p style={{ color: 'var(--text-gray)' }}>
              Anos de experiência
            </p>
          </div>

          <div>
            <h3 style={{
              fontSize: '2.5rem',
              fontWeight: '700',
              color: 'var(--primary-yellow)',
              marginBottom: '0.5rem'
            }}>
              50+
            </h3>
            <p style={{ color: 'var(--text-gray)' }}>
              Produções iluminadas
            </p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Clients;