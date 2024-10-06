Quadro de Chaves
Este é um projeto de gerenciamento de chaves usando Python e Tkinter. O sistema permite o controle de retirada e devolução de chaves, além de registrar eventos associados a esses processos. Foi adicionado um sistema de login para identificar qual usuário interagiu com as chaves.

Funcionalidades
Login de Usuário: Apenas usuários autorizados podem acessar o sistema. Atualmente, há quatro usuários registrados: "Usuario1", "Usuario2", "Usuario3", "Usuario4".
Gerenciamento de Chaves: Permite registrar a retirada e devolução de chaves, exibindo quem retirou a chave e quando.
Histórico de Eventos: Registra todos os eventos de retirada e devolução, permitindo a geração de relatórios.
Resetar Estado: Possibilidade de resetar o estado de todas as chaves, tornando-as disponíveis novamente.
Relatórios: Geração de relatórios detalhados sobre a retirada e devolução de chaves.
Configuração do Banco de Dados
O sistema utiliza um banco de dados SQLite para armazenar informações sobre as chaves e o histórico de eventos. O banco de dados é criado automaticamente ao iniciar o programa.

Como Executar
Certifique-se de ter o Python instalado em seu sistema.
Instale a biblioteca Tkinter, caso ainda não esteja instalada. No Windows, geralmente já vem instalada com o Python.
Execute o script principal para iniciar o programa:
python nome_do_arquivo.py
Faça login utilizando um dos usuários permitidos.
Utilize a interface gráfica para gerenciar as chaves.
Estrutura do Projeto
Banco de Dados: chaves.db - Armazena informações sobre as chaves e eventos.
Interface Gráfica: Implementada usando Tkinter, com botões para cada chave e menus para operações adicionais.
Código Principal: Contém a lógica para login, gerenciamento de chaves e geração de relatórios.
Desenvolvedor
Este projeto foi desenvolvido por @ReehCitelli com assistência da IA Monica.

Licença
Este projeto é livre para uso e modificação de acordo com as necessidades do usuário.
