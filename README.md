**SI-IT**

**I - INSTRUÇÕES INICIAIS**

*Main.py* - é o núcleo do código.

*Auth_functions.py* - é o código do login.

*Sql_functions.py* - é o código do banco de dados.

*Mock_data.py* - está alguns dados de teste do código main.

*Credits_functions.py* - está elementos gráficos e créditos.

*Main_database.db* - é o banco de dados.


**Todos foram feitos no VSCode e podem ser abertos normalmente como arquivo python, exceto o main_database.db que precisa de alguns passos extras:**

	1) Instale a extensão SQLite

	2) Ctrl+Shift+P para abrir a command pallete 
	procure e selecione SQLite: Open Database.

	3) Ainda no command pallete, selecione main-database.db: 
	a aba SQLITE EXPLORER aparecerá na parte inferior do Explorer(Ctrl+Shift+E) do VScode,
	clicar nas setas.


**II SUMÁRIO**

O objetivo deste código é criar um banco de dados de atrações turísticas, que combinados se tornem roteiros turísticos. Também implementamos recursos de acesso personalizado (login), criação de roteiros personalizados, categorização das atrações turísticas, salvar e exportar roteiros e criação de roteiros aleatórios. Para tal, utilizamos abundantemente listas e dicionários, mas também funções, iterações, condicionais, manipulação de strings e arquivos, e o SQLite para criação de um banco de dados simplificado.

**III LIBRARIES**

*Random*

	Geração de aleatóriedades para criar o roteiro aleatório, 
	será explicado detalhadamente mais adiante.

*Time*

	Criação de pequenos intervalos de tempo na execução do código, 
	com  finalidade estética de na exibição do código no terminal simular uma “busca” no banco de dados. 
	Fizemos uso desse recurso no roteiro aleatório e no roteiro personalizado, 
	serão explicados detalhadamente mais adiante.

*System*

	Por meio da função system(‘cls’) limpar a tela do terminal, para melhor estética e clareza. 
	Foi utilizado por todo o código


**IV BANCO DE DADOS**

*SQLITE é uma biblioteca feita na linguagem C que implementa um banco de dados relacional SQL em forma de arquivo. 
Dessa forma, é possível fazer todas as “queries” ao banco e assim conseguir testar o programa como um todo.*

	*connect_to_database()*
	Essa função é responsável por criar uma conexão com o banco de dados sqlite;
	Criar as tabelas de atrações e usuários, caso elas não existem.
	Retornar a conexão criada.

	*create_attractions(connection)*
	Essa função é responsável por popular a tabela de atrações no banco de dados;
	Recebe a conexão do sqlite como parâmetro, e através dela consegue realizar a query e adicionar as atrações no banco.

	*create_user(connection, user)*
	Essa função é responsável por criar um usuário no banco de dados;
	Recebe a conexão e o usuário como parâmetros.
	Adiciona na tabela usuários o ‘user’.

	*select_attractions(connection)*
	Essa função é responsável por retornar as atrações do banco de dados;
	Recebe a conexão como parâmetro;
	Busca as atrações no banco através de uma query ‘SELECT’ e transforma-as em uma lista de tuplas;
	Transforma a lista de tuplas em uma lista de dicionários; 
	Retorna a lista de usuários.

	*get_attractions(connection)*
	Essa função é responsável por retornar as atrações formatadas;
	Recebe a conexão como parâmetro;
	Pega as atrações da função select_attractions e formata os horários de cada atração, transformando a string em lista.


**V LOGIN**

A autenticação funciona de tal forma que é possível criar uma conta nova e fazer o login com a senha e o código gerado pelo programa.

	criar_conta(contas, connection)
	 Essa função é responsável por criar a conta do usuário;
	 Recebe como parâmetro a lista de contas e conexão do banco de dados;
	 Responsável pela verificação se o CPF do usuário já existe no banco;
	 Caso não exista, recebe os dados do usuário através dos inputs;
	 Invoca a função create_user passando os dados do usuário e a conexão.

	acesso_conta(contas)
	 Essa função é responsável por logar o usuário no programa;
	 Recebe como parâmetro a lista de contas;
	 Checa se o código e a senha do usuário está correta;
	 Se tiver, retorna True e prossegue com a aplicação;
	 Senão, retorna False e o usuário pode fazer de novo o login..



**VI ATRAÇÕES E ROTEIROS**

Definimos a seguinte estrutura geral:

	atraçao={‘ID’: integer identificador ,
		‘NOME’: ‘Nome da Atração’,
		‘DESCRICAO’:’descrição da atração’,
		‘TIPO’:’categoria da atração’,
		'HORARIOS’:’dia/noite,’
		}
	// Módulo-base do código, conteúdo em si que forma as outras listas e dicionários,
	// uma key (ID) para facilitar a manipulação, 
	// duas keys (‘NOME’ e ‘DESCRICAO’) para fins de exibição 
	// duas keys (‘TIPO’ e ‘HORARIOS’) para filtragem e busca. 
	// Keys e values são exemplificativaos, mas há infinitas possibilidades

	roteiro={‘ID’: integer identificador ,
		‘NOME’: ‘Nome do Roteiro’,
		‘ATRACOES’: [lista de atrações],
			}
	// Conjunto de atrações com chaves identificadoras para fins de exibição.

	atracoes=[{atracao1}, {atracao2}...]
	// Lista com todas as atrações, para facilitar a busca ao longo do código.

	roteiros=[{roteiro1}, {roteiro2}, {roteiro3}]]
	// Lista de roteiros já prontos para facilitar sua busca no código por meio de iterações.

	meu_roteiro=[{atracao1},{atracao2}... ]
	// Lista de atrações para o roteiro personalizado do usuário, de natureza temporária, 
	// é transformada em dicionário no mesmo formato do “roteiro={}” quando é salvo pelo usuário.

	meus_roteiros=[{meu_roteiro1}, {meu_roteiro2}...]
	// Lista dos roteiros personalizados criados pelo usuário.


*Para melhor organização, as atrações e os roteiros prontos ficam localizados no arquivo mock_data.py.*


**VII MENU PRINCIPAL**

O menu principal é um dicionário, as keys são integers e os values são strings. Que são printados por meio de um for, sendo as  keys  os comandos que o usuário deve digitar para navegar pelo menu, o zero (0) ficou convencionado como a opção de sair/voltar em todo código. Cada opção chama um subprograma.

**VIII SUBPROGRAMAS**

menu_roteiros() printa o ID e o NOME de cada roteiro pronto e fornece a condição de exportar como  um arquivo txt ou voltar para o menu principal.

menu_meu_roteiro() é o maior subprograma do código, ele printa um novo menu com 4 condições, sendo uma delas o 0 - Voltar:
	
	A **condição 1** chama uma nova função buscar_passeios() que tem como finalidade filtrar as atrações
	e adicionar a atração desejada a lista meu_roteiro. Para tal, é oferecido 3 opções:
	uma de exibir todas as atrações, que fica dentro do próprio subprograma,
	E outras duas opções de filtro por tipo ou horário, chamando suas respectivas funções com parâmetro:
	As funções horario(turno) e tipo(categoria) recebem o parâmetro para filtrar 
	nos values dos dicionários de atrações da lista atracoes
	e solicita ao usuário se ele deseja adicionar a atração à lista meu_roteiro. 
	Seguem o mesmo conceito e podem ser replicados para qualquer filtro.

	A **condição 2** serve para imprimir as atrações contidas na lista meu_roteiro,
	caso haja roteiros, se não houver, é ativado um timer e avisa que não roteiro.
	Em seguida, pergunta se o usuário deseja salvar o roteiro, caso sim: ele cria um novo dicionário,
	que estabelece o ID como o maior número utilizado por outros IDs +1 (não inviabiliza o zero do sair/voltar),
	pede para o usuário digitar o nome do roteiro, adiciona o roteiro à lista meus_roteiros 
	e apaga a lista meu_roteiro para que o usuário possa criar um novo roteiro futuramente.

	A **condição 3** printa os roteiros salvos na lista meus_roteiros por meio de um for,
	solicita que o usuário selecione um deles para receber a descrição
	e dá a opção de exportá-lo como um arquivo txt.
	
A função **role_aleatorio()** ativa um timer gráfico para simular um processamento da máquina, em seguida gera dois números aleatórios, um para a quantidade de atrações que serão sorteadas e outro para sortear este número de atrações da lista atracoes. Por fim, ele pergunta ao usuário se deseja salvá-la na lista meus_roteiros para que possa ser acessada e exportada posteriormente.

Por fim, mas não menos importante, o arquivo **credits_functions.py** tem duas funções: siit() e credit() que tem objetivos gráficos e imprimem a marca e o os créditos do time utilizando ASCII art.

**SIIT**

PROJETO 1 // CESAR.SCHOOL

**EQUIPE:**

Ana Beatriz Alves // Ciência da Computação - 1° Período A/2022.2 - abxa@cesar.school

Ana Beatriz Rocha // Design - 1° Período 2022.2 - abrbd@cesar.school

Caio Vila Nova // Design - 1° Período 2022.2 - csvn@cesar.school

Clara Wanderley // Design - 1° Período 2022.2 - mcwa@cesar.school

Edmar Rocha // Ciência da Computação 1° Período B/2022.2 - era@cesar.school

Guilherme Silveira // Ciência da Computação 1° Período A/2022.2 - gsa3@cesar.school

Pedro Coelho // Ciência da Computação - 1º Período B/2022.2 - pcdr@cesar.school

Ricardo Lima // Design - 1° Período 2022.2 - rfsl@cesar.school

Sofia Valadares // Ciência da Computação - 1° Período B/2022.2 - svc3@cesar.school

Virna Amaral // Ciência da Computação - 1° Período A/2022.2 - vfpa@cesar.school


**ORIENTADORES:**

Geysa Barvaleno - gpb2@cesar.org.br

Erick Simões - esm@cesar.school

Rodrigo Larrazábal - rrl@cesar.school
