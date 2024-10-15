# Shipment Network Analysis and Visualization

This project performs shipment analysis using mock data for various ports, cargo types, and shipment times. The analysis covers the following aspects:

- **Bar and Pie Charts**: Visualization of shipment distributions.
- **Graph Analysis**: Network visualization of shipments between ports using NetworkX.
- **Duration Calculations**: Detecting negative shipment durations, swapping times if necessary, and analyzing shortest paths for shipments.

## Features

1. **Data Generation**:
   - Mock shipment data is created for 20 shipments involving multiple ports and cargo types.
   
2. **Visualization**:
   - **Bar Chart**: Highlights the top departure ports.
   - **Pie Chart**: Displays the distribution of cargo types.
   - **Network Graph**: Visualizes the shipment paths between ports with edge weights representing shipment duration or frequency.

3. **Data Preprocessing**:
   - The dataset is prepared by converting string times into datetime objects and calculating the shipment duration.

4. **Duration Handling**:
   - Detection of negative shipment durations (if the arrival time is before the departure time).
   - Automatic swapping of departure and arrival times for shipments with negative durations.

5. **Graph Network Analysis**:
   - Creation of directed or undirected graphs based on shipment paths.
   - Calculation of direct and shortest paths between ports using Dijkstra's algorithm.
   
6. **Custom Styling**:
   - Custom table display and styling for better visualization of results.

## Dependencies

This project requires the following Python libraries:

- `pandas`: For data manipulation and analysis.
- `matplotlib`: For data visualization.
- `networkx`: For network graph creation and analysis.
- `numpy`: For numerical operations.
- `IPython.display`: For displaying tables in Jupyter environments.

You can install the dependencies using the following command:

```bash
pip install pandas matplotlib networkx numpy
etc.
```

## How to Run

### 1. Create the Data
The `create_data()` function generates a mock dataset of shipment information, including shipment IDs, departure ports, arrival ports, cargo types, and times.

### 2. Data Preparation
The `prepare_data()` function converts the departure and arrival times to datetime objects for proper time calculations.

### 3. Visualization

- Use `plot_bar_with_highlight()` to create a bar chart for the top ports.
- Use `plot_pie_chart()` to generate a pie chart for cargo type distribution.
- Use `plot_departure_distribution()` to display a histogram of departure times by the hour of the day.

### 4. Network Analysis

- Use `analyze_network()` to analyze and visualize the shipment network. The function allows switching between using shipment **frequency** or **duration** as the edge weight in the graph.
- The `analyze_undirected_network()` function generates an undirected network graph and calculates shortest shipment paths between ports.

### 5. Duration Analysis

- Use `detect_negative_duration()` to identify shipments with negative durations.
- If negative durations exist, use `swap_negative_duration_times()` to swap the departure and arrival times automatically.

### 6. Result Display
The `display_table()` and `display_results()` functions provide enhanced and styled table displays, making the output easier to interpret.

