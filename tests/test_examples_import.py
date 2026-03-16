"""
Tests that example scripts can be imported without errors.
"""


def test_examples_import():
    import examples.quaternion_rotation
    import examples.spinor_to_quaternion
    import examples.bloch_visualization
    import examples.su2_gate_demo
    import examples.qiskit_single_qubit
