import numpy as np
import matplotlib.pyplot as plt
import time

class Results():
    def __init__(self):
        None

    def get_information_for_chart():
        None

    def print_in_barchart(self, data_dict):
        X_data = list(data_dict.keys())
        Y_data = list(data_dict.values())
        amount_of_times_run = 10000

        plt.bar(X_data, Y_data)
        plt.title(f'Ran algorithms {amount_of_times_run} times on 6x6_1')
        plt.xlabel('Algorithms')
        plt.ylabel('Average amount of moves made')
        return plt.show()
    
    def print_in_boxplot(self, data_dict):
        X_data = list(data_dict.keys())
        Y_data = list(data_dict.values())
        amount_of_times_run = 10000

        plt.boxplot(X_data, Y_data)
        plt.title(f'Ran algorithms {amount_of_times_run} times on 6x6_1')
        plt.xlabel('Algorithms')
        plt.ylabel('Average amount of moves made')
        return plt.show()
    
    def Time_spent_run():
        None