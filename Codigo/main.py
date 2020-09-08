#!/usr/bin/python
# -*- coding: utf-8 -*-

from grafo		  import *
from entradasaida import InputOutput
from simulated    import *
from solucao      import *
import			  sys

#loggin
# Funcao principal da aplicacao
def main():


	metodo_inicial  = 1
	temperatura_max = 250
	SAMAX 			= 15
	n_reaquecimento = 10
	reseta_inicial  = 0
	metodo_vizinho  = 1
	
	if ((len(sys.argv) != 8) & (len(sys.argv) !=2)) :

		print("\nERRO Sintaxe: python3 main.py <arq-entrada> <metodo-inicial 1..3> <temperatura-max> <SAMAX> <N Reaquecimento> <Reseta Inicial 0|1> <Metodo-Vizinhança 1..2>\n")
		exit()

	arq = sys.argv[1]
	entrada = InputOutput(sys.argv[1])

	if (len(sys.argv) == 8):
		metodo_inicial  = int(sys.argv[2])
		temperatura_max = int(sys.argv[3])
		SAMAX 			= int(sys.argv[4])
		n_reaquecimento = int(sys.argv[5])
		reseta_inicial	= int(sys.argv[6])
		metodo_vizinho	= int(sys.argv[7])		

	g=Grafo(entrada.listas,entrada.n_vert,entrada.n_arest)	

	# Cria a solucao inicial
	SolInicial = Solucao(g,metodo_inicial)

	#printa a soluçao inicial
	print("\nSolucao Inicial\n"+str(SolInicial))	

	# Cria uma instancia do SA
	Sa = SimulatedAnnealing(temperatura_max, 10, 0.90, SAMAX, SolInicial, n_reaquecimento, reseta_inicial, metodo_vizinho)
	MelhorSolucao = Sa.Solve()

	#Printa melhor solução encontrada
	print("\nMelhor encontrada\n"+str(MelhorSolucao))
	return 0
main()
