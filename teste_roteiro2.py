import unittest
from bibgrafo.grafo_errors import VerticeInvalidoError
from meu_grafo_lista_adj_dir import MeuGrafo as GrafoListaDir
from meu_grafo_lista_adj_nao_dir import MeuGrafo as GrafoListaNaoDir
from meu_grafo_matriz_adj_dir import MeuGrafo as GrafoMatrizDir


class TestGrafoRoteiro3(unittest.TestCase):





    def test_alcancabilidade_vertice(self):

        g = GrafoMatrizDir()

        for letra in ['A','B','C','D']:
            g.adiciona_vertice(letra)

        g.adiciona_aresta("a1","A","B",1)
        g.adiciona_aresta("a2","B","C",1)

        self.assertCountEqual(g.alcancabilidade_vertice("A"),["B","C"])

        self.assertCountEqual(g.alcancabilidade_vertice("B"),['C'])

        self.assertCountEqual(g.alcancabilidade_vertice("C"),[])
        self.assertCountEqual(g.alcancabilidade_vertice("D"),[])


    def test_altura_arvore(self):

       g = GrafoListaNaoDir()

       for letra in ["A","B","C","D"]:
           g.adiciona_vertice(letra)

       g.adiciona_aresta("a1","A","B",1)
       g.adiciona_aresta("a2","B","C",1)
       g.adiciona_aresta("a3","C","D",1)

       self.assertEqual(g.altura_arvore("A"),4)
       self.assertEqual(g.altura_arvore("B"),2)








    def test_vertices_isolados(self):

        g = GrafoListaDir()

        for letra in ['A','B','C','D']:
            g.adiciona_vertice(letra)

        g.adiciona_aresta('a1',"A","B",1)

        resultado = g.vertices_isolados()

        self.assertCountEqual(resultado,['C','D'])

        g.adiciona_aresta("a2","B","C",1)
        self.assertCountEqual(g.vertices_isolados(),["D"])



    def test_conjuntos_bipartidos(self):
        g = GrafoListaDir()

        for letra in ['A','B','C','D']:
            g.adiciona_vertice(letra)

        g.adiciona_aresta("p1","A","B",1)
        g.adiciona_aresta("p2","B","C",1)
        g.adiciona_aresta("p3","C","D",1)
        g.adiciona_aresta("p4","D","A",1)

        resultado = g.conjuntos_bipartidos()


        self.assertIsNotNone(resultado)

        grupo_1, grupo_2 = resultado

        self.assertTrue({'A','C'} in [grupo_1,grupo_2])
        self.assertTrue({'B', 'D'} in [grupo_1, grupo_2])







    # Teste para achar os ciclos do grafo

    def test_ha_ciclo(self):
        g = GrafoListaDir()

        for letra in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            g.adiciona_vertice(letra)

        #Criei um grafo só para esse teste

        g.adiciona_aresta("a1", "A", "B", 1)
        g.adiciona_aresta("a2", "B", "C", 1)
        g.adiciona_aresta("a3", "C", "D", 1)
        g.adiciona_aresta("a4", "D", "E", 1)
        g.adiciona_aresta("a5", "E", "F", 1)
        g.adiciona_aresta("a6", "F", "G", 1)
        g.adiciona_aresta("a7", "G", "H", 1)

        #O grafo que eu criei ele não tem ciclos
        self.assertFalse(g.ha_ciclo())

        #Com esse novo aresta passa a ter um ciclo
        g.adiciona_aresta("a8", "H", "C", 1)
        self.assertTrue(g.ha_ciclo())

    # Teste para descobrir se é arvore
    def test_eh_arvore(self):
        g_arvore = GrafoListaNaoDir()

        #Primeira situação
        for letra in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            g_arvore.adiciona_vertice(letra)

        g_arvore.adiciona_aresta("a1", "A", "B", 1)
        g_arvore.adiciona_aresta("a2", "A", "C", 1)
        g_arvore.adiciona_aresta("a3", "B", "D", 1)
        g_arvore.adiciona_aresta("a4", "B", "E", 1)
        g_arvore.adiciona_aresta("a5", "C", "F", 1)
        g_arvore.adiciona_aresta("a6", "C", "G", 1)

        resultado = g_arvore.eh_arvore()
        print(f"\nLista de folhas encontrada: {resultado}")
        self.assertCountEqual(resultado, ['D', 'E', 'F', 'G'])


        #Segunda Situação
        g_ciclo = GrafoListaNaoDir()

        for letra in ['X', 'Y', 'Z', 'W']:
            g_ciclo.adiciona_vertice(letra)

        g_ciclo.adiciona_aresta("c1", "X", "Y", 1)
        g_ciclo.adiciona_aresta("c2", "Y", "Z", 1)
        g_ciclo.adiciona_aresta("c3", "Z", "W", 1)
        g_ciclo.adiciona_aresta("c4", "W", "X", 1)

        self.assertFalse(g_ciclo.eh_arvore())

        #Terceira situação

        g_desconexo = GrafoListaNaoDir()

        for letra in ['M', 'N', 'O', 'P', 'Q']:
            g_desconexo.adiciona_vertice(letra)

        g_desconexo.adiciona_aresta("d1", "M", "N", 1)
        g_desconexo.adiciona_aresta("d2", "N", "O", 1)
        g_desconexo.adiciona_aresta("d3", "P", "Q", 1)

        self.assertFalse(g_desconexo.eh_arvore())


    # Teste para saber se é bipartido
    def test_eh_bipartido(self):
        g_par = GrafoListaDir()

        for letra in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            g_par.adiciona_vertice(letra)

        g_par.adiciona_aresta("p1", "A", "B", 1)
        g_par.adiciona_aresta("p2", "B", "C", 1)
        g_par.adiciona_aresta("p3", "C", "D", 1)
        g_par.adiciona_aresta("p4", "D", "E", 1)
        g_par.adiciona_aresta("p5", "E", "F", 1)
        g_par.adiciona_aresta("p6", "F", "G", 1)
        g_par.adiciona_aresta("p7", "G", "H", 1)
        g_par.adiciona_aresta("p8", "H", "A", 1)

        self.assertTrue(g_par.eh_bipartido())

        g_impar = GrafoListaDir()

        for letra in ['M', 'N', 'O', 'P', 'Q', 'R', 'S']:
            g_impar.adiciona_vertice(letra)

        g_impar.adiciona_aresta("i1", "M", "N", 1)
        g_impar.adiciona_aresta("i2", "N", "O", 1)
        g_impar.adiciona_aresta("i3", "O", "P", 1)
        g_impar.adiciona_aresta("i4", "P", "Q", 1)
        g_impar.adiciona_aresta("i5", "Q", "R", 1)
        g_impar.adiciona_aresta("i6", "R", "S", 1)
        g_impar.adiciona_aresta("i7", "S", "M", 1)

        self.assertFalse(g_impar.eh_bipartido())

    # Achar a matriz de alcançabilidade
    def test_alcancabilidade(self):
        g_matriz = GrafoMatrizDir()


        for letra in ['A', 'B', 'C', 'D']:
            g_matriz.adiciona_vertice(letra)

        #agente cria o caminho
        g_matriz.adiciona_aresta("m1", "A", "B", 1)
        g_matriz.adiciona_aresta("m2", "B", "C", 1)
        g_matriz.adiciona_aresta("m3", "C", "D", 1)


        matriz_resultado = g_matriz.alcancabilidade()


        self.assertEqual(matriz_resultado[0], [0, 1, 1, 1])

        self.assertEqual(matriz_resultado[1], [0, 0, 1, 1])

        self.assertEqual(matriz_resultado[2], [0, 0, 0, 1])

        self.assertEqual(matriz_resultado[3], [0, 0, 0, 0])

    # Achar o menor caminho
    def test_menor_caminho(self):
        g = GrafoListaDir()

        for letra in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
            g.adiciona_vertice(letra)

        g.adiciona_aresta("a1", 'A', 'B', 2)
        g.adiciona_aresta("a2", 'A', 'C', 6)
        g.adiciona_aresta("a3", 'B', 'C', 2)
        g.adiciona_aresta("a4", 'B', 'D', 6)
        g.adiciona_aresta("a5", 'C', 'E', 2)
        g.adiciona_aresta("a6", 'E', 'D', 1)
        g.adiciona_aresta("a7", 'D', 'F', 2)
        g.adiciona_aresta("a8", 'E', 'G', 4)
        g.adiciona_aresta("a9", 'F', 'H', 3)
        g.adiciona_aresta("a10", 'G', 'H', 1)

        custo, rota = g.menor_caminho("A", "H")
        self.assertEqual(custo, 11)
        self.assertEqual(rota, ['A', 'B', 'C', 'E', 'G', 'H'])

        custo_isolado, rota_isolada = g.menor_caminho("A", "I")
        self.assertEqual(custo_isolado, float("inf"))
        self.assertEqual(rota_isolada, [])

        with self.assertRaises(VerticeInvalidoError):
            g.menor_caminho("A", "Z")

        with self.assertRaises(VerticeInvalidoError):
            g.menor_caminho("Z", "H")