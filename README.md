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

### Quaternion rotation

```bash
python examples/quaternion_rotation.py
```

```
Quaternion: (0.7071, 0.7071, 0, 0)
Norm: 1.0
```

### Spinor to quaternion

```bash
python examples/spinor_to_quaternion.py
```

```
Quaternion representation: (1.0, 0.0, 0.0, 0.0)
```

### Bloch vector conversion

```bash
python examples/bloch_visualization.py
```

```
Bloch vector: (0.0, 0.0, 1.0)
```

### SU(2) gate demo

```bash
python examples/su2_gate_demo.py
```

```
SU(2) matrix: [[-0.+0.j, 0.+0.j], [0.+0.j, -0.+0.j]]
```

### Qiskit single qubit

```bash
python examples/qiskit_single_qubit.py
```

```
Initial state: |0⟩
```

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
