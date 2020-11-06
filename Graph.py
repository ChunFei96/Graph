import networkx as nx

import matplotlib.pyplot as plt


class Graph:
    def __init__(self, nodes=0, auto=False, noOfNodes=0, probabilityOfCreateEdges=0, outputFile=0):
        self.G = nx.Graph()
        self.path = None
        if auto==False:
            self.constructGraph(nodes)
        elif auto == True:
            self.autoGraphGenerator(noOfNodes, probabilityOfCreateEdges,outputFile)

    def constructGraph(self, nodes):
        self.G.add_edges_from(nodes, color='#D3D3D3')

    def search(self, start, target):
        self.path = nx.dijkstra_path(self.G, start, target)
        return self.path

    def drawGraph(self):
        try:
            # prevent crashes
            if len(self.G.nodes) < 100:
             plt.subplot(111)
             print("Loading graph...")
             nx.draw(self.G, with_labels=True, font_weight='bold', node_color='r', edge_color='g', width = 3)
             print("Graph successfully loaded!")
             plt.show()
        except Exception as e:
            print(e)

    def autoGraphGenerator(self, noOfNodes, probabilityOfCreateEdges, outputFile):
        try:
            self.G = nx.erdos_renyi_graph(noOfNodes, probabilityOfCreateEdges, seed=None, directed=False)

            # write pair nodes into file
            with open(outputFile, 'w') as writeFile:
                for keyValue in self.G.edges():
                    writeFile.write(str(keyValue[0]) + '\t' + str(keyValue[1]) + '\n')

        except Exception as e:
            print(e)



