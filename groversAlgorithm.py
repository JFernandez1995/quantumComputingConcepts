# first, we would like to see a classical approach to finding, lets say, a winner



#create a list:
listing = [1,4,6,8,3,4,8,5,12,7]

def the_oracle(winnerInput):

	winner = 7
	if winnerInput == winner:
		response = True

	else:
		response = False

	return response


for i in range(len(listing)):

	if the_oracle(listing[i]) == True:
		print('winner found at index')
		print(i)
		print('calls to oracle function: ')
		print(i+1)
		break

#the classical approach above would normally take O(N) time complexity


'''
2 qubits representing the 4 input states
00
01
10
11 -> [oracle] -> -11 if winner

'''

#Controlled z gate to flip the 11 state
#Grover's diffusion operation [Oracle] + [reflection]: amplitude amplification

from qiskit import *
import matplotlib.pyplot as plt
import numpy as np

oracle = QuantumCircuit(2,name = 'oracle')
oracle.cz(0,1)
oracle.to_gate()
oracle.draw()

#define backend
backend = Aer.get_backend('statevector_simulator')
#define the grover cirucuit. 2 qubits, 2 classcal registers
grover_circ = QuantumCircuit(2,2)
#add hadamard gates for both qubits to prepare superposition state
grover_circ.h([0,1])
#add oracle
grover_circ.append(oracle, [0,1])
grover_circ.draw()

#execute job and get result of the job from a simulator
job = execute(grover_circ,backend)
result = job.result()

#get the state vector from the job result
stateVector = result.get_statevector()
np.round(stateVector,2)

#output
#array([ 0.5+0.j,  0.5+0.j,  0.5+0.j, -0.5+0.j])

'''
aplitude amplification -> amplify the probabilities of the winning state 
and reduce the probalities the non-winning states

o(squar_root(n))
'''

reflection = QuantumCircuit(2,name = 'reflection')
reflection.h([0,1])
reflection.z([0,1])
reflection.cz(0,1)
reflection.h([0,1])
reflection.to_gate()

#check out the circuit you have just built
grover_circ.draw()

#execute the job and get the results from the job
job = execute(grover_circ,backend,shots=1)
result=job.result()
result.get_counts()

'''
output:
{'11': 1}

this gets us our winning state in 1 call
'''