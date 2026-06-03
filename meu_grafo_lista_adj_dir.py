import queue

from bibgrafo.grafo_lista_adj_dir import GrafoListaAdjacenciaDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaDirecionado):


    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        pass # Apague essa instrução e inicie seu código aqui

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau_entrada(self, V=''):
        '''
        Provê o grau de entrada do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau de saída do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        pass

    def ha_ciclo(self):

        cores = {}
        for v in self.vertices:
            cores[v.rotulo] = 'branco'
        def dfs(v_rotulo):
            cores[v_rotulo] = 'cinza'

            for aresta in self.arestas.values():
                origem = aresta.v1.rotulo
                destino = aresta.v2.rotulo

                if origem == v_rotulo:
                    if cores[destino] == 'branco':
                        if dfs(destino):
                            return True
                    elif cores[destino] == 'cinza':
                        return True

            cores[v_rotulo] = 'preto'
            return False

        for v in self.vertices:
            if cores[v.rotulo] == 'branco':
                if dfs(v.rotulo):
                    return True


        return False


    def eh_bipartido(self):

        vertices = list(self.vertices)
        espera =[]
        cores = {}
        atual,vizinho = None,None

        for v_obj in vertices:
            v = v_obj.rotulo

            if v not in cores:
                cores[v]=1
                espera.append(v)

                while (len(espera)>0):
                    atual= espera.pop(0)

                    for a in self.arestas:
                        if self.arestas[a].v1.rotulo==atual:
                            vizinho = self.arestas[a].v2.rotulo
                        elif self.arestas[a].v2.rotulo == atual:
                            vizinho = self.arestas[a].v1.rotulo
                        else:
                            continue

                        if vizinho not in cores:

                            cores[vizinho]= cores[atual]*-1
                            espera.append(vizinho)

                        elif cores[vizinho]==cores[atual]:
                            return False

        return True

    def menor_caminho(self,v1,vf):

        import heapq

        if not self.existe_rotulo_vertice(v1) or not self.existe_rotulo_vertice(vf):
            raise VerticeInvalidoError

        distancias = {v.rotulo:float("inf") for v in self.vertices}

        distancias[v1] = 0
        predecessores={}
        fila = [(0,v1)]

        while fila:
            distancia_atual,vertice_atual = heapq.heappop(fila)
            if distancia_atual> distancias[vertice_atual]:
                continue

            if vertice_atual == vf:
                break

            for a in self.arestas.values():
                if a.v1.rotulo == vertice_atual:
                    vizinho = a.v2.rotulo
                    peso = a.peso

                    nova_distancia = distancia_atual + peso

                    if nova_distancia <distancias[vizinho]:
                        distancias[vizinho] = nova_distancia
                        heapq.heappush(fila,(nova_distancia,vizinho))
                        predecessores[vizinho] = vertice_atual

        if distancias[vf]== float("inf"):
            return float("inf"),[]


        menor_caminho = []

        vertice = vf

        while vertice != v1:
            menor_caminho.append(vertice)
            vertice = predecessores[vertice]

        menor_caminho.append(v1)
        menor_caminho.reverse()

        return distancias[vf],menor_caminho
