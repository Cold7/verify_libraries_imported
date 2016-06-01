from os import listdir 

libs=[]
for fichero in listdir("."):
	if fichero!="necessaryLibs.py":
		File=open(fichero)
		for line in File:
			if "import" in line:
				if "#" in line:
					Line=line[:-1]
					l=Line[0:((Line.index("#")))]
					flag=0
					for char in l:
						if char!=" ":
							flag=1
							break
					if len(l)>0:
						flag=1
					
					if l not in libs and flag==1:
						libs.append(l)
				else:
					if line[0:-1] not in libs:
						libs.append(line[:-1])
		File.close()
for lib in libs:
	print lib
