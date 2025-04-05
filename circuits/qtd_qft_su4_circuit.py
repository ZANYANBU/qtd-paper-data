# QTD SU(4) Circuit Simulation
from qiskit import QuantumCircuit
qc = QuantumCircuit(4)
qc.h(0)
qc.cx(0, 1)
print(qc)