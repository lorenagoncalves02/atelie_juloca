CREATE database if not exists juloca;
USE juloca;



CREATE TABLE if not exists cadastro (
 email VARCHAR(50) PRIMARY KEY,
 nome_usu VARCHAR(100),
 telefone VARCHAR(11),
 endereco VARCHAR(200),
 senha INT
);

CREATE TABLE if not exists carrinho (
 cod_carrinho int auto_increment PRIMARY KEY ,
 email VARCHAR(50),
 CONSTRAINT fk_carrinho_login FOREIGN KEY (email) REFERENCES cadastro (email)  
);

CREATE TABLE if not exists categoria (
 id_categoria int auto_increment PRIMARY KEY,
 nome_categoria VARCHAR(100),
 url_categoria VARCHAR(30)
);

CREATE TABLE if not exists produto (
 cod_prod  int auto_increment PRIMARY KEY,
 nome_prod VARCHAR(100),
 descricao_prod VARCHAR(200),
 preco_prod FLOAT(10),
 img_1 VARCHAR(200),
 img_2 VARCHAR(200),
 img_3 VARCHAR(200),
 id_categoria int,
 CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
);


CREATE TABLE if not exists comentarios (
 cod_comentario  int auto_increment PRIMARY KEY,
 email VARCHAR(50) NOT NULL,
 comentario VARCHAR(300),
 CONSTRAINT fk_comentarios_login FOREIGN KEY (email) REFERENCES cadastro (email)
);



CREATE TABLE if not exists item_carrinho (
 cod__item_carrinho  int auto_increment PRIMARY KEY,
 cod_prod VARCHAR(100) NOT NULL,
 cod_carrinho int NOT NULL,
 quantidade INT, 
 CONSTRAINT fk_item_carrinho_carrinho FOREIGN KEY (cod_carrinho) REFERENCES carrinho (cod_carrinho)
);