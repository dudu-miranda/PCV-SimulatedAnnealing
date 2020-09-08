#!/usr/bin/python
# -*- coding: utf-8 -*-

from grafo   import *
from vertice import *
from copy 	 import deepcopy
import       sys

class InputOutput():

	def __init__(self, NomeArquivo):

		self.NomeArquivo = NomeArquivo

		self.n_vert = 0
		self.n_arest = 0
		self.listas = []

		ContaId = 1

		Arq = open(NomeArquivo, "r")

		for linha in Arq:

			Conteudo = linha.split()

			if Conteudo[0] == "e":
				self.listas[int(Conteudo[1])-1].lista.append(int(Conteudo[2])-1)
				self.listas[int(Conteudo[2])-1].lista.append(int(Conteudo[1])-1)


			elif Conteudo[0] == "c":

				continue

			elif Conteudo[0] == "p":
			
				self.n_vert = int(Conteudo[2])
				self.n_arest = int(Conteudo[3])

				i=0;
				while i<self.n_vert:
					vert=Vertice()
					self.listas.append(deepcopy(vert))
					self.listas[i].id = i+1
					i+=1			

		Arq.close()