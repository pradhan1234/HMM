# Homework 3
# Hidden Markov Model: Viterbi Algorithm
# author: Yash Pradhan

import sys

# model parameters

states = ["hot", "cold"]
symbols = ["1","2","3"]

initial_probability = {"hot":0.8, "cold":0.2}

emission_probability = {"hot":{"1":0.2, "2":0.4, "3":0.4},
                          "cold":{"1":0.5, "2":0.4, "3":0.1}}

transistion_probability = {"hot":{"hot":0.7, "cold":0.3},
                           "cold":{"hot":0.4, "cold":0.6}}


if(len(sys.argv) == 2):
	observation_sequence = sys.argv[1]
else:
	print("\nPlease provide Complete Observation Sequence as Command Line Argument")
	print("> python hmm.py 331122313")
	exit()

result = []
back_trace = []
for i in range(len(observation_sequence)):
    obs = observation_sequence[i]
    
    local_result = []
    local_back_trace = []
    for j in range(len(states)):
        state = states[j]
        if(i==0):
            local_result.append(initial_probability[state]*emission_probability[state][obs])
            local_back_trace.append("start")
        else:
            max_so_far = 0
            best_k = 0
            for k in range(len(states)):
                previous_state = states[k]
                if(max_so_far<result[i-1][k]*transistion_probability[previous_state][state]*emission_probability[state][obs]):
                    max_so_far = result[i-1][k]*transistion_probability[previous_state][state]*emission_probability[state][obs]
                    best_k = k
            local_result.append(max_so_far)
            local_back_trace.append(best_k)
    result.append(local_result)
    back_trace.append(local_back_trace)

if(result[-1][0] > result[-1][1]):
    probability = result[-1][0]
    back_trace.append(0)
else:
    probability = result[-1][1]
    back_trace.append(1)
result.append(probability)
    


i = len(back_trace) - 2
prevIndex = back_trace[-1]    

hidden_states = []

while i >= 0:
    hidden_states.insert(0, states[prevIndex])
    prevIndex = back_trace[i][prevIndex]
    i -= 1



print("Observation Sequence: " + observation_sequence)
print("Probability: ", result[-1])
print("Most Likely Weather Sequence: ", end="")

for state in hidden_states:
	print(state, end =" ")