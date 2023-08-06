Classiq enables the development of quantum circuits and algorithms that could not be created otherwise. 

We do this by synthesizing high-level functional models into optimized quantum circuits, taking into account the
constraints that are important to the designer. Furthermore, we are able to generate circuits for practically any
universal gate-based quantum computer and are compatible with most quantum cloud providers.

## Requirements
Python 3.8+


## Installation
```console
$ pip install classiq
```

## Example

```python
import asyncio

from classiq.generator import Generator
from classiq.analyzer import Analyzer
from classiq_interface.generator.state_preparation import (
    StatePreparation,
    PMF,
    StatePreparationOutputs,
)
from classiq_interface.generator.qft import QftInputs, QFT
from classiq_interface.generator.preferences.optimization import (
    Optimization,
    OptimizationType,
)

circuit_generator = Generator(qubit_count=8, max_depth=20)
opt = Optimization(optimization_type=OptimizationType.DEPTH, approximation_error=0.05)
circuit_generator.constraints.optimization = opt

probabilities = (0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125)
pmf = PMF(pmf=probabilities)
sp_params = StatePreparation(probabilities=pmf, num_qubits=5)
sp_out_wires = circuit_generator.StatePreparation(params=sp_params)

out_wire_enum = StatePreparationOutputs.OUT
in_wire_enum = QftInputs.IN
wire = sp_out_wires[out_wire_enum]

qft_params = QFT(num_qubits=5)
circuit_generator.QFT(params=qft_params, in_wires={in_wire_enum: wire})

circuit = asyncio.run(circuit_generator.generate())

circuit_analyzer = Analyzer(circuit=circuit)
analysis_result = asyncio.run(circuit_analyzer.analyze())

```

## License

