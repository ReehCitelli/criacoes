Key Management Board

This is a key management project using Python and Tkinter. The system allows for the control of key check-outs and returns, as well as recording events associated with these processes. A login system has been added to identify which user interacted with the keys.

Features
User Login: Only authorized users can access the system. Currently, there are four registered users: "User1", "User2", "User3", "User4".
Key Management: Allows registering the check-out and return of keys, displaying who took the key and when.
Event History: Records all check-out and return events, allowing for report generation.
Reset State: Ability to reset the state of all keys, making them available again.
Reports: Generation of detailed reports on key check-outs and returns.
Database Setup
The system uses an SQLite database to store information about keys and event history. The database is automatically created upon starting the program.

How to Run
Ensure you have Python installed on your system.
Install the Tkinter library if it's not already installed. On Windows, it usually comes installed with Python.
Run the main script to start the program:
python script_name.py
Log in using one of the allowed users.
Use the graphical interface to manage the keys.
Project Structure
Database: keys.db - Stores information about keys and events.
Graphical Interface: Implemented using Tkinter, with buttons for each key and menus for additional operations.
Main Code: Contains logic for login, key management, and report generation.
Developer
This project was developed by @ReehCitelli with assistance from AI Monica.

License
This project is free to use and modify according to the user's needs.

*************************************************************************************************************************************

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
