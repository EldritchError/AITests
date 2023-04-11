import numpy as np
import time
import codon

class NumpyNetwork:
    def sigmoid(x):
        return(1/(1 + np.exp(-x)))
    
    def __init__(self, neuron_counts=list):
        self.neuron_count = sum(n for n in neuron_counts)
        self.layer_count = neuron_counts.__len__()
        
        # ToDo: randomizer function
        np.random.seed(444)
        
        self.layers = []
        
        for neuron_count in neuron_counts:
            self.layers.append(np.random.random(neuron_count * 2).reshape(2, neuron_count))
                
        print(self.layers)
        
        

@codon.jit     
def codon_array():
    def codon_init(neuron_counts=list):
        neuron_count = sum(n for n in neuron_counts)
        layer_count = neuron_counts.__len__()
        
        
test_structure = [5, 3, 3, 2]
test = NumpyNetwork(test_structure)