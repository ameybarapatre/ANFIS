# ANFIS
ANFIS Q Learning

# Dataset.py
It creates all possible combinations of waiting time , active time , total fare and ride fare and stores it in dataset.csv

# ANFIS.py
It creates the ANFIS network uses renforcement learning algorithm Q Learning and stores the trained network

# Preprocessing.py 
It generates fuzzy membership fucntions and calculates reward values using PID for each combination in the dataset.csv

# run.py
loads a saved model or creates a new one if saved model isn't found it creates one , and generates Q factor values for each input.
