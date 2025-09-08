import React from 'react';
import { ExternalLink, Calendar, Tag } from 'lucide-react';
import { portfolioData } from '../data/mock';

const Portfolio = () => {
  const { featuredWorks, recentProjects } = portfolioData;

  const ProjectCard = ({ project, featured = false }) => (
    <div className={`project-card ${featured ? 'featured' : ''}`}>
      <img
        src={project.image}
        alt={project.title}
        className="project-image"
      />
      
      <div className="project-overlay">
        <h3 className="project-title" style={{ color: '#0f0f10', textAlign: 'center' }}>
          {project.title}
        </h3>
        <p className="project-client" style={{ color: '#0f0f10', marginBottom: '1rem' }}>
          {project.client} • {project.year}
        </p>
        <p style={{ color: '#0f0f10', textAlign: 'center', maxWidth: '250px' }}>
          {project.description}
        </p>
        <div style={{ 
          marginTop: '1rem', 
          display: 'flex', 
          alignItems: 'center', 
          gap: '0.5rem',
          color: '#0f0f10'
        }}>
          <Tag size={16} />
          <span>{project.category}</span>
        </div>
      </div>
      
      <div className="project-content">
        <h3 className="project-title">{project.title}</h3>
        <p className="project-client">{project.client}</p>
        <p className="body-text" style={{ marginTop: '0.5rem', fontSize: '0.9rem' }}>
          {project.description}
        </p>
        
        <div style={{ 
          marginTop: '1rem', 
          display: 'flex', 
          justifyContent: 'space-between',
          alignItems: 'center',
          fontSize: '0.8rem',
          color: '#666'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Calendar size={14} />
            <span>{project.year}</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Tag size={14} />
            <span>{project.category}</span>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <section id="portfolio" className="section-spacing" style={{ background: 'var(--dark-bg)' }}>
      <div className="container-gaffer">
        {/* Trabalhos em destaque */}
        <div className="fade-in-up">
          <h2 className="section-title">Trabalhos em Destaque</h2>
        </div>
        
        <div className="project-grid fade-in-up stagger-1">
          {featuredWorks.map((project) => (
            <ProjectCard key={project.id} project={project} featured={true} />
          ))}
        </div>

        {/* Projetos recentes */}
        <div className="fade-in-up" style={{ marginTop: '4rem' }}>
          <h2 className="section-title">Projetos Recentes</h2>
          <p className="body-large" style={{ textAlign: 'center', marginBottom: '2rem' }}>
            Últimos trabalhos realizados em ordem cronológica
          </p>
        </div>
        
        <div className="project-grid fade-in-up stagger-2">
          {recentProjects.map((project) => (
            <ProjectCard key={project.id} project={project} />
          ))}
        </div>

        {/* Call to action */}
        <div className="fade-in-up stagger-3" style={{ 
          textAlign: 'center', 
          marginTop: '3rem' 
        }}>
          <p className="body-text" style={{ marginBottom: '1.5rem' }}>
            Interessado em trabalhar comigo?
          </p>
          <button 
            onClick={() => {
              const element = document.getElementById('contact');
              if (element) element.scrollIntoView({ behavior: 'smooth' });
            }}
            className="btn-cinematic btn-primary"
          >
            Vamos Conversar
          </button>
        </div>
      </div>
    </section>
  );
};

export default Portfolio;