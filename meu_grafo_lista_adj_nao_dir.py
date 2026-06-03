from bibgrafo import aresta
from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''

        nao_adjacentes = set()


        lista_vertices = self.vertices


        lista_arestas = self.arestas.values() if type(self.arestas) == dict else self.arestas


        for i in range(len(lista_vertices)):
            for j in range(i + 1, len(lista_vertices)):


                v1_rotulo = lista_vertices[i].rotulo
                v2_rotulo = lista_vertices[j].rotulo

                sao_adjacentes = False


                for aresta in lista_arestas:

                    if (aresta.v1.rotulo == v1_rotulo and aresta.v2.rotulo == v2_rotulo) or \
                            (aresta.v1.rotulo == v2_rotulo and aresta.v2.rotulo == v1_rotulo):
                        sao_adjacentes = True
                        break



                if not sao_adjacentes:
                    par = f"{v1_rotulo}-{v2_rotulo}"
                    nao_adjacentes.add(par)

        return nao_adjacentes


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        lista_arestas = self.arestas.values() if type(self.arestas) == dict else self.arestas


        for aresta in lista_arestas:

            if aresta.v1.rotulo == aresta.v2.rotulo:
                return True

        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''


        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError(f"O vértice {V} não existe no grafo.")

        grau_do_vertice = 0
        lista_arestas = self.arestas.values() if type(self.arestas) == dict else self.arestas

        for aresta in lista_arestas:
            if aresta.v1.rotulo == V and aresta.v2.rotulo==V:
                grau_do_vertice += 2

            elif aresta.v1.rotulo== V or aresta.v2.rotulo == V:
                grau_do_vertice +=1

        return grau_do_vertice

    def altura_arvore(self, raiz_rotulo):

        lista_arestas = self.arestas.values() if type(self.arestas) == dict else self.arestas

        def dfs(vertice_atual, pai):

            maior_altura = -1

            for aresta in lista_arestas:
                vizinho = None

                if aresta.v1.rotulo == vertice_atual:
                    vizinho = aresta.v2.rotulo
                elif aresta.v2.rotulo == vertice_atual:
                    vizinho = aresta.v1.rotulo

                if vizinho is not None:

                    if vizinho != pai:
                        altura = dfs(vizinho, vertice_atual)

                        if altura > maior_altura:
                            maior_altura = altura

            return maior_altura + 1

        return dfs(raiz_rotulo, None)

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''

    def ha_paralelas(self):

        pares_vistos = set()
        lista_arestas = self.arestas.values() if type (self.arestas)== dict else self.arestas

        for aresta in lista_arestas:
            r1 = aresta.v1.rotulo
            r2 = aresta.v2.rotulo

            par = tuple(sorted([r1,r2]))

            if par in pares_vistos:
                return True
            else:
                pares_vistos.add(par)

        return False



    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Ta errado")


        arestas_conectadas = set()

        lista_arestas = self.arestas.values() if type(self.arestas)== dict else self.arestas

        for aresta in lista_arestas:
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V:

                arestas_conectadas.add(aresta.rotulo)

        return arestas_conectadas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        if self.ha_paralelas():
            return False
        if len(self.vertices_nao_adjacentes())>0:
            return False


        return True




    def eh_arvore(self):

        if len(self.vertices)==0:
            return False

        visitados = set()

        def dfs(vertice_atual,pai):
            visitados.add(vertice_atual)
            lista_arestas=self.arestas.values() if type(self.arestas)== dict else self.arestas

            for aresta in lista_arestas:
                vizinho = None

                if aresta.v1.rotulo == vertice_atual:
                    vizinho = aresta.v2.rotulo
                elif aresta.v2.rotulo == vertice_atual:
                    vizinho = aresta.v1.rotulo


                if vizinho is not None:

                    if vizinho not in visitados:
                        if dfs(vizinho,vertice_atual):
                            return True


                    elif vizinho != pai:
                        return True

            return False

        vertice_inicial = self.vertices[0].rotulo
        tem_ciclo = dfs(vertice_inicial,None)

        if tem_ciclo or len(visitados)!= len(self.vertices):
            return False

        folhas = []
        for v in self.vertices:
            if self.grau(v.rotulo)==1:
                folhas.append(v.rotulo)

        return folhas
