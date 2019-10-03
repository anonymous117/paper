import tkinter as tk
from tkinter import filedialog
import os
import sys
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import shutil
import re
import csv

def load_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def convert_data(data):
    output = []
    output.append(float(data[0][0]))
    output.append(float(data[0][1]))
    return output

def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

def make_plot(term_data, title):
    labels = ["$\\bf{R1}$","$\\bf{R2}$","$\\bf{R3}$","$\\bf{R4}$","$\\bf{R5}$","$\\bf{R6}$","$\\bf{R7}$"]
    rows = ["Incorrect","Identical"]
    x = np.arange(len(labels))  # the label locations
    zero = []
    one = []
    for i in range(len(term_data)):
        zero.append(term_data[i][0])
        one.append(term_data[i][1])
    ind = np.arange(len(zero))
    N = 7
    incorrect = np.array(zero)
    identical = np.array(one)
    fig, (ax, ax_table) = plt.subplots(nrows=2, ncols=1, figsize = (6,6) )
    ax_table.axis("off")
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    p2 = ax.bar(ind, incorrect, width, color="red", label="incorrect")
    p1 = ax.bar(ind, identical, width, bottom=incorrect, color="green", label="identical")
    ax.set_axisbelow(True)
    ax.grid(linestyle='dashed', axis='y')
    cells = []
    cells.append(zero)
    cells.append(one)
    the_table = ax_table.table(cellText=cells,
                      rowLabels=rows,
                      colLabels=labels,
                      loc='center',
                      cellLoc='center')
    ax.set_ylabel('Percentage of models [%]')
    ax.set_title(title)
    ax.set_xlabel('Modeler configuration')
    ax.set_ylim(0,100)
    ax.set_yticks(np.arange(0, 110, step=10))
    ax.set_xticklabels(labels)
    ax.set_xticks(x)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=3, fontsize = 'x-small', prop={'size': 8})
    fig.tight_layout()
    plt.subplots_adjust(left=0.15)
    fig.savefig(title+'.pdf', dpi = 300)
    #plt.show()

if __name__ == '__main__':
    folders = []
    folders.append("data1/")
    folders.append("data2/")
    folders.append("data3/")
    folders.append("data4/")
    folders.append("data5/")
    folders.append("data6/")
    folders.append("data7/")
    title = "Term analysis for P=6 and N=5"
    number_function_terms = 2
    iterations = 100
    repetitions = 10
    number_of_functions = iterations * repetitions
    percentage_term_data = []

    for i in range(len(folders)):
        path = folders[i]
        # load all data for plotting
        #percentage_errors = load_csv(path+"percentage_errors.csv")
        #percentage_errors = convert_data(percentage_errors)
        temp = load_csv(path+"percentage_term_data.csv")
        temp = convert_data(temp)
        percentage_term_data.append(temp)

    # create the plot
    make_plot(percentage_term_data, title)
