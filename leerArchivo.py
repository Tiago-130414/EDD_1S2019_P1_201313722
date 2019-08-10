import csv

class lector:
    def leer(self,listaCircular = object):
        archivo = 'prueba.csv'
        with open (archivo) as File:
            lee = csv.reader(File, delimiter=',',quotechar=',',quoting=csv.QUOTE_MINIMAL)
            for col in lee:
               cad = str(col).replace(']',"")
               cad = cad.replace("'","")
               cad = cad.replace("[","")
               if(cad!="Usuario"):
                    listaCircular.agregarFinal(str(cad))
                    cad=""
                