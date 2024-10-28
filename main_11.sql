CREATE DATABASE loja_online;
USE loja_online;

CREATE TABLE Produtos (
    id_produto INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    preco_produto DECIMAL(10, 2),
    quantidade_estoque INT
);

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    email_cliente VARCHAR(100)
);

CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY,
    data_pedido DATE,
    id_cliente INT,
    status_pedido VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Itens_Pedido (
    id_item_pedido INT PRIMARY KEY,
    id_pedido INT,
    id_produto INT,
    quantidade INT,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);


