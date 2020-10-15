import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

max_iter_num = 10  # 模拟的次数
G = nx.karate_club_graph()  # 空手道俱乐部

for edge in G.edges:
    G.add_edge(edge[0], edge[1], weight=random.uniform(0, 1))  # 可不可以作为权值
for node in G:
    G.add_node(node, state=0)  # 用state标识状态 state=0 未激活，state=1 激活

seed = 33  # 选定33作为初始激活节点
G.nodes[seed]['state'] = 1  # 表示33被激活

# activated_graph = nx.Graph() # 被激活的图
# activated_graph.add_node(seed)

all_active_nodes = [seed]  # 所有被激活的节点放在这里

start_influence_nodes = [seed]  # 刚被激活的节点 即有影响力去影响别人的节点

color_list = ['brown', 'orange', 'r', 'g', 'b', 'y', 'm', 'gray', 'black', 'c', 'pink', 'brown', 'orange', 'r', 'g',
              'b', 'y', 'm', 'gray', 'black', 'c', 'pink']
res = [[seed]]
for i in range(max_iter_num):
    new_active = list()
    t1 = '%s time' % i + ' %s nodes' % len(all_active_nodes)
    print(t1)  # 当前有多少个节点激活

    # 画图
    # plt.title(t1)
    # nx.draw(activated_graph, with_labels=True,node_color=color_list[i])
    # plt.show()

    for v in start_influence_nodes:
        for nbr in G.neighbors(v):
            if G.nodes[nbr]['state'] == 0:  # 如果这个邻居没被激活
                edge_data = G.get_edge_data(v, nbr)
                if random.uniform(0, 1) < edge_data['weight']:
                    G.nodes[nbr]['state'] = 1
                    new_active.append(nbr)
                    # activated_graph.add_edge(v, nbr) # 画图 添加边

    print('激活', new_active)
    start_influence_nodes.clear()  # 将原先的有个影响力的清空
    start_influence_nodes.extend(new_active)  # 将新被激活的节点添加到有影响力
    all_active_nodes.extend(new_active)  # 将新被激活的节点添加到激活的列表中
    res.append(new_active)

    print('all_active_nodes', all_active_nodes)  # 打印
# print(res)

res = [c for c in res if c]
pos = nx.spring_layout(G)  # 节点的布局为spring型
nx.draw(G, pos, with_labels=True, node_color='w', node_shape='.')
color_list = ['brown', 'orange', 'r', 'g', 'b', 'y', 'm', 'gray', 'black', 'c', 'pink', 'brown', 'orange', 'r', 'g',
              'b', 'y', 'm', 'gray', 'black', 'c', 'pink']
for i in range(len(res)):
    nx.draw_networkx_nodes(G, pos,  node_color=color_list[i], nodelist=res[i])
plt.show()

