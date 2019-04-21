Nome: Wesley Benício

Sistema Operacional:
	Windows 7 Ultimate 64 bits
Compilador:
	Anaconda - Spyder --versão: 3.2.8
	Python 3.6.0

Passos para compilar:
	O programa vem com os 2 Simuladores de automatos finito.
	Na pasta local ao programa, onde possui o código fonte, deve conter 3 arquivos txt: dfaTabela.txt,nfaTabela.txt,entrada.txt. Para que o programa funcione perfeitamente.
	Os testes realizados com base nos exemplos. Pode haver anormalidades em outros exemplos
	Estrutura do Arquivo: A tabela de transição deve estar organizada da seguinte forma:
para dfaTabela.txt:
\t(entrada1)\t(entrada2)\n
>(estado)\t(estado)\t(estado)\n
*(estado)\t(estado)\t(estado)\n

> representa estado inicial
* representa estados finais
\t representa tecla TAB 
\n representa New Line (enter)
() os parenteses não devem ser expressados

para tabela de transição NFA deve ser estruturada da mesma maneira com o simbolo de leitura vazia sempre em ultimo:
para nfaTabela:
\t(entrada1)\t(entrada2)\t(&)\n
>{estado}\t{estado}\t{estado}\n
*{estado}\t{estado}\t{estado}\n
...

{} As chaves devem ser expressadas

é recomendável usar apenas duas entradas binárias(0,1) para DFA, e duas entradas com letras(a-z) para NFA + &(string vazia).

Há algumas restrições sobre algumas funções que podem ocasionar erro:
def move(est,entrada,estados,alpha): - Só funciona com um conjunto de estado (ex:q1,q2,q3) tem que possuir +1.

OBS: os dois programas compartilham da mesma entrada, então tome cuidado para que a entrada esteja correta!