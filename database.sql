CREATE TABLE IF NOT EXISTS alunos (
    id serial primary key,
    nome varchar(50),
    idade smallint,
    nota int
);

INSERT INTO alunos (nome, idade, nota) VALUES
('Lucas', 15, 9),
('Pedro', 13, 7),
('Gabriel', 15, 5),
('Maria', 15, 10),
('Luiza', 15, 4);