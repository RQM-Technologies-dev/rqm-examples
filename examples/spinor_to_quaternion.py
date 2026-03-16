"""
spinor_to_quaternion.py

Shows how spinors map to quaternions using rqm-core.
"""

from rqm_core.spinor import spinor_to_quaternion

alpha = complex(1, 0)
beta = complex(0, 0)

q = spinor_to_quaternion(alpha, beta)

print("Quaternion representation:", q)
