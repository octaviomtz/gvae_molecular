#!/bin/bash
pyg=$( python3 install_geometric.py )
pip3 install torch-scatter     -f $pyg
pip3 install torch-sparse      -f $pyg
pip3 install torch-cluster     -f $pyg
pip3 install torch-spline-conv -f $pyg
pip3 install torch-geometric 