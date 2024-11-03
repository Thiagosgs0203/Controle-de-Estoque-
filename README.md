1. Introdução ao Projeto
Objetivo do sistema: permitir o controle e monitoramento do estoque de produtos de uma loja.
Principais funcionalidades: adicionar, editar, excluir e consultar produtos em estoque.
2. Tecnologias Utilizadas
Flask: framework backend para gerenciar a lógica do sistema.
SQLite: banco de dados para armazenar informações de produtos e usuários.
HTML, CSS, Bootstrap: para criar uma interface de usuário responsiva e amigável.
Flask-Login: para autenticação e restrição de acesso ao sistema.
Git e Render: controle de versão e deploy online da aplicação.
3. Funcionalidades do Sistema
Cadastro e Autenticação de Usuários: controle de acesso para garantir que apenas funcionários autorizados possam gerenciar o estoque.
Painel de Controle de Estoque:
Interface para visualização e gerenciamento de produtos em estoque.
Cadastro de Produtos: formulário para adicionar novos produtos com detalhes como nome, descrição, categoria, preço e quantidade.
Edição e Exclusão de Produtos: funcionalidades para atualizar informações e remover produtos, com confirmações para segurança.
Consulta de Produtos: pesquisa e filtro de produtos por nome, categoria e outros critérios.
4. Funcionalidades Avançadas
Alertas de Estoque Baixo: notificação quando a quantidade de um produto atinge um nível crítico.
Histórico de Movimentação de Estoque: registro de operações no estoque (adições, edições, exclusões), facilitando auditorias e análises.
5. Segurança e Controle de Acesso
Implementação de restrições de acesso utilizando Flask-Login para garantir que apenas usuários autenticados tenham permissão para gerenciar o estoque.
6. Deploy e Controle de Versão
Git: uso de controle de versão para gerenciar o desenvolvimento.
Render: deploy da aplicação, permitindo que o sistema esteja disponível para acesso online.
Render: deploy da aplicação na plataforma, permitindo acesso online ao sistema.

