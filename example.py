import qiskit
from qiskit import IBMQ
from qiskit import *

IBMQ.save_account('<INSERT_KEY>',overwrite=True)

IBMQ.load_account()


qr = QuantumRegister(2) 	#2 qubit quantum register

cr = ClassicalRegister(2)	#2 bit classical register

circuit = QuantumCircuit(qr,cr)



print(circuit.draw())

#do more research on what a hadamard gate and what does it have to do with entanglement?
circuit.h(qr[0])
circuit.draw(output = 'mpl')


# Controlled X, like logical IF. If this then that
circuit.cx(qr[0],qr[1])
circuit.draw(output = 'mpl')

#measure quantum bits so we can know what happened in the quantum circuit in the end
circuit.measure(qr,cr)
circuit.draw(output = 'mpl')

#run the circuit for confidence: simulator. Aer is used for simulations 
simulator = Aer.get_backend('qasm_simulator')
execute(circuit,backend = simulator)
result = execute(circuit,backend = simulator).result()
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))
#run the circuit for confidence: simulator

#we actually run this in our quantum device. wait will job is queued and ran!!
IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne') #you can use a device that is not busy
job = execute(circuit, backend = qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)
result = job.result()
plot_histogram(result.get_counts(circuit))

#simulator would simulate the perfect quantum device
#quantum device succeptable to little errors