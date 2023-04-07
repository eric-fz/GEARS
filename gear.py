# Import necessary libraries
import numpy as np
import scipy.sparse as sp
# Set the number of nodes in the graph
num_nodes = 5
# Set edge density
edge_density = 0.1

# Define the number of edge features and node features
num_edge_features = 7
num_node_features = 3

connected = False
while not connected:
    # Instantiate a connectivity matrix with the desired shape
    connectivity_matrix = sp.random(num_nodes, num_nodes, density=edge_density)
    connectivity_matrix = np.array(connectivity_matrix.todense())
    #Fill diagonals with 0s
    np.fill_diagonal(connectivity_matrix,0)
    # Make matrix symmetric
    connectivity_matrix = np.triu(connectivity_matrix) + np.triu(connectivity_matrix, 1).T

    # ensure connectivity
    _, components = sp.csgraph.connected_components(connectivity_matrix, directed=False)
    if components[0] == components[-1]:
        connected = True

connectivity_matrix[connectivity_matrix != 0] = 1

# Instantiate empty list of edge matrixes
E_list = []

# Define function to add edge feature matrix to list
def addToMatrix(loc, scale, size):
    edge_matrix = np.copy(connectivity_matrix)
    for i in range(num_nodes):
        for j in range(num_nodes):
            edge_matrix[i,j] *= np.random.normal(loc=loc, scale=scale, size=size)
    E_list.append(edge_matrix)

# module in
addToMatrix(2.0, 1.0, None)
# teeth 1
addToMatrix(30.0, 10.0, None)
# teeth 2
addToMatrix(30.0, 10.0, None)
# gear thickness
# working contact angle
print(E_list)

# Instantiate an empty node feature matrix with the desired shape
node_feature_matrix = np.zeros((num_nodes, num_node_features))

# # Loop through the nodes in the graph and assign their features
# for i in range(num_nodes):
#     # Define the node features as desired
#     x = #x position
#     y = #y position
#     z = #z position

#     # Assign the node features to the node feature matrix
#     node_feature_matrix[i, 0] = x
#     node_feature_matrix[i, 1] = y
#     node_feature_matrix[i, 2] = z


