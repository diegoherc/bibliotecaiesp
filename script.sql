CREATE TABLE biblioteca.livros (
	id BIGINT auto_increment NOT NULL,
	nome TEXT NULL,
	ano VARCHAR(5) NULL,
	reservado INT NULL,
	categoriaId BIGINT NULL,
	tematicaId BIGINT NULL,
	quantidade BIGINT NULL,
    quantidadeReservada BIGINT NULL,
	PRIMARY KEY (id)
)
CREATE TABLE biblioteca.categorias (
	id BIGINT auto_increment NOT NULL,
	nome TEXT NULL,
	PRIMARY KEY (id)
)
CREATE TABLE biblioteca.tematicas (
	id BIGINT auto_increment NOT NULL,
	nome TEXT NULL,
	PRIMARY KEY (id)
)
CREATE TABLE biblioteca.reservas (
	id BIGINT auto_increment NOT NULL,
	nomePessoa TEXT NULL,
    idLivro INT NULL,
	PRIMARY KEY (id)
)