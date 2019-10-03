import tkinter as tk
from tkinter import filedialog
import os
import sys
from math import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

def get_file_names(path):
        return os.listdir(path)

def parse_to_python_function(function):
    # remove leading + for the first coefficient
    if function[0] == ' ':
        function = function[1:]
    if function[0] == '+':
        function = function[1:]
    if function[0] == ' ':
        function = function[1:]
    # replace power operator ^ with **
    while True:
        id = 0
        complete = True
        for i in range(0,len(function)):
            if function[i] == '^':
                id = i
                complete = False
                break
        if complete == True:
            break
        temp = function[:id]
        temp2 = function[id+2:]
        exponent = function[id+1]
        temp2 = '**' + exponent + temp2
        function = temp + temp2
    # replace log operator log2(x) with log(x,2)
    while True:
        id = function.find('log2')
        if id == -1:
            break
        else:
            temp = function[:id]
            temp2 = function[id+4:]
            bracket1 = temp2.find('(')
            bracket2 = temp2.find(')')
            parameter = temp2
            parameter = parameter[bracket1+1:]
            idd = parameter.find(')')
            parameter = parameter[:idd]
            temp3 = temp2[:bracket1]
            temp4 = temp2[bracket2+1:]
            temp2 = temp3 + temp4
            function = temp + 'log(' + parameter + ',2)' + temp2
    return function


if __name__ == "__main__":
    path = select_folder()
    folders = get_file_names(path)
    filepaths = []
    for i in range(len(folders)):
        path_folder = path +"/"+ folders[i] + "/"
        files = os.listdir(path_folder)
        for j in range(len(files)):
            path_file = path +"/"+ folders[i] + "/" + files[j]
            filepaths.append(path_file)

    #set parameters
    p_max = 64
    size_max = 50
    n_max = 10
    multiplicators = [2,4,8,16,32]
    noise = int(input("Please input limit for divergence (noise %): "))
    numbers = []
    for _ in range(len(multiplicators)):
        template = []
        for _ in range(7):
            template.append(0)
        numbers.append(template)
    for i in range(len(filepaths)):
        src = filepaths[i]
        with open(src) as f:
            lines = f.readlines()
        for j in range(len(lines)):
            string = lines[j]
            lines[j] = string[:-1]
        for z in range(len(lines)-1):
            baseline_function = lines[0]
            modeled_function = lines[z+1]
            baseline_function_python = parse_to_python_function(baseline_function)
            modeled_function_python = parse_to_python_function(modeled_function)
            for j in range(len(multiplicators)):
                p = p_max * multiplicators[j]
                size = size_max * multiplicators[j]
                n = n_max * multiplicators[j]
                result_base = eval(baseline_function_python)
                result_modeled = eval(modeled_function_python)
                one_percent = result_base / 100
                # limit = max result noise allowed in one direction
                limit = (one_percent * noise)/2
                difference_absolute = abs(result_base - result_modeled)
                
                if difference_absolute > limit:
                    difference_percent = difference_absolute / one_percent
                    #print(difference_absolute)
                    #print(difference_percent)
                    numbers[j][z] = numbers[j][z] + 1

    functions_number = len(filepaths)
    one_percent = functions_number / 100

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            total = numbers[i][j]
            relativ = total / one_percent 
            numbers[i][j] = relativ

    #print("numbers:",numbers)

    results = []
    for i in range(len(numbers)):
        data = []
        for j in range(len(numbers[i])):
            #if j==0 or j==1 or j==2 or j==7 or j==12 or j==17:
            data.append(numbers[i][j])
        results.append(data)

    print("results:",results)

    #plot the data
    zero = []
    one = []
    two = []
    three = []
    four = []
    for j in range(len(results[0])):
        zero.append(numbers[0][j])
        one.append(numbers[1][j])
        two.append(numbers[2][j])
        three.append(numbers[3][j])
        four.append(numbers[4][j])

    ind = np.arange(7)  # the x locations for the groups
    width = 0.1  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind-width*2, zero, width,
                    color='red', label='2x')
    rects2 = ax.bar(ind-width, one, width,
                    color='green', label='4x')
    rects3 = ax.bar(ind + width-width, two, width,
                    color='blue', label='8x')
    rects4 = ax.bar(ind + width*2-width, three, width,
                    color='yellow', label='16x')
    rects5 = ax.bar(ind + width*3-width, four, width,
                    color='gray', label='32x')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Incorrect Models [%]')
    ax.set_xticks(ind)
    ax.set_xticklabels(('B125', 'S13', 'S14', 'S15', 'S25', 'S75', 'S125'))
    ax.legend(title='Scaling factor for max. p, size')
    plt.show()
