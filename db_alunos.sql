INSERT INTO `db_alunos`.`tabela_alunos` (nome_alunos, idade, cpf) VALUES ("Joao Felipe", "24", "05765339123");

INSERT INTO `db_alunos`.`tabela_alunos` (nome_alunos, idade, cpf) VALUES ("Emerson", "24", "02556639525");

INSERT INTO `db_alunos`.`tabela_alunos` (nome_alunos, idade, cpf) VALUES ("Ana", "22", "01933453150");

INSERT INTO `db_alunos`.`tabela_alunos` (nome_alunos, idade, cpf) VALUES ("Pedro", "26", "02665339123");

UPDATE `db_alunos`.`tabela_alunos` SET cpf = "02336225391" WHERE id = "1";

DELETE from `db_alunos`.`tabela_alunos` WHERE id = "";

SELECT * from `db_alunos`.`tabela_alunos` where idade > 20;