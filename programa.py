import sys
#sys.argv = ["programa.py", "tarefas.txt"]
if (len(sys.argv) !=2):
	print("Execute \npython programa.py nome_do_arquivo")
else:
	try:
		arquivo = open(sys.argv[1], "r")
		while True:
			t = arquivo.readline()
			print(t, end="")
			if (t == ""):
				break
		arquivo.close()
	except:
		print("Arquivo não existe.")
