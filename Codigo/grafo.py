#!/usr/bin/python
# -*- coding: utf-8 -*-

class Grafo():

	def __init__(self,vertices,n_vert,n_arest):

		self.n_vert=n_vert
		self.n_arest=n_arest
		self.grafo=vertices
		self.atualizaGraus()

	def atualizaGraus(self):
		for i in range(1,len(self.grafo)):
			self.grafo[i].atualizaGrau()


	def __str__(self):
		
		#return s
		s=""
		for i in range(1,len(self.grafo)):
			s=s+str(self.grafo[i])
		return "N. Vertices = " + str(self.n_vert) + "\nN. Arestas = " + str(self.n_arest) + "\n Grafo:\n" + s		