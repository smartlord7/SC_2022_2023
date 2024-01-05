import matplotlib
import networkx as nx
import networkx.algorithms.community as c
import matplotlib.pyplot as plt


def load_graph(path, delim=" "):
    g = nx.Graph()
    with open(path, 'r') as file:
        for line in file:
            nodes = line.strip().split(delim)
            g.add_edge(nodes[0], nodes[1])

    return g


def show_betwenness_centrality(g, top_n_nodes):
    betweenness_centrality = nx.betweenness_centrality(g)
    betweenness_centrality = sorted(betweenness_centrality.items(),
                                    key=lambda x: x[1], reverse=True)
    i = 1
    for pair in betweenness_centrality:
        node = pair[0]
        centrality = pair[1]

        print("#%d - Node %s: %.4f" % (i, node, centrality))
        i += 1

        if i > top_n_nodes:
            break


def show_communities(g):
    comm = c.louvain_communities(g)

    pos = nx.spring_layout(g)
    size = float(len(comm))
    count = 0.
    for com in comm:
        count += 1.
        list_nodes = [nodes for nodes in comm
                      if comm[nodes] == com]
        nx.draw_networkx_nodes(g, pos, list_nodes, node_size=20,
                               node_color=str(count / size))

    nx.draw_networkx_edges(g, pos, alpha=0.5)
    plt.show()


def show_graph_stats(g: nx.Graph, top_n_nodes=10):
    n_nodes = len(g.nodes)

    n_edges = len(g.edges)

    degrees = dict(g.degree()).values()
    bins = max(degrees) - min(degrees)
    plt.hist(degrees, bins=bins)
    plt.title('Degree distribution')
    plt.xlabel('Degree')
    plt.ylabel('Occurrences')
    plt.show()

    avg_degree = sum(degrees) / n_nodes

    max_n_nodes = n_nodes * (n_nodes - 1) / 2
    density = n_nodes / max_n_nodes

    eccentricity = 0 #nx.eccentricity(g)

    diameter = 0 #nx.diameter(g, e=eccentricity)

    radius = 0 #nx.radius(g, e=eccentricity)

    print('Number of nodes: %d\n'
          'Number of edges: %d\n'
          'Average degree: %.4f\n'
          'Density: %.4f\n'
          'Eccentricity: %s\n'
          'Diameter: %d\n'
          'Radius: %d\n' % (n_nodes, n_edges, avg_degree,
                            density, str(eccentricity), diameter, radius))

    print('Betweenness centrality from the top %d nodes: ' % top_n_nodes)

    #show_betwenness_centrality(g, top_n_nodes)

    show_communities(g)


def main():
    matplotlib.use('TkAgg')
    PATH_DATA = 'data/'
    EXTENSION_DATA = '.txt'
    PATH_FACEBOOK_NETWORK = PATH_DATA + 'facebook_combined' + EXTENSION_DATA

    g = load_graph(PATH_FACEBOOK_NETWORK)
    # nx.draw_spectral(g, with_labels=True)
    show_graph_stats(g)


if __name__ == '__main__':
    main()
