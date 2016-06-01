from os import listdir 

libs=[]
for fichero in listdir("."):
	if fichero!="necessaryLibs.py":
		File=open(fichero)
		for line in File:
			if "import" in line:
				if line not in libs:
					libs.append(line[:-1])
		File.close()
for lib in libs:
	print lib
