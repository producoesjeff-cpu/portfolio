// Mock data para o portfólio do Jeferson Rodrigues - Gaffer

export const portfolioData = {
  // Informações pessoais
  personal: {
    name: "Jeferson Rodrigues",
    role: "Gaffer | Iluminação Audiovisual",
    location: "São Paulo & Rio de Janeiro",
    email: "jeferson@exemplo.com",
    phone: "+55 11 9999-9999",
    social: {
      instagram: "@jefersonrodrigues",
      linkedin: "jeferson-rodrigues",
      youtube: "@jefersonrodrigues",
      whatsapp: "5511999999999"
    },
    bio: "Profissional especializado em iluminação para produções audiovisuais com mais de 8 anos de experiência. Trabalho como Gaffer em grandes produções para Netflix, canais de TV e campanhas publicitárias. Minha especialidade é criar a atmosfera perfeita através da luz, transformando conceitos em realidade visual.",
    heroImage: "https://images.unsplash.com/photo-1576280314550-773c50583407?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHwxfHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
    aboutImage: "https://images.unsplash.com/photo-1649334977308-32becd48fc63?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwyfHxnYWZmZXJ8ZW58MHx8fHwxNzU3MjkwMjAyfDA&ixlib=rb-4.1.0&q=85"
  },

  // Demo reel (placeholder)
  demoReel: {
    title: "Demo Reel 2024",
    description: "Principais trabalhos em iluminação cinematográfica",
    videoUrl: "", // Será preenchido quando o usuário fornecer
    thumbnail: "https://images.unsplash.com/photo-1649376673488-739e6d8f5d99?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1ODF8MHwxfHNlYXJjaHwxfHxnYWZmZXJ8ZW58MHx8fHwxNzU3MjkwMjAyfDA&ixlib=rb-4.1.0&q=85"
  },

  // Trabalhos em destaque
  featuredWorks: [
    {
      id: 1,
      title: "Série Netflix Original",
      client: "Netflix",
      year: "2024",
      category: "Série",
      description: "Iluminação principal para série dramática de 8 episódios",
      image: "https://images.unsplash.com/photo-1619473667737-b3abeb860aa1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHw0fHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
      featured: true
    },
    {
      id: 2,
      title: "Campanha Seara",
      client: "Seara",
      year: "2024",
      category: "Publicidade",
      description: "Direção de fotografia e iluminação para campanha nacional",
      image: "https://images.unsplash.com/photo-1625690303837-654c9666d2d0?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHwyfHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
      featured: true
    },
    {
      id: 3,
      title: "Documentário MIO",
      client: "MIO",
      year: "2023",
      category: "Documentário",
      description: "Iluminação natural e artificial para documentário institucional",
      image: "https://images.unsplash.com/photo-1490971774356-7fac993cc438?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzF8MHwxfHNlYXJjaHwxfHxmaWxtJTIwbGlnaHRpbmd8ZW58MHx8fHwxNzU3MjkwMTk3fDA&ixlib=rb-4.1.0&q=85",
      featured: true
    },
    {
      id: 4,
      title: "Comercial Nutrata",
      client: "Nutrata",
      year: "2023",
      category: "Comercial",
      description: "Setup de iluminação complexo para produto alimentício",
      image: "https://images.unsplash.com/photo-1611784728558-6c7d9b409cdf?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzB8MHwxfHNlYXJjaHwzfHxjaW5lbWF0b2dyYXBoeXxlbnwwfHx8fDE3NTcyOTAxOTJ8MA&ixlib=rb-4.1.0&q=85",
      featured: true
    }
  ],

  // Projetos recentes
  recentProjects: [
    {
      id: 5,
      title: "Freboy - Videoclipe",
      client: "Freboy",
      year: "2024",
      category: "Videoclipe",
      description: "Iluminação criativa com neon e LED para videoclipe",
      image: "https://images.pexels.com/photos/3379934/pexels-photo-3379934.jpeg",
      date: "2024-01-15"
    },
    {
      id: 6,
      title: "Maturatta - Institutional",
      client: "Maturatta",
      year: "2024",
      category: "Institucional",
      description: "Vídeo corporativo com iluminação natural e técnica",
      image: "https://images.pexels.com/photos/3379942/pexels-photo-3379942.jpeg",
      date: "2024-02-20"
    }
  ],

  // Serviços oferecidos
  services: [
    {
      title: "Gaffer",
      description: "Direção de iluminação para cinema, TV e publicidade",
      icon: "lightbulb"
    },
    {
      title: "Direção de Fotografia",
      description: "Conceito visual e estética cinematográfica",
      icon: "camera"
    },
    {
      title: "Consultoria Técnica",
      description: "Planejamento de equipamentos e orçamentos",
      icon: "settings"
    },
    {
      title: "Color Grading",
      description: "Finalização e correção de cor",
      icon: "palette"
    }
  ],

  // Clientes - logos editáveis
  clients: [
    {
      id: 1,
      name: "Netflix",
      logo: "/api/placeholder/120/60", // Placeholder - será substituído
      website: "https://netflix.com"
    },
    {
      id: 2,
      name: "MIO",
      logo: "/api/placeholder/120/60",
      website: "#"
    },
    {
      id: 3,
      name: "Seara",
      logo: "/api/placeholder/120/60",
      website: "#"
    },
    {
      id: 4,
      name: "Nutrata",
      logo: "/api/placeholder/120/60",
      website: "#"
    },
    {
      id: 5,
      name: "Freboy",
      logo: "/api/placeholder/120/60",
      website: "#"
    },
    {
      id: 6,
      name: "Maturatta",
      logo: "/api/placeholder/120/60",
      website: "#"
    }
  ]
};

export default portfolioData;