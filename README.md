# Shipping-Analysis

A project analyzing global shipping routes, port activity, and cargo distribution using Python and NetworkX.

## Overview

This project uses a mock dataset of shipment records to perform the following tasks:
1. **Data Visualization**: Bar charts and pie charts to display shipment data.
2. **Network Analysis**: Creation and visualization of a directed graph representing shipping routes between ports, with node degrees and edge weights indicating port activity and shipment frequency.

## Features
- **Top Departure Ports**: Visualizes the most active departure ports based on shipment data.
- **Cargo Type Distribution**: A pie chart representing the distribution of different cargo types across shipments.
- **Network Graph**: A directed graph that visualizes connections between ports, highlighting the most connected ports and the number of shipments between them.

## Dependencies

The following Python libraries are required:
- `pandas`
- `matplotlib`
- `networkx`

You can install the necessary libraries by running:
```bash
pip install pandas matplotlib networkx
