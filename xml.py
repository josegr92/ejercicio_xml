#_*_ coding:utf-8 _*_

from lxml import etree

for directorio in directorios:
	print "Nombre: %s Telf: %s"%(directorio.find("nombre").text,directorio.find("telefono").text)
	print directorio.find("direccion").text