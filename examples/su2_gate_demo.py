"""
su2_gate_demo.py

Demonstrates SU(2) matrix generation using rqm-core.
"""

from rqm_core.su2 import axis_angle_to_su2

matrix = axis_angle_to_su2([0, 0, 1], 3.14159)

print("SU(2) matrix:", matrix)
