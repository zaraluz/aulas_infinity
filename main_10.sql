CREATE DATABASE Escola;

USE Escola;

CREATE TABLE Professores (
    NumeroMatricula INT PRIMARY KEY,
    Nome VARCHAR(100),
    Especialidade VARCHAR(100),
    Endereco VARCHAR(255)
);

CREATE TABLE Turmas (
    Identificador INT PRIMARY KEY,
    HorarioInicio TIME,
    DiaSemana VARCHAR(20)
);

CREATE TABLE Disciplinas (
    Identificador INT PRIMARY KEY,
    Nome VARCHAR(100),
    QuantidadeAulas INT
);



