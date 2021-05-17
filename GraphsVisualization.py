import networkx as nx
import matplotlib.pyplot as plt

G1=nx.DiGraph()


G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
print(G1.nodes)
G1.add_edge(0, 1, weight = 5.0)
G1.add_edge(0, 2, weight = 3.0)
G1.add_edge(0, 4, weight = 2.0)
G1.add_edge(1, 2, weight = 2.0)
G1.add_edge(1, 3, weight = 6.0)
G1.add_edge(2, 1, weight = 1.0)
G1.add_edge(2, 3, weight = 2.0)
G1.add_edge(4, 1, weight = 6.0)
G1.add_edge(4, 2, weight = 10.0)
import networkx as nx
import matplotlib.pyplot as plt

G1=nx.DiGraph()

G1.add_node(0)
G1.add_node(1)
G1.add_node(2)
G1.add_node(3)
G1.add_node(4)
print(G1.nodes)
G1.add_edge(0, 1, weight = 5.0)
G1.add_edge(0, 2, weight = 3.0)
G1.add_edge(0, 4, weight = 2.0)
G1.add_edge(1, 2, weight = 2.0)
G1.add_edge(1, 3, weight = 6.0)
G1.add_edge(2, 1, weight = 1.0)
G1.add_edge(2, 3, weight = 2.0)
G1.add_edge(4, 1, weight = 6.0)
G1.add_edge(4, 2, weight = 10.0)
G1.add_edge(4, 3, weight = 4.0)
G1.nodes[0]['pos'] = (0,4)
G1.nodes[1]['pos'] = (4,0)
G1.nodes[2]['pos'] = (2,-4)
G1.nodes[3]['pos'] = (-2,-4)
G1.nodes[4]['pos'] = (-4,0)
def cizim():
    for a in range(4):
        if(a == 2):
            a +=1
            node_pos=nx.get_node_attributes(G1,'pos')
            arc_weight=nx.get_edge_attributes(G1,'weight')
            sp = nx.dijkstra_path(G1,source = 0, target = a+1 )
            red_edges = list(zip(sp, sp[1:]))
            node_col = ['white' if not node in sp else 'red' for node in G1.nodes()]
            edge_col = ['black' if not edge in red_edges else 'red' for edge in G1.edges()]
            nx.draw_networkx(G1, node_pos, node_color=node_col, node_size=450)
            nx.draw_networkx_edges(G1, node_pos, edge_color=edge_col)
            nx.draw_networkx_edge_labels(G1, node_pos, edge_labels=arc_weight)
            plt.axis('off')
            plt.show()


def uzaklikHesabi():
    for i in range(G1.number_of_nodes()-2):
        sp = nx.dijkstra_path(G1,source = 4, target = i+1)
        print(i+1,". node the shortest path ->",sp)


cizim()
uzaklikHesabi()

G1.remove_node(3)
G1.remove_edges_from(([1,3],[2,3],[4,3]))

print("Node 3 REMOVE")

cizim()
uzaklikHesabi()







