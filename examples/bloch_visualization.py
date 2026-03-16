"""
bloch_visualization.py

Demonstrates Bloch vector conversion using rqm-core.
"""

from rqm_core.bloch import state_to_bloch

state = [1, 0]

bloch = state_to_bloch(state)

print("Bloch vector:", bloch)
