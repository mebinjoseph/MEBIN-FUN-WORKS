import graphviz
graph=graphviz.Digraph(format='svg')

#Creates a node IPCC
graph.node('IPCC', shape='oval', style="filled", color="#ADD8E6", URL="https://www.ipcc.ch/report")

AR=['AR1', 'AR2', 'AR3', 'AR4', 'AR5', 'AR6'] #Creates nodes AR 1-6 [Assessment Reports 1-6]
for node in AR:                               #For displaying the properties of AR 1-6 [Assessment Reports 1-6]
    graph.node(node, node, shape='parallelogram', style="filled", color="#90EE90")

for node in AR: #Connects edge IPCC to node i.e., AR [Assessment Reports]
    graph.edge('IPCC', node, style="dotted")

Wg=['Wg1', 'Wg2', 'Wg3'] # Creates nodes Wg1-3 [Working group 1-3]
SynR=['SynR']            # Creates a nodeSynR [Synthesis Report]
for node in Wg: #For displaying the properties and URL of Working Groups 1-3
    if node == "Wg1":
        graph.node(node, node, shape='diamond', style='filled', color="#FFF4EO", URL = "https://www.ipcc.ch/report/ar6/wg1/")
    elif node == "Wg2":
        graph.node(node, node, shape='diamond', style='filled', color="#FFF4EO", URL = "https://www.ipcc.ch/report/ar6/wg2/")
    else:
        graph.node(node, node, shape='diamond', style='filled', color="#FFF4EO", URL = "https://www.ipcc.ch/report/ar6/wg3/")

for node in Wg:             #Connects edge AR6 to Wg i.e., Working Groups
    graph.edge('AR6', node, style="dotted")

for node in SynR:           #For displaying the properties and URL of Synthesis Report
    if node == 'SynR':
        graph.node(node, node, shape='diamond', style='filled', color="#FFF4EO", URL= "https://www.ipcc.ch/report/ar6/syr/")

for node in SynR:           #Connects edge AR6 to SynR i.e., Synthesis Report
    graph.edge('AR6', node, style="dotted")

# Creates Chapter 1-12 & Atlas in Working Group 1
Wg1_Ch=['Ch1_1', 'Ch1_2', 'Ch1_3', 'Ch1_4', 'Ch1_5', 'Ch1_6', 'Ch1_7', 'Ch1_8', 'Ch1_9', 'Ch1_10', 'Ch1_11', 'Ch1_12', 'Atlas']
for node in Wg1_Ch: #For displaying the properties and URL of Chapters of Working Group 1
    if node=='Ch1_1':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-1/")
    elif node=='Ch1_2':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-2/")
    elif node=='Ch1_3':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-3/")
    elif node=='Ch1_4':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-4/")
    elif node == 'Ch1_5':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL="https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-5/")
    elif node=='Ch1_6':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-6/")
    elif node=='Ch1_7':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/")
    elif node=='Ch1_8':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-8/")
    elif node == 'Ch1_9':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL="https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-9/")
    elif node=='Ch1_10':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-10/")
    elif node=='Ch1_11':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-11/")
    elif node=='Ch1_12':
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL= "https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-12/")
    else:
        graph.node(node, node, shape='cylinder', style='filled', color="#E6E6FA", URL="https://www.ipcc.ch/report/ar6/wg1/chapter/atlas/")

for node in Wg1_Ch:                 #Connects edge Chapter 1-12 & Atlas to Working Group 1
    graph.edge('Wg1', node, style="dotted")

SubcategoryWg2=['Chapters', 'Cross_Chapters']   #Creates nodes Chapter & Cross_Chapters for Working Group 2
for node in SubcategoryWg2:                     #For displaying the properties of Chapter & Cross_Chapters for Working Group 2
    graph.node(node, node, shape='hexagon', style='filled', color="#AFEEEE")

for node in SubcategoryWg2:                     #Connects edge Working Group 2 to Chapters & Cross_Chapters
    graph.edge('Wg2',node, style="dotted")

# Creates Chapter 1-18 in Working Group 2
Wg2_Ch=['Ch2_1', 'Ch2_2', 'Ch2_3', 'Ch2_4', 'Ch2_5', 'Ch2_6', 'Ch2_7', 'Ch2_8', 'Ch2_9', 'Ch2_10', 'Ch2_11', 'Ch2_12','Ch2_13','Ch2_14', 'Ch2_15', 'Ch2_16', 'Ch2_17', 'Ch2_18']
for node in Wg2_Ch: #For displaying the properties and URL of Chapters of Working Group 2
    if node=='Ch2_1':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-1/")
    elif node=='Ch2_2':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-2/")
    elif node=='Ch2_3':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-3/")
    elif node=='Ch2_4':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-4/")
    elif node =='Ch2_5':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-5/")
    elif node=='Ch2_6':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-6/")
    elif node=='Ch2_7':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-7/")
    elif node=='Ch2_8':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-8/")
    elif node =='Ch2_9':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-9/")
    elif node=='Ch2_10':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-10/")
    elif node=='Ch2_11':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-11/")
    elif node=='Ch2_12':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-12/")
    elif node=='Ch2_13':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-13/")
    elif node=='Ch2_14':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-14/")
    elif node=='Ch2_15':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-15/")
    elif node=='Ch2_16':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-16/")
    elif node=='Ch2_17':
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-17/")
    else:
        graph.node(node, node, shape='cylinder', style='filled', color="#F5DEB3", URL= "https://www.ipcc.ch/report/ar6/wg2/chapter/chapter-18/")

for node in Wg2_Ch:                     #Connects edge Chapter 1-18 to Chapters from Working Group 2
    graph.edge('Chapters', node, style="dotted")

# Creates Cross-Chapter 1-7 in Working Group 2
Wg2_Ccp=['Ccp1', 'Ccp2', 'Ccp3', 'Ccp4', 'Ccp5', 'Ccp6', 'Ccp7']
for node in Wg2_Ccp: #For displaying the properties and URL of Cross-Chapters of Working Group 2
    if node=='Ccp1':
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF", URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp1/")
    elif node=='Ccp2':
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF",URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp2/")
    elif node=='Ccp3':
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF",URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp3/")
    elif node=='Ccp4':
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF",URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp4/")
    elif node=='Ccp5':
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF",URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp5/")
    elif node=='Ccp6':
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF",URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp6/")
    else:
        graph.node(node, node, shape='cylinder', style='filled', color="#9FE2BF",URL="https://www.ipcc.ch/report/ar6/wg2/chapter/ccp7/")

for node in Wg2_Ccp:                    #Connects edge Cross_Chapter 1-7 to Cross_Chapters from Working Group 2
    graph.edge('Cross_Chapters', node, style="dotted")

# Creates Chapter 1-17 in Working Group 3
Wg3_Ch=['Ch3_1', 'Ch3_2', 'Ch3_3', 'Ch3_4', 'Ch3_5', 'Ch3_6', 'Ch3_7', 'Ch3_8', 'Ch3_9', 'Ch3_10', 'Ch3_11', 'Ch3_12','Ch3_13','Ch3_14', 'Ch3_15', 'Ch3_16', 'Ch3_17']
for node in Wg3_Ch: #For displaying the properties and URL of Chapters of Working Group 3
    if node=='Ch3_1':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-1/")
    elif node=='Ch3_2':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-2/")
    elif node=='Ch3_3':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-3/")
    elif node=='Ch3_4':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-4/")
    elif node =='Ch3_5':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-5/")
    elif node=='Ch3_6':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-6/")
    elif node=='Ch3_7':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-7/")
    elif node=='Ch3_8':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-8/")
    elif node =='Ch3_9':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL="https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-9/")
    elif node=='Ch3_10':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-10/")
    elif node=='Ch3_11':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-11/")
    elif node=='Ch3_12':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-12/")
    elif node=='Ch3_13':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-13/")
    elif node=='Ch3_14':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-14/")
    elif node=='Ch3_15':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-15/")
    elif node=='Ch3_16':
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-16/")
    else:
        graph.node(node, node, shape='cylinder', style='filled', color="#D8BFD8", URL= "https://www.ipcc.ch/report/ar6/wg3/chapter/chapter-17/")

for node in Wg3_Ch:                 #Connects edge Chapter 1-17 to Chapters from Working Group 3
    graph.edge('Wg3', node, style="dotted")

graph.render('layered_graph',view=True) #Renders the graph for output



