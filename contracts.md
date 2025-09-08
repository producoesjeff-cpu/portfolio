# API Contracts - Portfólio Gaffer Jeferson Rodrigues

## Visão Geral
Sistema completo para portfólio de gaffer com painel administrativo para edição de conteúdo, upload de vídeos/imagens e formulário de contato com envio real de emails.

## Estrutura de Dados

### 1. Portfolio Content (Conteúdo do Portfólio)
```javascript
{
  id: string,
  personal: {
    name: string,
    role: string,
    location: string,
    email: string,
    phone: string,
    bio: string,
    heroImage: string,
    aboutImage: string,
    social: {
      instagram: string,
      linkedin: string,
      youtube: string,
      whatsapp: string
    }
  },
  demoReel: {
    title: string,
    description: string,
    videoUrl: string, // URL do YouTube/Vimeo
    thumbnail: string
  },
  services: [
    {
      title: string,
      description: string,
      icon: string
    }
  ]
}
```

### 2. Projects (Projetos)
```javascript
{
  id: string,
  title: string,
  client: string,
  year: string,
  category: string,
  description: string,
  image: string, // URL da imagem de capa
  featured: boolean,
  date: Date,
  videoUrl?: string, // Opcional para projetos com vídeo
  createdAt: Date,
  updatedAt: Date
}
```

### 3. Clients (Clientes)
```javascript
{
  id: string,
  name: string,
  logo: string, // URL da imagem do logo
  website: string,
  order: number, // Para ordenação personalizada
  active: boolean,
  createdAt: Date,
  updatedAt: Date
}
```

### 4. Contact Messages (Mensagens de Contato)
```javascript
{
  id: string,
  name: string,
  email: string,
  phone?: string,
  subject: string,
  message: string,
  read: boolean,
  replied: boolean,
  createdAt: Date
}
```

### 5. Admin User (Usuário Admin)
```javascript
{
  id: string,
  username: string,
  email: string,
  passwordHash: string,
  createdAt: Date,
  lastLogin: Date
}
```

## Endpoints da API

### Público (Frontend)

#### GET /api/portfolio
- **Descrição**: Busca dados completos do portfólio
- **Response**: Portfolio Content + Projects + Clients
- **Status**: 200

#### POST /api/contact
- **Descrição**: Envia mensagem de contato
- **Body**: { name, email, phone?, subject, message }
- **Funcionalidade**: Salva no DB + Envia email real
- **Response**: { success: true, message: "Mensagem enviada" }
- **Status**: 201

### Admin (Painel Administrativo)

#### POST /api/admin/login
- **Descrição**: Login do admin
- **Body**: { username, password }
- **Response**: { token, user }
- **Status**: 200

#### GET /api/admin/portfolio
- **Descrição**: Busca dados para edição
- **Auth**: Required
- **Response**: Portfolio Content completo
- **Status**: 200

#### PUT /api/admin/portfolio
- **Descrição**: Atualiza dados do portfólio
- **Body**: Portfolio Content
- **Auth**: Required
- **Status**: 200

#### POST /api/admin/projects
- **Descrição**: Cria novo projeto
- **Body**: Project data
- **Auth**: Required
- **Status**: 201

#### PUT /api/admin/projects/:id
- **Descrição**: Atualiza projeto
- **Body**: Project data
- **Auth**: Required
- **Status**: 200

#### DELETE /api/admin/projects/:id
- **Descrição**: Remove projeto
- **Auth**: Required
- **Status**: 204

#### GET/POST/PUT/DELETE /api/admin/clients/:id?
- **Descrição**: CRUD completo para clientes
- **Auth**: Required

#### POST /api/admin/upload
- **Descrição**: Upload de imagem/vídeo
- **Body**: FormData com arquivo
- **Auth**: Required
- **Response**: { url: string }
- **Status**: 200

#### GET /api/admin/messages
- **Descrição**: Lista mensagens de contato
- **Auth**: Required
- **Query**: ?page=1&limit=20&read=false
- **Status**: 200

#### PUT /api/admin/messages/:id
- **Descrição**: Marca mensagem como lida
- **Auth**: Required
- **Body**: { read: true }
- **Status**: 200

## Funcionalidades do Frontend

### Páginas Atuais (Mock Data)
- ✅ Hero fullscreen com demo reel
- ✅ Transição do título ao rolar
- ✅ Seção de portfólio (featured + recent)
- ✅ Sobre mim com estatísticas
- ✅ Serviços oferecidos
- ✅ Clientes/logos
- ✅ Formulário de contato
- ✅ Footer com redes sociais

### Integrações Backend Necessárias

#### 1. Formulário de Contato
- **Arquivo**: `/components/Contact.js`
- **Mudança**: Substituir mock por chamada real da API
- **EmailJS**: Integração para envio real de emails

#### 2. Dados Dinâmicos
- **Arquivo**: `/data/mock.js` → API calls
- **Componentes**: Todos que usam portfolioData
- **Cache**: Implementar cache local para performance

#### 3. Painel Admin (Novo)
- **Rota**: `/admin`
- **Componentes**: 
  - Login
  - Dashboard
  - Editor de conteúdo
  - Lista de projetos
  - Upload de arquivos
  - Mensagens de contato

## Tecnologias Backend

### Core
- **FastAPI** (já configurado)
- **MongoDB** (já configurado)
- **Pydantic** para validação
- **JWT** para autenticação admin

### Email
- **EmailJS** ou **SendGrid** para envio
- **Variáveis de ambiente** para configuração

### Upload
- **Cloudinary** ou **AWS S3** para armazenamento
- **Pillow** para processamento de imagens

### Segurança
- **bcrypt** para senhas
- **CORS** configurado
- **Rate limiting** para APIs públicas

## Fluxo de Implementação

### Fase 1: Backend Core
1. Modelos MongoDB (Portfolio, Project, Client, Message, Admin)
2. Endpoints públicos (GET portfolio, POST contact)
3. Sistema de autenticação admin
4. Integração EmailJS/SendGrid

### Fase 2: Admin Panel
1. Login/logout admin
2. CRUD de projetos
3. Edição de dados pessoais
4. Upload de arquivos
5. Gestão de clientes/logos

### Fase 3: Frontend Integration
1. Substituir mock data por API calls
2. Sistema de loading/error states
3. Cache e otimizações
4. Testes finais

## Estrutura de Arquivos Backend
```
/backend
├── models/
│   ├── portfolio.py
│   ├── project.py
│   ├── client.py
│   ├── message.py
│   └── admin.py
├── routes/
│   ├── public.py      # Portfolio + Contact
│   ├── admin.py       # Admin operations
│   └── upload.py      # File upload
├── services/
│   ├── auth.py        # JWT handling
│   ├── email.py       # Email service
│   └── upload.py      # File upload service
└── utils/
    ├── database.py    # DB connection
    └── config.py      # Environment config
```

## Configurações Necessárias

### Environment Variables (.env)
```
# Email Service
EMAILJS_SERVICE_ID=
EMAILJS_TEMPLATE_ID=
EMAILJS_USER_ID=

# Admin
ADMIN_SECRET_KEY=
JWT_SECRET_KEY=

# Upload (Cloudinary)
CLOUDINARY_CLOUD_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

### Admin Default User
- **Username**: admin
- **Password**: Será definido durante setup
- **Email**: jeferson@exemplo.com (ou email real fornecido)

## Mock Data Migration
O arquivo `/data/mock.js` contém todos os dados de exemplo que serão migrados para o banco de dados durante a primeira execução do backend.