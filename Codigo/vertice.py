#!/usr/bin/python
# -*- coding: utf-8 -*-

class Vertice():

	def __init__(self):

		self.lista = []
		self.grau  = 0
		self.id = 0

	def __str__(self):
		
		return "Grau do vert " + str(self.id) + " =" + str(self.grau) + " Lista de adj - " + str(self.lista) + "\n"

	def atualizaGrau(self):
		self.grau=len(self.lista)			