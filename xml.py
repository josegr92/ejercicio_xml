#_*_ coding:utf-8 _*_

from lxml import etree

arbol=etree.parse("artesania.xml")
directorios=arbol.getroot()


for directorio in directorios:
	print "Nombre: %s Telf: %s"%(directorio.find("nombre").text,directorio.find("telefono").text)
	print directorio.find("direccion").text

print "\n"
print "Locales de artesanía con la categoria Gijón Card"
for directorio in directorios:
	categorias=directorio.find("categorias")
	for categoria in categorias:
		if categoria.attrib["id"]=="2741": #Como el nombre de la categoria tiene acento da error al convertirlo, entonces lo busco por el id de la categoria.
			print directorio.find("nombre").text