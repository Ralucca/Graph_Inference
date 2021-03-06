import networkx as nx
import random, sys

class HND():
    def __init__(self, graph, sd):
        self.graph = graph
        random.seed(sd)
        self.result_graph = nx.Graph()
        self.monitor_set = set()

    def pick_start(self,tally):
        temp=list(set(self.graph.nodes()) - self.monitor_set)
        start_node = random.choice(temp)
        self.monitor_set.add(start_node)
        self.result_graph.add_node(start_node)
        tally=0
        return start_node, tally

    def add_neighbors(self, node):
        neighbors = self.graph.neighbors(node)
        for neighbor in neighbors:
            self.result_graph.add_edge(node, neighbor)

    def place_next_monitor(self, node, tally):
        neighbors = self.graph.neighbors(node)
        max_degree, neighbor_list = 0, []
        neighbor_set = set(neighbors) - self.monitor_set
        if len(neighbor_set)< len(set(neighbors))/2:
            next_monitor, tally = self.pick_start(tally)
            return next_monitor,tally
        for neighbor in neighbor_set:
            degree = self.graph.degree(neighbor)
            if degree > max_degree:
                neighbor_list = []
                max_degree = degree
                neighbor_list.append(neighbor)
            elif degree == max_degree and len(neighbor_list) >= 1:
                neighbor_list.append(neighbor)
            else:
                continue

        if neighbor_set:
            next_monitor = random.choice(neighbor_list)
            self.monitor_set.add(next_monitor)
            tally+=1
        else:
            next_monitor, tally = self.pick_start(tally)

        return next_monitor, tally

    def stop(self, allotment):
        if allotment > self.graph.number_of_nodes():
            sys.exit(1)
        if len(self.monitor_set) < allotment:
            return False
        else:
            return True
