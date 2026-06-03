from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass

    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def eh_conexo_e_simples(self):


        if len(self.vertices)==0:
            return False

        for i in range(len(self.vertices)):

            if len(self.matriz[i][i])>0:
                return False



    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
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

    def alcancabilidade(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        '''
        n = len(self.vertices)

        e = [[1 if len(self.matriz[i][j]) > 0 else 0 for j in range(n)] for i in range(n)]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    e[i][j] = e[i][j] or (e[i][k] and e[k][j])

        return e

    def alcancabilidade_vertice(self,v_rotulo):

        warshall = self.alcancabilidade()

        indice= -1

        for i in range(len(self.vertices)):
            if self.vertices[i].rotulo == v_rotulo:
                indice = i
                break

        alcancaveis = []

        if indice != -1:
            for j in range(len(self.vertices)):
                if warshall[indice][j]==1:
                    alcancaveis.append(self.vertices[j].rotulo)

        return alcancaveis
