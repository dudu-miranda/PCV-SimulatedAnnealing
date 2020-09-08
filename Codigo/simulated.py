#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy
from solucao import *
from random import uniform
from math import exp

class SimulatedAnnealing():

	def __init__(self, TInicial, TFinal, Alpha, SaMax, SolInicial, Reaquece, reseta_inicial, metodo_vizinho):

		self.TInicial = TInicial
		self.TFinal   = TFinal
		self.Alpha    = Alpha
		self.SaMax    = SaMax
		self.SolIni   = SolInicial
		self.Reaquece = Reaquece
		self.reseta_inicial = reseta_inicial
		self.metodo_vizinho = metodo_vizinho

	def Solve(self):
		
		# Define a melhor solucao como sendo a inicial
		SolMelhor   = deepcopy(self.SolIni)
		SolCorrente = deepcopy(self.SolIni)
		TCorrente = self.TInicial

		k = 0
		while k<self.Reaquece:
			k+=1
			#print("Iteração n - "+str(k))

			# Executa ate o sistema esfriar
			while (TCorrente >= self.TFinal) :

				#print("Temp = ", str(TCorrente))

				Iter = 0

				# Explora a vizinhanca
				while (Iter < self.SaMax):

					Iter = Iter + 1
					# Clona o vizinho
					SolVizinho = deepcopy(SolCorrente)
					if(self.metodo_vizinho == 1):
						SolVizinho.GeraVizinho1()
					elif(self.metodo_vizinho == 2):
						SolVizinho.GeraVizinho2()	

					# Compara para ver se é melhor
					Delta = SolVizinho.Objetivo() - SolCorrente.Objetivo()

					if(Delta < 0) :
				
						# Aceita de cara
						SolCorrente = deepcopy(SolVizinho)

						# Verifica se é melhor do que a overall
						if SolVizinho.Objetivo() < SolMelhor.Objetivo():

							# Atualiza a overall
							SolMelhor = deepcopy(SolVizinho)
							#print("\n\tUpdate Melhor em ", str(TCorrente), " com Obj = ", str(SolMelhor.Objetivo()), "\n")
							#print(SolMelhor)

					else :

						# Gera numero uniforme r ~ U(0,1)
						r = uniform(0,1)

						# Testa o criterio de Boltzmann
						if r <= exp(-Delta/TCorrente) :

							# Aceita uma solucao pior
							SolCorrente = deepcopy(SolVizinho)

				# Decai a temperatura
				TCorrente = TCorrente * self.Alpha

			#reinicia a temperatura corrente
			TCorrente = self.TInicial
			#Reinicia a soluçaõ corrente para a melhor solução atual
			SolCorrente = deepcopy(SolMelhor)
			
		# Retorna a melhor solucao encontrada no caminhamento
		return SolMelhor