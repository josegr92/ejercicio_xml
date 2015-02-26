#_*_ coding:utf-8 _*_

from lxml import etree

for directorio in directorios:
	print "Nombre: %s Telf: %s"%(directorio.find("nombre").text,directorio.find("telefono").text)
	print directorio.find("direccion").text

print "Locales de artesanía con la categoria Gijón Card"
for directorio in directorios:
	categorias=directorio.find("categorias")
	for categoria in categorias:
		if categoria.text=="Gijón Card":
			print directorio.find("nombre").text