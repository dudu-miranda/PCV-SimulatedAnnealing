nome = "vc4"
best = 54

nome_arquivo = "result_"+nome+".txt"
arq_estatistica = "estatistica_"+nome+".txt"

Arq = open(nome_arquivo, "r")
arqsaida = open(arq_estatistica, "w")

arqsaida.write("Metodo inicial\tNumero de reaquecimentos\tMetodo vizinho\tMedia\tMelhor encontrado\tCoeficiente de variacao\tMelhor solução = "+str(best)+"\n")

cont = 0
melhor = 100000
media = 0

for linha in Arq:

	#ignora linha inicial
	if(("SAMAX" in linha)):
		continue

	cont+=1
	conteudo = linha.split("\t")

	if( int(conteudo[5]) < melhor ):
		melhor = int(conteudo[5])

	media = media + int(conteudo[5])

	#zera contador pra nova instancia e salva no arquivo de saida a linha
	if(cont==100):

		if(conteudo[0] == "1"):
			metodo = "Random"
		else:
			metodo = "Guloso"	

		numero_reaquecimentos = conteudo[3]	

		if(conteudo[4] == "1"):
			vizinho = "Swap____"
		else:
			vizinho = "Exclusao"	

		media = media/100

		arqsaida.write(metodo+"\t"+str(numero_reaquecimentos)+"\t"+vizinho+"\t"+str(media)+"\t"+str(melhor)+"\t"+str(melhor/best)+"\n")

		melhor = 100000
		media = 0
		cont = 0


Arq.close()
arqsaida.close()