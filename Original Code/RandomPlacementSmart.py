#Trying to make the random placement.

#Random Placement Smart
import networkx as nx
import random
import sys
#import copy

#Algorithm: Random Placement Smart (RPS)
#
# Randomly places nodes without replacement.
#   (i.e. can't pick a node with a monitor)

class Alg():
    def __init__(self, graph, sd):
        self.graph = graph
        random.seed(sd)
        self.result_graph = nx.Graph()
        self.monitor_set = set()
        self.num_monitors = 0

    #public method. Picks a random node that hasn't been a monitor yet.
    #returns the node number
    def pick_start(self):
        start_node = random.choice([x for x in self.graph.nodes() if x not in self.monitor_set])
        self.monitor_set.add(start_node)
        #self.result_graph.add_node(start_node)
        return start_node
    
    #public method. adds all edges (in NetworkX adding an edge adds the nodes if not alread there)
    #from the node to all of its neighbors
    def add_neighbors(self, node):
        neighbors = self.graph.neighbors(node)
        for neighbor in neighbors:
            self.result_graph.add_edge(node, neighbor)
   
    #public method. 
    # Simply calls the 'pick start' method, which randomly places a monitor
    # without replacement. Provided to support standard algorithm interfacing.
    def place_next_monitor(self, node, prob):              
        return self.pick_start()
        
    #public method. Returns true if we have place all the monitors
    #we have available to us, else returns false
    def stop(self, allotment):
        #Probably obsolete.
        if allotment > self.graph.number_of_nodes():
            ##print "Error, cannot have more than", self.graph.number_of_nodes(), "monitors!"
            sys.exit(1)

        if len(self.monitor_set) < allotment:
            return False
        else:
            return True