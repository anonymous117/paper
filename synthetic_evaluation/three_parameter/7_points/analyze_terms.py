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

def make_plot_1(term_data, percentage_errors):
    zero = []
    one = []
    two = []
    for i in range(len(term_data)):
        zero.append(term_data[i][0])
        one.append(term_data[i][1])
        two.append(term_data[i][2])
    ind = np.arange(len(zero))
    width = 0.2
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind-width, zero, width, color='red', label='model is incorrect')
    rects2 = ax.bar(ind, one, width, color='orange', label='lead order term correct')
    rects3 = ax.bar(ind+width, two, width, color='green', label='model is identical')
    ax2 = ax.twinx()
    ax2.semilogy(ind, percentage_errors, "b-^")
    #ax2.plot(ind, percentage_errors, "b^-")
    ax2.set_ylabel('Relative error [%]')
    ax.set_ylabel('Correct models [%]')
    #ax.set_title('title')
    ax.set_xticks(ind)
    ax.set_xticklabels((""))
    ax.set_xlabel('Modeler configuration')
    fig.tight_layout()
    ax.legend(loc='upper right')
    plt.show()

def load_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def convert_data(data):
    output = []
    for i in range(len(data)):
        output.append(float(data[i][0]))
    return output

def convert_data2(data):
    output = []
    for i in range(len(data)):
        temp = []
        temp.append(float(data[i][0]))
        temp.append(float(data[i][1]))
        temp.append(float(data[i][2]))
        output.append(temp)
    return output

def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

def make_plot(term_data, percentage_errors, title):
    labels = ["$\\bf{B125}$","$\\bf{S13}$","$\\bf{S14}$","$\\bf{S15}$","$\\bf{S25}$","$\\bf{S75}$","$\\bf{S125}$"]
    rows = ["Incorrect","Lead","Identical"]
    x = np.arange(len(labels))  # the label locations
    zero = []
    one = []
    two = []
    for i in range(len(term_data)):
        zero.append(term_data[i][0])
        one.append(term_data[i][1])
        two.append(term_data[i][2])
    ind = np.arange(len(zero))
    N = 7
    incorrect = np.array(zero)
    lead = np.array(one)
    identical = np.array(two)
    fig, (ax, ax_table) = plt.subplots(nrows=2, ncols=1, figsize = (6,6) )
    ax_table.axis("off")
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    p3 = ax.bar(ind, incorrect, width, color="red", label="incorrect")
    p2 = ax.bar(ind, lead, width, bottom=incorrect, color="yellow", label="lead order term correct")
    p1 = ax.bar(ind, identical, width, bottom=incorrect+lead, color="green", label="identical")
    ax.set_axisbelow(True)
    ax.grid(linestyle='dashed', axis='y')
    ax2 = ax.twinx()
    ax2.semilogy(ind, percentage_errors, "kD", label="MPE")
    cells = []
    cells.append(zero)
    cells.append(one)
    cells.append(two)
    the_table = ax_table.table(cellText=cells,
                      rowLabels=rows,
                      colLabels=labels,
                      loc='center',
                      cellLoc='center')
    ax2.set_ylabel('MPE [%]')
    ax.set_ylabel('Correct models [%]')
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
    titles = []
    titles.append("Term analysis for R=1 and N=5")
    titles.append("Term analysis for R=2 and N=5")
    titles.append("Term analysis for R=3 and N=5")
    titles.append("Term analysis for R=4 and N=5")
    titles.append("Term analysis for R=5 and N=5")
    titles.append("Term analysis for R=6 and N=5")
    titles.append("Term analysis for R=7 and N=5")
    number_function_terms = 2
    iterations = 100
    repetitions = 10
    number_of_functions = iterations * repetitions
    for i in range(len(folders)):
        path = folders[i]
        title = titles[i]
        # load all data for plotting
        percentage_errors = load_csv(path+"percentage_errors.csv")
        percentage_errors = convert_data(percentage_errors)
        percentage_term_data = load_csv(path+"percentage_term_data.csv")
        percentage_term_data = convert_data2(percentage_term_data)
        # create the plot
        make_plot(percentage_term_data, percentage_errors, title)
