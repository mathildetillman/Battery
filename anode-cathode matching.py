from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching

anodes =  [75.10, 75.57, 75.89, 77.60, 75.90, 74.91, 75.08, 71.39, 73.96, 78.90, 72.20, 79.79, 71.75, 74.98, 79.77, 71.25, 74.52, 75.29, 71.73, 72.38, 72.51, 74.19, 77.94, 70.81, 70.25, 68.46, 68.09, 67.40] 
cathodes = [59.306576, 59.188624, 57.281216, 56.610752, 55.971328, 55.023056, 54.588496, 54.267232, 54.143072, 53.956832, 53.896304, 53.71472, 53.713168, 53.63712, 53.55952, 53.557968 ,53.405872 ,53.31896, 53.030288, 52.932512, 52.800592, 52.788176, 52.192208, 59.306576, 52.192208]

def getMatrix(anodes, cathodes):
    """
    Create matrix representing possible matches between anodes and cathodes based on NP ratio

    :param anodes: list of anodes
    :param cathodes: list of cathodes
    :return: matrix of possible matches between anodes and cathodes
    """ 

    matrix = []
    for anode in anodes:
        anodeList = []
        for cathode in cathodes:
            NP_ratio = anode/cathode
            if 1.1 <= NP_ratio <= 1.2:
                # Possible match 
                anodeList.append(1)   
            else:
                anodeList.append(0) 
        matrix.append(anodeList)
    return matrix


def getCouples(anodes, cathodes, matching):
    """
    Create touples of the anode-cathode matching pairs

    :param anodes: list of anodes
    :param cathodes: list of cathodes
    :param matching: list where index matches anodes index, and value matches cathode index
    :return: list of touples with matches anode-cathode pairs
    """ 

    couples = []
    for index, anode in enumerate(anodes):
        cathodeIndex = matching[index]
        if cathodeIndex != -1:
            cathode = cathodes[cathodeIndex]
            couples.append((anode, cathode))
    return couples


def main():

    print("hallo")
    # Create graph
    graph = csr_matrix(getMatrix(anodes, cathodes))

    # Create list which contains the index of cathodes that are matched with the anodes
    indexMatching = maximum_bipartite_matching(graph, perm_type='column')
    print("Indexes: ", indexMatching)

    # Get the anode-cathode pairs
    couples = getCouples(anodes, cathodes, indexMatching)
    print("Anode-cathode matches: ", couples)



main()




