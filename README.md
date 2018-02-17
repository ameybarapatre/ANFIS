

# DQN for Taxi Fleet Management

Proposal : To create a Deep Q learning Network to help dictate taxi allotment to user request.
A adaptive-neuro fuzzy network is created with rules with antecedents like  user's waiting time , taxi's active time ,
expected ride fare and total fare collected by the taxi . The network is trained using Q learning a reinforcement
learning method . The  output of the trained network is the Q factor for each possible taxi that can server a request.

## Reward Function :
Any reinforcement learning algorithm is based around maximizing the total reward at the end of an episode of actions.
The aim of the model is to ensure that rate of total fare per unit time of every taxi must converge on to its average
over all taxis. Thus reward function for the model is derived from the output of software implementation of
proportional–integral–derivative controller .The error is the difference between current and average rate of earning.

## Q learning :

Q-learning is a model-free reinforcement learning technique. Specifically, Q-learning can be used to find an optimal
action-selection policy for any given Markov decision process (MDP). It works by learning an action-value
function (Q function) that ultimately gives the expected utility of taking a given action in a given state and
following the optimal policy thereafter. A policy is a rule that the agent follows in selecting actions,
given the state it is in. When such an action-value function is learned, the optimal policy can be constructed by
simply selecting the action with the highest value in each state. One of the strengths of Q-learning is that
it is able to compare the expected utility of the available actions without requiring a model of the environment.


## Dataset.py
It creates all possible combinations of waiting time , active time , total fare and ride fare and stores it in dataset.csv

## ANFIS.py
It creates the ANFIS network uses reinforcement learning algorithm Q Learning and stores the trained network.

## Preprocessing.py 
It generates fuzzy membership fucntions and calculates reward values using PID for each combination in the dataset.csv

### Fuzzy rules:

if active_time_high and total_fare_low then Z1

if fare_high and waiting_time_low then Z2

if fare_high and waiting_time_low and active_time_high and total_fare_low then Z3

if fare_high and total_fare_low and active_time_high then Z4

## run.py
loads a saved model or creates a new one if saved model isn't found it creates one , and generates Q factor values for each input.
