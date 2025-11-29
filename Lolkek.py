import pickle

with open('answers.txt', 'rb') as f:
    answers = pickle.load(f)
    print(answers)