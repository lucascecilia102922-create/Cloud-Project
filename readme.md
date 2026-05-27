# Loja Veloz – Plataforma Cloud DevOps

# Link do vídeo de apresentação do projeto:  
https://youtu.be/OZ7rO_1_tM0

## Objetivo

Projeto de modernização da plataforma de pedidos da Loja Veloz.

A solução implementa:

- Docker Compose
- Microsserviços
- Kubernetes
- GitHub Actions
- Terraform
- Observabilidade
- Escalabilidade automática

---

# Arquitetura

```text
Cliente
 ↓
API Gateway
 ├── Pedidos
 ├── Pagamentos
 ├── Estoque
 ↓
PostgreSQL

RabbitMQ
```

---

# Tecnologias

- Python + Flask
- Docker
- Kubernetes
- GitHub Actions
- Terraform
- PostgreSQL
- RabbitMQ
- Prometheus
- Grafana
- OpenTelemetry

---

# Estrutura

```bash
loja-veloz/
│
├── docker-compose.yml
├── gateway/
├── pedidos/
├── pagamentos/
├── estoque/
├── k8s/
├── terraform/
└── .github/
```

---

# Executando localmente

Pré-requisitos:

- Docker
- Docker Compose

Comando:

```bash
docker compose up --build
```

---

# Serviços

Gateway:

http://localhost:8080

RabbitMQ:

http://localhost:15672

---

# Fluxo da aplicação

1 usuário acessa gateway

2 gateway recebe requisição

3 gateway consulta pedidos

4 pedidos publica evento

5 rabbitmq envia evento

6 estoque processa

7 pagamento valida

8 postgres salva

9 gateway responde

---

# Kubernetes

Aplicar manifests:

```bash
kubectl apply -f k8s/
```

Verificar:

```bash
kubectl get pods
```

---

# Pipeline CI/CD

Fluxo:

- push
- build
- testes
- publicação
- deploy

Arquivo:

```bash
.github/workflows/ci-cd.yml
```

---

# Deploy

Estratégia:

Rolling Update

Benefícios:

- sem downtime
- baixo risco
- rollback fácil

---

# Escalabilidade

HPA

CPU > 70%

Escala:

2 → 6 pods

---

# Terraform

Executar:

```bash
terraform apply
```

---

# Benefícios

- ambiente padronizado
- automação
- deploy seguro
- escalabilidade
- observabilidade
- recuperação automática
- rastreabilidade

