﻿
** Preparação do servidor de banco de dados da Azure para MySQL **


1. Criar servidor de banco de dados na Azure para MySQL

user: tux

password: Mud@r123



2. Após o servidor criado, usar o MySQL Workbench para conexão e executar os comandos.


CREATE DATABASE db_azure;


USE db_azure;


CREATE TABLE tbl_fala(
id INT AUTO_INCREMENT PRIMARY KEY,
texto TEXT
)


3. Configurar o arquivo "falaEmTexto_loop_ver2.py" , linha 66, com o endereço do Servidor de banco de dados MySQL do Azure.


host = ''


--------------------------------------------------------------------------------------------------------------------------