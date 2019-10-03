import tkinter as tk
from tkinter import filedialog
import os
import sys
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class experiment():
    def __init__(self, x_axis_1_data, x_axis_2_data):
        self.x_axis_1_data = x_axis_1_data
        self.x_axis_2_data = x_axis_2_data
        self.axes = []
        self.axes.append(self.x_axis_1_data)
        self.axes.append(self.x_axis_2_data)

class axis_data():
    def __init__(self, n1, n2, n3, n4, n5):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n = []
        self.n.append(self.n1)
        self.n.append(self.n2)
        self.n.append(self.n3)
        self.n.append(self.n4)
        self.n.append(self.n5)

def define_input_files():
    files = []
    files.append("scaling_analysis_data1.txt")
    files.append("scaling_analysis_data2.txt")
    files.append("scaling_analysis_data3.txt")
    files.append("scaling_analysis_data4.txt")
    files.append("scaling_analysis_data5.txt")
    files.append("scaling_analysis_data6.txt")
    files.append("scaling_analysis_data7.txt")
    return files

def load_data_sets(files):
    data = []
    with open(files[0]) as f:
        data1 = f.readlines()
    for i in range(len(data1)):
        string = data1[i]
        data1[i] = string[:-1]
    with open(files[1]) as f:
        data2 = f.readlines()
    for i in range(len(data2)):
        string = data2[i]
        data2[i] = string[:-1]
    with open(files[2]) as f:
        data3 = f.readlines()
    for i in range(len(data3)):
        string = data3[i]
        data3[i] = string[:-1]
    with open(files[3]) as f:
        data4 = f.readlines()
    for i in range(len(data4)):
        string = data4[i]
        data4[i] = string[:-1]
    with open(files[4]) as f:
        data5 = f.readlines()
    for i in range(len(data5)):
        string = data5[i]
        data5[i] = string[:-1]
    with open(files[5]) as f:
        data6 = f.readlines()
    for i in range(len(data6)):
        string = data6[i]
        data6[i] = string[:-1]
    with open(files[6]) as f:
        data7 = f.readlines()
    for i in range(len(data7)):
        string = data7[i]
        data7[i] = string[:-1]
    data.append(data1)
    data.append(data2)
    data.append(data3)
    data.append(data4)
    data.append(data5)
    data.append(data6)
    data.append(data7)
    return data

def preprocess_data(data):
    # read experiments data
    experiments = []
    for j in range(len(data)):
        data_set = data[j]

        #print(data_set[0])

        # read axis data
        axes = []
        for i in range(len(data_set)):
            line = data_set[i]
            #print(line)
            pos = line.find("[")
            line = line[pos:]
            #print(line)
            line = line[1:]
            #print(line)
            line = line[:-1]
            #print(line)
            line = line.replace(" ","")
            line = line.split(",")
            #print(line)
            #print(line[0])
            n1 = float(line[0])
            n2 = float(line[1])
            n3 = float(line[2])
            n4 = float(line[3])
            n5 = float(line[4])

            a = axis_data(n1,n2,n3,n4,n5)
            axes.append(a)
        e = experiment(axes[0],axes[1])
        experiments.append(e)
    return experiments

def make_plot(title,r1,r2,r3,r4,r5,r6,r7):
    labels = ["$\\bf{7 points}$"]
    rows = ["$\\bf{R=1}$","$\\bf{R=2}$","$\\bf{R=3}$","$\\bf{R=4}$","$\\bf{R=5}$","$\\bf{R=6}$","$\\bf{R=7}$"]
    x = np.arange(len(labels))  # the label locations
    width = 0.1  # the width of the bars
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize = (6,6) )
    #ax_table.axis("off")
    ax.set_axisbelow(True)
    ax.grid(linestyle='dashed', axis='y')
    rects1 = ax.bar(x - width*3, r1, width, label='R=1')
    rects2 = ax.bar(x - width*2, r2, width, label='R=2')
    rects3 = ax.bar(x - width, r3, width, label='R=3')
    rects4 = ax.bar(x, r4, width, label='R=4')
    rects5 = ax.bar(x + width, r5, width, label='R=5')
    rects6 = ax.bar(x + width*2, r6, width, label='R=6')
    rects7 = ax.bar(x + width*3, r7, width, label='R=7')
    cells = []
    cells.append(r1)
    cells.append(r2)
    cells.append(r3)
    cells.append(r4)
    cells.append(r5)
    cells.append(r6)
    cells.append(r7)

    """
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
    """

    #the_table = ax_table.table(cellText=cells,
    #                  rowLabels=rows,
#                      colLabels=labels,
#                      loc='center',
#                      cellLoc='center')
    ax.set_ylabel('Correct models [%]')
    ax.set_xlabel('Modeler configuration')
    ax.set_title(title)
    ax.set_ylim(0,100)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_yticks(np.arange(0, 110, step=10))
    ax.legend(loc='upper center', title="Number of repetitions per measurement point",
    bbox_to_anchor=(0.5, -0.25), ncol=7, fontsize = 'x-small', prop={'size': 8})

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, -15),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    autolabel(rects4)
    autolabel(rects5)
    autolabel(rects6)
    autolabel(rects7)

    fig.tight_layout()
    fig.savefig(title+'.pdf', dpi = 300)
    #plt.show()

def define_all_titles():
    titles = []
    titles.append("Scaling for x-axis - P(512) - n=1x5")
    titles.append("Scaling for x-axis - P(512) - n=2x5")
    titles.append("Scaling for x-axis - P(512) - n=3x5")
    titles.append("Scaling for x-axis - P(512) - n=4x5")
    titles.append("Scaling for x-axis - P(512) - n=5x5")
    titles.append("Scaling for x-axis - P(1024) - n=1x5")
    titles.append("Scaling for x-axis - P(1024) - n=2x5")
    titles.append("Scaling for x-axis - P(1024) - n=3x5")
    titles.append("Scaling for x-axis - P(1024) - n=4x5")
    titles.append("Scaling for x-axis - P(1024) - n=5x5")
    return titles

def make_all_plots(experiments):
    titles = define_all_titles()
    counter = 0
    for i in range(2):
        for j in range(5):
            title = titles[counter]
            r1 = experiments[0].axes[i].n[j]
            r2 = experiments[1].axes[i].n[j]
            r3 = experiments[2].axes[i].n[j]
            r4 = experiments[3].axes[i].n[j]
            r5 = experiments[4].axes[i].n[j]
            r6 = experiments[5].axes[i].n[j]
            r7 = experiments[6].axes[i].n[j]
            make_plot(title,r1,r2,r3,r4,r5,r6,r7)
            counter += 1

if __name__ == "__main__":

    # define input files
    files = define_input_files()

    # load data sets
    data = load_data_sets(files)

    # preprocess data
    experiments = preprocess_data(data)

    # make the plots
    make_all_plots(experiments)
