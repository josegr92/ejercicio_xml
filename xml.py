#_*_ coding:utf-8 _*_

from lxml import etree

arbol=etree.parse("artesania.xml")
directorios=arbol.getroot()

for directorio in directorios:
	print "Nombre: %s Telf: %s"%(directorio.find("nombre").text,directorio.find("telefono").text)
	print directorio.find("direccion").text

print "\n"
cont=0
print "Locales de artesanía con la categoria Gijón Card"
for directorio in directorios:
	categorias=directorio.find("categorias")
	for categoria in categorias:
		if categoria.attrib["id"]=="2741": #Como el nombre de la categoria tiene acento da error al convertirlo, entonces lo busco por el id de la categoria.
			print directorio.find("nombre").text
		if categoria.text=="Turismo":
			cont=cont+1

print "\n"
print "Hay %i locales con la categoria Turismo"%cont

print "\n"
print "Identificadores de los locales de artesania"
for directorio in directorios:
	print "Identificador: %s"%directorio.find("identificador").text

ident=raw_input("Introduce el identificador del local: ")
for directorio in directorios:
	if directorio.find("identificador").text==ident:
		print "Nombre: %s"%directorio.find("nombre").text