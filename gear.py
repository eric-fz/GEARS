# Import necessary libraries
import numpy as np
import scipy.sparse as sp
# Set the number of nodes in the graph
num_nodes = 10
# Set edge density
edge_density = 0.1

# Define the number of edge features and node features
num_edge_features = 7
num_node_features = 3

connected = False
while not connected:
    # Instantiate an empty connectivity matrix with the desired shape
    connectivity_matrix = sp.rand(num_nodes, num_nodes, density=edge_density)
    connectivity_matrix = np.array(connectivity_matrix.todense())
    #Fill diagonals with 0s
    np.fill_diagonal(connectivity_matrix,0)
    # Make matrix symmetric
    connectivity_matrix = np.triu(connectivity_matrix) + np.triu(connectivity_matrix, 1).T

    # ensure connectivity
    _, components = sp.csgraph.connected_components()
    if components[0] == components[-1]:
        connected = True

# Loop through the edges in the graph and assign their features
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j & connectivity_matrix[i,j,0] == 1:
            # Define the edge features as desired
            m = #module
            t1 = #teeth 1
            t2 = #teeth 2
            b = #gear thickness
            alpha = #working contact angle
            x1 = #profile shift 1
            x2 = #profile shift 2
            # Increase dimension of connectivity matrix
            # Assign the edge features to the connectivity matrix
            np.expand_dims(connectivity_matrix, axis = 0)
            connectivity_matrix[i, j, 1] = m
            connectivity_matrix[i, j, 2] = t1
            connectivity_matrix[i, j, 3] = t2
            connectivity_matrix[i, j, 4] = b
            connectivity_matrix[i, j, 5] = alpha
            connectivity_matrix[i, j, 6] = x1
            connectivity_matrix[i, j, 7] = x2


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


