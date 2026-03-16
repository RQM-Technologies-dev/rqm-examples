"""
quaternion_rotation.py

Demonstrates quaternion rotation operations using rqm-core.
"""

from rqm_core.quaternion import Quaternion

q = Quaternion(0.7071, 0.7071, 0, 0)

print("Quaternion:", q)
print("Norm:", q.norm())
