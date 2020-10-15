import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

max_iter_num = 5  # 模拟的次数
G = nx.karate_club_graph()  # 空手道俱乐部

for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值 病毒的感染能力
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 未激活，state=1 激活

seed = 33  # 选定33作为传染源
G.node[seed]['state'] = 1  # 表示33是感染的

all_infect_nodes = []  # 所有被感染的节点放在这里
all_infect_nodes.append(seed)

infected_graph = nx.Graph()  # 被激活的图
infected_graph.add_node(seed)

for i in range(max_iter_num):
    new_infect = list()  # 新被感染的
    t1 = '%s time' % i + ' %s nodes' % len(all_infect_nodes)
    print(t1)  # 当前有多少个节点被感染

    # 画图
    plt.title(t1)
    nx.draw(infected_graph, with_labels=True)
    plt.show()

    # 感染的机会不止一次
    for v in all_infect_nodes:
        for nbr in G.neighbors(v):
            if G.node[nbr]['state'] == 0:  # 如果这个邻居节点没被感染
                edge_data = G.get_edge_data(v, nbr)
                if random.uniform(0, 1) < edge_data['weight']:
                    G.node[nbr]['state'] = 1
                    new_infect.append(nbr)
                    infected_graph.add_edge(v, nbr)  # 画图 添加边

    all_infect_nodes.extend(new_infect)  # 将新感染的添加到
    print('all_active_nodes:', all_infect_nodes)
