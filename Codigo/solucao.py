#!/usr/bin/python
# -*- coding: utf-8 -*-

from grafo  import Grafo
from math   import inf
from random import shuffle, random, randint
from copy   import deepcopy

class Solucao():

	def __init__(self, GrafoOriginal, Metodo):

		self.GrafoOriginal	   = deepcopy(GrafoOriginal)
		self.g 		           = GrafoOriginal
		self.coberturaFinal	   = []
		self.PermutacaoVerts   = []

		for i in range(0, len(self.g.grafo)):
			self.PermutacaoVerts.append(i)		

		# Random
		if Metodo == 1:

			shuffle(self.PermutacaoVerts)

		#Do maior pro menor em grau, guloso
		elif Metodo == 2:
		
			self.PermutacaoVerts.sort(key = lambda x: -self.g.grafo[x].grau )#len(PermutacaoVerts[x-1]	

		# Do menor para o maior em grau
		elif Metodo == 3:
		
			self.PermutacaoVerts.sort(key = lambda x: self.g.grafo[x].grau )

		self.Decode()

	def Objetivo(self):
		return len(self.coberturaFinal)

	# Transforma uma solucao do espaco de codigo em espaco de solucoes
	def Decode(self):
		
		self.g=deepcopy(self.GrafoOriginal)
		self.coberturaFinal = []
		qtsArestaAtual = 0

		#itera todos os números da lista de permutação
		for idItem in self.PermutacaoVerts:

			#verifica se a lista de adjacencia do vertice em questão está vazia
			if(self.g.grafo[idItem].lista):
			
				#itera a lista de adjacencia do vertice
				for vert in self.g.grafo[idItem].lista:

					#remove a ligação do vertice que se está observando da adjacencia
					self.g.grafo[vert].lista.remove(idItem)
					#aumenta a quantidade de arestas que ja foi coberta
					qtsArestaAtual = qtsArestaAtual+1

				#zera a lista de adjacencia do vertice em questao
				self.g.grafo[idItem] = []
				#coloca o numero do vertice na lista da cobertura final
				self.coberturaFinal.append(idItem)

			#caso a quantidade de arestas coberta for igual a quantidade de arestas do grafo encerra-se o laço inicial que percorre a lista de permutação
			if(self.g.n_arest==qtsArestaAtual):
				break	

		#retorna a lista com os numeros dos vertices que ficaram na cobertura final
		return self.coberturaFinal

	#geração de vizinhos com swap
	def GeraVizinho1(self):

		MaxSwap = int(len(self.PermutacaoVerts) * 0.1)

		if MaxSwap == 0:
			MaxSwap = 1

		for i in range(1,MaxSwap + 1):

			IdFrom = randint(0, len(self.PermutacaoVerts) - 1)
			IdTo   = randint(0, len(self.PermutacaoVerts) - 1)

			aux = self.PermutacaoVerts[IdFrom]
			self.PermutacaoVerts[IdFrom] = self.PermutacaoVerts[IdTo]
			self.PermutacaoVerts[IdTo] = aux
		
		self.Decode()

	'''
	#metodo de gerar do caio que troca duas janelas do vetor do decoder
	def GeraVizinho2(self):

		_qtd = randint(0, (len(self.PermutacaoVerts)) // 2 - 1)
		a = randint(0, len(self.PermutacaoVerts)-1)
		b = randint(0, len(self.PermutacaoVerts)-1)
		# print(_qtd, a, b)

		while (a + _qtd >= len(self.PermutacaoVerts)) or (b + _qtd >= len(self.PermutacaoVerts)):

			a = randint(0, len(self.PermutacaoVerts)-1)

			b = randint(0, len(self.PermutacaoVerts)-1)


		for i in range(0, _qtd):

			self.PermutacaoVerts[a+i], self.PermutacaoVerts[b+i] = self.PermutacaoVerts[b+i], self.PermutacaoVerts[a+i]
		
		self.Decode()
	'''


	#metódo de gerar que "exclui um vertice"
	def GeraVizinho2(self):

		tamCover = self.Objetivo()

		IdSelecionado = randint(0, tamCover)

		sel = deepcopy(self.PermutacaoVerts[IdSelecionado])
		del self.PermutacaoVerts[IdSelecionado]
		self.PermutacaoVerts.append(sel)

		# self.PermutacaoVerts[IdSelecionado],self.PermutacaoVerts[len(self.PermutacaoVerts)-1] = self.PermutacaoVerts[len(self.PermutacaoVerts)-1],self.PermutacaoVerts[IdSelecionado]
		
		self.Decode()


	def __str__(self):

		StrOut = ""
		for vert in self.coberturaFinal:
			StrOut = StrOut + str(vert+1) + ' '

		StrOut = "Objetivo = " + str(len(self.coberturaFinal)) + "\nCobertura final: \n" + StrOut

		return StrOut