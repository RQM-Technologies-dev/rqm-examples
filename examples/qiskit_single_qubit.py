"""
qiskit_single_qubit.py

Example using the rqm-qiskit bridge package.
"""

from rqm_qiskit.state import QuantumState

state = QuantumState.zero()

print("Initial state:", state)
