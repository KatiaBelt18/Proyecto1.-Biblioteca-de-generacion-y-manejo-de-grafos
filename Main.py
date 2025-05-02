from Modelos import *
'''
#Generar modelo Gn,m de Erdös y Rényi
g = grafo_ErdosRenyi(500,499)
g.mostrar_grafo()
g.exportar_a_gv("Grafo_ErdosRenyi_500.gv")
'''

'''
#Generar modelo Gn,p de Gilbert
g = grafo_Gilbert(500,15)
g.mostrar_grafo()
g.exportar_a_gv("Grafo_Gilbert_500.gv")
'''

'''
#Generar modelo Gn Dorogovtsev-Mendes
g = grafo_DoroMendes(500)
g.mostrar_grafo()
g.exportar_a_gv("Grafo_DoroMendes_500.gv")
'''

'''
#Generar modelo Gm,n de malla
g = grafo_Malla(25,20)
g.mostrar_grafo()
g.exportar_a_gv("Grafo_Malla_500.gv")
'''

'''
#Generar variante del modelo Gn,d Barabási-Albert
g = grafo_BarabasiAlbert(50,5)
g.mostrar_grafo()
g.exportar_a_gv("Grafo_Barabasi_50.gv")
'''


#Generar modelo Gn,r geográfico simple
g = grafo_Geografico(200,0.2)
g.mostrar_grafo()
g.exportar_a_gv("Grafo_Geografico_200.gv")





