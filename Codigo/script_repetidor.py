
from main1 import *

nome_arquivo="vc4"
nome_arquivo_entrada = nome_arquivo+".txt"
nome_arquivo_saida	 = "result_"+nome_arquivo+".txt"

f=open(nome_arquivo_saida,'w')
f.write("Nome_arquivo\tTemperatura_inicial\tSAMAX\tQtd_Reaquecimentos\tMetodo_Vizinho\tFunção_Objetivo\tIteração\n")
temp_inicial = 100
Samax = 10

for i in range(1,3):
	metodo_inicial = i
	for j in range(7,15,7):
		n_reaquecer = j
		for k in range(1,3):
			metodo_vizinho = k
			for l in range(1,101):
				iter = l
				string =  main1(metodo_inicial,n_reaquecer,metodo_vizinho,nome_arquivo_entrada,temp_inicial,Samax)
				string += str(iter)+"\n"
				f.write(string)

f.close()
																				