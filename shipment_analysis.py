import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from IPython.display import display
from matplotlib.lines import Line2D

# ---------------------------
# Data
# ---------------------------
def create_data():
    # """Creates mock shipment data including ports, cargo types, departure and arrival times."""
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
    return pd.DataFrame(data)

# ---------------------------
# Visualization of the Shipment per Port in a Bar Chart, TASK 1
# ---------------------------
def plot_bar_with_highlight(df, column, title, xlabel, ylabel, highlight_top_n=5):
    """
    Plots a bar chart of the selected column and highlights the top N values.
    
    Args:
        df: DataFrame containing the data.
        column: The column to plot.
        title: Title of the plot.
        xlabel: Label for the x-axis.
        ylabel: Label for the y-axis.
        highlight_top_n: Number of top values to highlight.
    """
    counts = df[column].value_counts()
    plt.figure(figsize=(10, 6))
    top_n = counts.head(highlight_top_n)
    colors = ['orange' if port in top_n.index else 'skyblue' for port in counts.index]
    counts.plot(kind='bar', color=colors, label='All Ports')

    plt.title(title, fontweight='bold')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.legend(handles=[
        Line2D([0], [0], color='orange', lw=10, label=f'Top {highlight_top_n} Ports'),
        Line2D([0], [0], color='skyblue', lw=10, label='Other Ports')
    ])
    plt.tight_layout()
    plt.show()

# ---------------------------
# Visualization of the pie chart
# ---------------------------

def plot_pie_chart(df, column, title):
    """
    Plots a pie chart showing the distribution of a categorical column.
    
    Args:
        df: DataFrame containing the data.
        column: The column to plot.
        title: Title of the plot.
    """
    counts = df[column].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.arange(len(counts))))
    plt.title(title, fontweight='bold')
    plt.axis('equal')
    plt.show()


# ---------------------------
# Data Preparation (Single DateTime Conversion)
# ---------------------------
def prepare_data(df):
    # """Converts the Departure and Arrival Time columns to datetime objects."""
    df['Departure Time'] = pd.to_datetime(df['Departure Time'])
    df['Arrival Time'] = pd.to_datetime(df['Arrival Time'])
    return df

# ---------------------------
# Utility Function to Format Duration
# ---------------------------
def format_duration(td):
    # """Formats a timedelta object as 'X days Y hours Z minutes'."""
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{days} days {hours} hours {minutes} minutes"

# ---------------------------
# Function to Enhance and Display the Table
# ---------------------------
def display_table(df):
    #"""Enhances the table display and adds formatted Duration."""
    df['Duration'] = df['Arrival Time'] - df['Departure Time']
    df['Duration'] = df['Duration'].apply(format_duration)
    display_df = df[['Shipment ID', 'Departure Port', 'Arrival Port', 'Cargo Type', 'Departure Time', 'Arrival Time', 'Duration']]

    styled_table = display_df.style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#f0f0f0'), ('color', '#333'), ('font-weight', 'bold')]},
        {'selector': 'tbody td', 'props': [('padding', '10px')]}
    ]).hide(axis='index')  # Hide index
    display(styled_table)

# ---------------------------
# Function to Detect Negative Durations
# ---------------------------
def detect_negative_duration(df):
    """
    Detects and prints shipments that have negative durations.
    
    Args:
        df: DataFrame containing the data.
    """
    df['Duration'] = df['Arrival Time'] - df['Departure Time']
    negative_duration = df[df['Duration'] < pd.Timedelta(0)]
    
    if not negative_duration.empty:
        print("Negative durations found:")
        print(negative_duration[['Shipment ID', 'Departure Port', 'Arrival Port', 'Duration']])
    else:
        print("No negative durations found.")

# ---------------------------
# Function to Swap Negative Durations
# ---------------------------
def swap_negative_duration_times(df):
    """Swaps Departure and Arrival times if the duration is negative."""
    new_df = df.copy()
    new_df['Duration'] = new_df['Arrival Time'] - new_df['Departure Time']
    negative_duration_mask = new_df['Duration'] < pd.Timedelta(0)
    
    # Swap times for negative durations
    new_df.loc[negative_duration_mask, ['Departure Time', 'Arrival Time']] = new_df.loc[negative_duration_mask, ['Arrival Time', 'Departure Time']].values
    
    return new_df

# ---------------------------
# Function to Plot Departure Distribution by Hour
# ---------------------------
def plot_departure_distribution(df):
    """Plots the distribution of ship departures by the hour of the day."""
    df['departure_hour'] = df['Departure Time'].dt.hour
    plt.figure(figsize=(10, 4))
    counts, bins, patches = plt.hist(df['departure_hour'], bins=range(25), edgecolor='black', rwidth=0.85, align='left')

    for count, patch in zip(counts, patches):
        plt.text(patch.get_x() + patch.get_width() / 2, count + 0.2, int(count), ha='center', va='top', color='blue')

    plt.title('Distribution of Ship Departures by Hour of the Day')
    plt.xlabel('Hour of the Day (24-hour format)')
    plt.ylabel('Number of Departures')
    plt.xticks(range(0, 24))
    plt.ylim(0, max(counts) + 0.5)
    plt.show()

# Helper function to create graph (undirected or directed)
def create_graph(df, weight_type='frequency', graph_type='directed'):
    """Creates a graph using NetworkX, based on frequency or duration of shipments."""
    G = nx.Graph() if graph_type == 'undirected' else nx.DiGraph()

    for _, row in df.iterrows():
        if weight_type == 'frequency':
            G.add_edge(row['Departure Port'], row['Arrival Port'], weight=G.get_edge_data(row['Departure Port'], row['Arrival Port'], default={'weight': 0})['weight'] + 1)
        elif weight_type == 'duration':
            duration = (row['Arrival Time'] - row['Departure Time']).total_seconds() / 3600
            G.add_edge(row['Departure Port'], row['Arrival Port'], weight=duration)
    return G

# Function to define the positions of ports
def get_positions():
    return {
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

# Function to plot the graph
def plot_graph(G, positions, weight_type='frequency'):
    """Plots a network graph of ports and shipments with weights based on the selected type."""
    plt.figure(figsize=(12, 10))
    nx.draw_networkx_edges(G, positions, edge_color='black', arrows=True, arrowsize=20, width=2)
    nx.draw_networkx_nodes(G, positions, node_size=500, node_color='lightblue', alpha=0.5)
    nx.draw_networkx_labels(G, positions, font_size=10, font_color='red')

    if weight_type == 'frequency':
        top_5_ports = sorted(G.degree, key=lambda x: x[1], reverse=True)[:5]
        nx.draw_networkx_nodes(G, positions, nodelist=[port for port, degree in top_5_ports], node_color='yellow', node_size=[100 * degree for port, degree in top_5_ports], alpha=0.5)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=edge_labels, font_size=8, font_color='blue')

    if weight_type == 'duration':
        plt.legend(handles=[
            Line2D([0], [0], marker='o', color='w', label='Ports', markerfacecolor='lightblue', markersize=10),
            Line2D([0], [0], color='black', lw=2, label='Edges')
        ], loc='upper left')
    else:
        plt.legend(handles=[
            Line2D([0], [0], marker='o', color='w', label='Top 5 Ports', markerfacecolor='yellow', markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Other Ports', markerfacecolor='lightblue', markersize=10),
            Line2D([0], [0], color='black', lw=2, label='Edges')
        ], loc='upper left')

    plt.title(f'Network Graph of Ports and Shipments with {weight_type.capitalize()} as Edge Weights', fontweight='bold')
    plt.show()

# Function to analyze and visualize the undirected network and calculate shortest paths
def analyze_undirected_network(df):
    G = create_graph(df, weight_type="duration", graph_type="undirected")  # Create an undirected graph

    # Plot the undirected graph using the existing plot_graph function
    plot_graph(G, get_positions(), weight_type='duration')

    # Analyze each shipment for direct vs. transit paths
    results = []
    for _, row in df.iterrows():
        shipment_id = row['Shipment ID']
        cargo_type = row['Cargo Type']
        departure = row['Departure Port']
        arrival = row['Arrival Port']
        direct_duration = round((row['Arrival Time'] - row['Departure Time']).total_seconds() / 3600, 1)

        # Find the shortest path using Dijkstra's algorithm
        shortest_duration = round(nx.shortest_path_length(G, source=departure, target=arrival, weight='weight'), 1)
        shortest_path = nx.shortest_path(G, source=departure, target=arrival, weight='weight')

        # Compare direct and shortest path durations
        transit_needed = shortest_duration < direct_duration

        # Store the results
        results.append({
            'Shipment ID': shipment_id,
            'Cargo Type': cargo_type,
            'Departure': departure,
            'Arrival': arrival,
            'Direct Duration (hours)': direct_duration,
            'Shortest Duration (hours)': shortest_duration,
            'Shortest Path': ' -> '.join(shortest_path),
            'Transit Needed': transit_needed
        })

    # Convert the results to a DataFrame for easy viewing
    return pd.DataFrame(results)

# ---------------------------
# Display Results with Custom Styling
# ---------------------------
def display_results(results_df):
    # Apply the custom table style
    styled_table = results_df.style.set_table_styles([
        {'selector': 'thead th', 'props': [('background-color', '#f0f0f0'), ('color', '#333'), ('font-weight', 'bold')]},
        {'selector': 'tbody tr:nth-child(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tbody td', 'props': [('padding', '10px')]}
    ]).format({"Direct Duration (hours)": "{:.1f}", "Shortest Duration (hours)": "{:.1f}"})

    # Display the styled table
    display(styled_table)

# ---------------------------
# Main Program Execution
# ---------------------------
def analyze_network(df, weight_type='frequency'):
    """Analyzes the shipment network and plots it."""
    G = create_graph(df, weight_type)
    positions = get_positions()  # Fix: Call the function by adding parentheses
    plot_graph(G, positions, weight_type)

# ---------------------------
# Complete Workflow
# ---------------------------
df = create_data()

plot_bar_with_highlight(df, 'Departure Port', 'Top Departure Ports', 'Ports', 'Number of Shipments')
plot_pie_chart(df, 'Cargo Type', 'Cargo Type Distribution')
analyze_network(df, weight_type='frequency')

df = prepare_data(df)  # Centralized datetime conversion
display_table(df)  # Display the initial table
detect_negative_duration(df)  # Detect negative durations

# Swap negative duration times, if any
revised_df = swap_negative_duration_times(df)
display_table(revised_df)  # Display the table after swapping

plot_departure_distribution(revised_df)  # Plot distribution by hour
analyze_network(revised_df, weight_type='duration')  # Analyze and visualize the network

# Analyze and display results for undirected network
results_df = analyze_undirected_network(revised_df)
display_results(results_df)
