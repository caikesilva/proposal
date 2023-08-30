# Propostas

## Clonar repositório
Clone o projeto com o seguinte comando:
```sh
git clone git@github.com:caikesilva/proposal.git
```

## Build containers Docker
Após clonar o projeto execute:
```sh
cd proposal
```

Na pasta proposal execute:
```
docker compose -f docker-compose.yml up -d --build
```

## Administração
Acesse a URL de administração para efetuar o gerenciamento das propostas solicitadas, bem como para criar os campos necessários para realizar uma solicitação de proposta.
<br>
URL: http://127.0.0.1:8000/admin/

Para acessar a área de administração, utilize as credenciais fornecidas abaixo:
```
Usuário: root
Senha: root
```

## Aplicação
Acesse a URL da aplicação e faça a solicitação de uma proposta utilizando o formulário disponível.
<br>
URL: http://127.0.0.1:8000/

