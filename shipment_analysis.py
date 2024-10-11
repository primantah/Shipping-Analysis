#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Oct  11 17:38:05 2024
@author: PRIMANTA HOLAND BANGUN
"""

# shipment_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# ---------------------------
# Mock Data (Predefined and Clean)
# ---------------------------
data = {
    'Shipment ID': [
        'SHIP_0001', 'SHIP_0002', 'SHIP_0003', 'SHIP_0004', 'SHIP_0005',
        'SHIP_0006', 'SHIP_0007', 'SHIP_0008', 'SHIP_0009', 'SHIP_0010',
        'SHIP_0011', 'SHIP_0012', 'SHIP_0013', 'SHIP_0014', 'SHIP_0015',
        'SHIP_0016', 'SHIP_0017', 'SHIP_0018', 'SHIP_0019', 'SHIP_0020'
    ],
    'Departure Port': [
        'Port of Rotterdam', 'Port of Hamburg', 'Port of Tianjin', 'Port of Antwerp', 'Port of Los Angeles',
        'Port of Dubai', 'Port of Busan', 'Port of Singapore', 'Port of Qingdao', 'Port of Shanghai',
        'Port of Rotterdam', 'Port of Hamburg', 'Port of Tianjin', 'Port of Antwerp', 'Port of Los Angeles',
        'Port of Dubai', 'Port of Busan', 'Port of Singapore', 'Port of Qingdao', 'Port of Shanghai'
    ],
    'Arrival Port': [
        'Port of Dubai', 'Port of Antwerp', 'Port of Los Angeles', 'Port of Shanghai', 'Port of Rotterdam',
        'Port of Hamburg', 'Port of Singapore', 'Port of Qingdao', 'Port of Dubai', 'Port of Busan',
        'Port of Los Angeles', 'Port of Tianjin', 'Port of Antwerp', 'Port of Dubai', 'Port of Busan',
        'Port of Shanghai', 'Port of Rotterdam', 'Port of Los Angeles', 'Port of Tianjin', 'Port of Hamburg'
    ],
    'Cargo Type': [
        'Bulk Liquids', 'Frozen Meat', 'Refrigerated Goods', 'Grain', 'Processed Foods',
        'Rice', 'Soybeans', 'Vegetables', 'Fruits', 'Corn',
        'Bulk Liquids', 'Frozen Meat', 'Refrigerated Goods', 'Grain', 'Processed Foods',
        'Rice', 'Soybeans', 'Vegetables', 'Fruits', 'Corn'
    ],
    'Departure Time': [
        '2024-01-10 08:00', '2024-02-15 12:30', '2024-03-20 16:45', '2024-04-25 09:15', '2024-05-30 14:20',
        '2024-06-05 07:50', '2024-07-10 11:25', '2024-08-15 18:40', '2024-09-20 05:10', '2024-10-25 22:55',
        '2024-11-30 13:35', '2024-12-05 09:00', '2025-01-10 16:45', '2025-02-14 20:30', '2025-03-19 11:10',
        '2025-04-24 03:55', '2025-05-29 10:20', '2025-06-30 19:40', '2025-07-15 08:25', '2025-08-20 14:50'
    ],
    'Arrival Time': [
        '2024-01-15 14:00', '2024-02-20 18:30', '2024-03-25 22:45', '2024-04-30 15:15', '2024-06-04 20:20',
        '2024-06-10 13:50', '2024-07-15 16:25', '2024-08-20 23:40', '2024-09-25 11:10', '2024-10-30 04:55',
        '2024-12-05 19:35', '2024-12-10 15:00', '2025-01-15 21:45', '2025-02-19 02:30', '2025-03-24 17:10',
        '2025-04-29 09:55', '2025-05-04 14:20', '2025-06-09 23:40', '2025-07-14 13:25', '2025-08-25 19:50'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Departure Time' and 'Arrival Time' to datetime objects
df['Departure Time'] = pd.to_datetime(df['Departure Time'])
df['Arrival Time'] = pd.to_datetime(df['Arrival Time'])

# ---------------------------
# Data Visualization
# ---------------------------

# 1a. Top 5 Departure Ports

# Bar Chart with Highlighted Top 5 Ports
plt.figure(figsize=(10, 6))
top_5_ports = departure_counts.head(5)
colors = ['orange' if port in top_5_ports.index else 'skyblue' for port in departure_counts.index]

# Plot the bar chart for departure ports with labels for legend
departure_counts.plot(kind='bar', color=colors, label='All Ports')
plt.title('Departure Ports by Number of Shipments (Top 5 Highlighted)', fontweight='bold')
plt.xlabel('Departure Port')
plt.ylabel('Number of Shipments')
plt.xticks(rotation=45)

# Set custom y-axis ticks to only show 0, 1, and 2
plt.yticks([0, 1, 2])

# Adding custom legend
plt.legend(handles=[
    plt.Line2D([0], [0], color='orange', lw=10, label='Top 5 Ports'),
    plt.Line2D([0], [0], color='skyblue', lw=10, label='Other Ports')
])

plt.tight_layout()
plt.show()


# b. Cargo Type Distribution
cargo_distribution = df['Cargo Type'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(cargo_distribution, labels=cargo_distribution.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Cargo Type Distribution', fontweight='bold')
plt.axis('equal')
plt.show()

# ---------------------------
# Basic Network Analysis
# ---------------------------

# 2a. Construct a Network Graph
G = nx.DiGraph()

# Adding edges with weights
for _, row in df.iterrows():
    G.add_edge(row['Departure Port'], row['Arrival Port'], weight=G.get_edge_data(row['Departure Port'], row['Arrival Port'], default={'weight': 0})['weight'] + 1)

# b. Visualize the Network with Realistic Port Positions and Semi-Transparent Nodes (with Edge Weights)
plt.figure(figsize=(12,10))

# Define a fixed node size for all nodes
node_size = 500  # Set a fixed size for the nodes

# Define custom positions for each port (approximate geographic positions)
positions = {
    'Port of Rotterdam': (-1, 5),
    'Port of Hamburg': (0, 6),
    'Port of Tianjin': (6, 3),
    'Port of Antwerp': (-2, 4),
    'Port of Los Angeles': (-7, 2),
    'Port of Dubai': (3, 2),
    'Port of Busan': (9, 2.5),
    'Port of Singapore': (5, 0),
    'Port of Qingdao': (7, 4),
    'Port of Shanghai': (6, 5)
}

# Draw the edges with arrows and display weights
nx.draw_networkx_edges(G, positions, edge_color='black', arrows=True, arrowsize=20, width=2)

# Draw the network graph nodes with semi-transparent color
nx.draw_networkx_nodes(G, positions, node_size=node_size, node_color='lightblue', alpha=0.5)

# Draw labels
nx.draw_networkx_labels(G, positions, font_size=10, font_color='red')

# Highlight the top 5 most connected ports with semi-transparent orange nodes
top_5_ports = sorted(G.degree, key=lambda x: x[1], reverse=True)[:5]
nx.draw_networkx_nodes(G, positions, nodelist=[port for port, degree in top_5_ports], node_color='yellow', node_size=[100 * degree for port, degree in top_5_ports], alpha=0.5)

# Add edge weights as labels on the graph
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels)

# Create a custom legend
plt.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='w', label='Top 5 Ports', markerfacecolor='yellow', markersize=10),
    plt.Line2D([0], [0], marker='o', color='w', label='Other Ports', markerfacecolor='lightblue', markersize=10),
    plt.Line2D([0], [0], color='black', lw=2, label='Edges')
])

plt.title('Network Graph of Ports and Shipments with Edge Weights (Top 5 Highlighted)', fontweight='bold')
plt.show()


# Print the edge weights to the console
for u, v, data in G.edges(data=True):
    print(f"Edge from {u} to {v} has weight {data['weight']}")

print()

# Print node degree information sorted by highest total degree
degree_info = [(node, G.out_degree(node), G.in_degree(node), G.degree(node)) for node in G.nodes()]
sorted_degree_info = sorted(degree_info, key=lambda x: x[3], reverse=True)

# Print the sorted node degree information
for node, out_degree, in_degree, total_degree in sorted_degree_info:
    print(f"Node: {node}, Out-Degree: {out_degree}, In-Degree: {in_degree}, Total Degree: {total_degree}")

# ---------------------------
# Insights
# ---------------------------
# 1. Each port has exactly 2 shipments, indicating an equal distribution of the shipping load across all ports in the dataset.
#	 There is no dominant port in terms of departures, and the top 5 ports are highlighted based on their detection order rather than volume.
#	 The chart also shows a global distribution of ports across Europe, Asia, the Middle East, and North America, reflecting a well-balanced global shipping network.
# 2. All cargo types—Bulk Liquids, Corn, Fruits, Vegetables, Soybeans, Rice, Processed Foods, Grain, Refrigerated Goods, and Frozen Meat—make up an equal share (10%) of the total shipments.
#	 This indicates a balanced variety of goods, with no emphasis on any single type, serving industries like agriculture, food processing, and energy
#	 The inclusion of temperature-controlled goods (Frozen Meat, Refrigerated Goods) suggests the network supports such shipments, highlighting the importance of speed and efficiency.
#	 This equal distribution may also reflect a strategy to reduce risk by diversifying the cargo base, making operations more resilient to market disruptions.
# 3. Dubai and Los Angeles are the most active ports, with 5 connections to other key ports, highlighting their role as central hubs in the shipping network.
#	 Hamburg, Rotterdam, Antwerp, Tianjin, and Shanghai also play significant roles with 4 connections, reinforcing their importance in global shipping.
#	 Each edge has a weight of 1, indicating only one shipment between each pair of connected ports, suggesting that no single route is heavily trafficked.
#	 Each port has exactly 2 shipments, indicating an equal distribution of the shipping load across all ports in the dataset.
#	 The chart also shows a global distribution of ports across Europe, Asia, the Middle East, and North America, reflecting a well-balanced global shipping network.
