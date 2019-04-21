Nome: Wesley Ben�cio

Sistema Operacional:
	Windows 7 Ultimate 64 bits
Compilador:
	Anaconda - Spyder --vers�o: 3.2.8
	Python 3.6.0

Passos para compilar:
	O programa vem com os 2 Simuladores de automatos finito.
	Na pasta local ao programa, onde possui o c�digo fonte, deve conter 3 arquivos txt: dfaTabela.txt,nfaTabela.txt,entrada.txt. Para que o programa funcione perfeitamente.
	Os testes realizados com base nos exemplos. Pode haver anormalidades em outros exemplos
	Estrutura do Arquivo: A tabela de transi��o deve estar organizada da seguinte forma:
para dfaTabela.txt:
\t(entrada1)\t(entrada2)\n
>(estado)\t(estado)\t(estado)\n
*(estado)\t(estado)\t(estado)\n

> representa estado inicial
* representa estados finais
\t representa tecla TAB 
\n representa New Line (enter)
() os parenteses n�o devem ser expressados

para tabela de transi��o NFA deve ser estruturada da mesma maneira com o simbolo de leitura vazia sempre em ultimo:
para nfaTabela:
\t(entrada1)\t(entrada2)\t(&)\n
>{estado}\t{estado}\t{estado}\n
*{estado}\t{estado}\t{estado}\n
...

{} As chaves devem ser expressadas

� recomend�vel usar apenas duas entradas bin�rias(0,1) para DFA, e duas entradas com letras(a-z) para NFA + &(string vazia).

H� algumas restri��es sobre algumas fun��es que podem ocasionar erro:
def move(est,entrada,estados,alpha): - S� funciona com um conjunto de estado (ex:q1,q2,q3) tem que possuir +1.

OBS: os dois programas compartilham da mesma entrada, ent�o tome cuidado para que a entrada esteja correta!