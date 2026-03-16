# RQM Examples

This repository provides **runnable demonstrations** of the RQM software stack.

Examples illustrate:

- quaternion operations
- spinor conversions
- Bloch sphere relationships
- SU(2) rotations
- simple quantum circuits

## Dependencies

The examples rely on:

```
rqm-core
rqm-qiskit
```

## Installation

```bash
pip install -e .
```

## Running an Example

```bash
python examples/quaternion_rotation.py
```

## Examples

| Script | Description |
|--------|-------------|
| `examples/quaternion_rotation.py` | Demonstrates quaternion rotations |
| `examples/spinor_to_quaternion.py` | Shows how spinors map to quaternions |
| `examples/bloch_visualization.py` | Demonstrates Bloch vector conversion |
| `examples/su2_gate_demo.py` | Demonstrates SU(2) matrix generation |
| `examples/qiskit_single_qubit.py` | Example using the rqm-qiskit bridge package |

## Architecture

`rqm-examples` sits above the core libraries in the ecosystem:

```
rqm-core
    ↓
rqm-qiskit
    ↓
rqm-examples
```

This repository **does not implement any math or algorithms**.
It exists only to demonstrate usage of the packages above.
