CREATE TABLE biblioteca.livros (
	id INT NOT NULL auto_increment,
	nome TEXT NULL,
	ano VARCHAR(5) NULL,
	reservado INT NULL,
	categoriaId INT NULL,
	tematicaId INT NULL,
	quantidade INT NULL,
    quantidadeReservada INT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE biblioteca.categorias (
	id INT NOT NULL auto_increment,
	nome TEXT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE biblioteca.tematicas (
	id INT NOT NULL auto_increment,
	nome TEXT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE biblioteca.reservas (
	id INT NOT NULL auto_increment,
	nomePessoa TEXT NULL,
    idLivro INT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE biblioteca.usuarios (
	id INT NOT NULL auto_increment,
	login TEXT NULL,
    senha INT NULL,
	PRIMARY KEY (id)
);