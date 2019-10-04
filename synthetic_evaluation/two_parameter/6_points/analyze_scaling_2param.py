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

    noise = int(input("Please input limit for divergence (noise %): "))
    print("Noise level set to "+str(noise)+"%.")

    print("percentage of correct models per [noise factor][modeler configuration].")

    data_set = []

    ########################################################################################################################################################

    # for scaling along all axis 1 step further
    P = 256
    S = 70
    #N = 12
    results = []
    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*2:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*3:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*4:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*5:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    #print(results)
    functions_number = len(filepaths)
    #print("total functions:",functions_number)
    one_percent = functions_number / 100
    for i in range(len(results)):
        for j in range(len(results[i])):
            total = results[i][j]
            relativ = total / one_percent
            results[i][j] = relativ
    #print(results)
    for i in range(len(results)):
        for j in range(len(results[i])):
            incorrect = results[i][j]
            correct = 100 - incorrect
            results[i][j] = correct
    print("all axis 1 step further:",results)
    data = "all axis 1 step further:"+str(results)
    data_set.append(data)

    ###################################################################################################################################

    # for scaling along all axis 2 step further
    P = 512
    S = 80
    #N = 12
    results = []
    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*2:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*3:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*4:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*5:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    #print(results)
    functions_number = len(filepaths)
    #print("total functions:",functions_number)
    one_percent = functions_number / 100
    for i in range(len(results)):
        for j in range(len(results[i])):
            total = results[i][j]
            relativ = total / one_percent
            results[i][j] = relativ
    #print(results)
    for i in range(len(results)):
        for j in range(len(results[i])):
            incorrect = results[i][j]
            correct = 100 - incorrect
            results[i][j] = correct
    print("all axis 2 step further:",results)
    data = "all axis 2 step further:"+str(results)
    data_set.append(data)

    ###################################################################################################################################

    # for scaling along x-axis 1 step further
    P = 256
    S = 10
    #N = 2
    results = []
    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*2:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*3:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*4:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*5:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    #print(results)
    functions_number = len(filepaths)
    #print("total functions:",functions_number)
    one_percent = functions_number / 100
    for i in range(len(results)):
        for j in range(len(results[i])):
            total = results[i][j]
            relativ = total / one_percent
            results[i][j] = relativ
    #print(results)
    for i in range(len(results)):
        for j in range(len(results[i])):
            incorrect = results[i][j]
            correct = 100 - incorrect
            results[i][j] = correct
    print("x-axis 1 step further:",results)
    data = "x-axis 1 step further:"+str(results)
    data_set.append(data)

    ###################################################################################################################################

    # for scaling along x-axis 2 step further
    P = 512
    S = 10
    #N = 2
    results = []
    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*2:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*3:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*4:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*5:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    #print(results)
    functions_number = len(filepaths)
    #print("total functions:",functions_number)
    one_percent = functions_number / 100
    for i in range(len(results)):
        for j in range(len(results[i])):
            total = results[i][j]
            relativ = total / one_percent
            results[i][j] = relativ
    #print(results)
    for i in range(len(results)):
        for j in range(len(results[i])):
            incorrect = results[i][j]
            correct = 100 - incorrect
            results[i][j] = correct
    print("x-axis 2 step further:",results)
    data = "x-axis 2 step further:"+str(results)
    data_set.append(data)

    ###################################################################################################################################

    # for scaling along y-axis 1 step further
    P = 4
    S = 70
    #N = 2
    results = []
    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*2:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*3:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*4:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*5:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    #print(results)
    functions_number = len(filepaths)
    #print("total functions:",functions_number)
    one_percent = functions_number / 100
    for i in range(len(results)):
        for j in range(len(results[i])):
            total = results[i][j]
            relativ = total / one_percent
            results[i][j] = relativ
    #print(results)
    for i in range(len(results)):
        for j in range(len(results[i])):
            incorrect = results[i][j]
            correct = 100 - incorrect
            results[i][j] = correct
    print("y-axis 1 step further:",results)
    data = "y-axis 1 step further:"+str(results)
    data_set.append(data)

    ###################################################################################################################################

    # for scaling along y-axis 2 step further
    P = 4
    S = 80
    #N = 2
    results = []
    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*2:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*3:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*4:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    numbers = []
    for _ in range(7):
        numbers.append(0)
    #print(numbers)
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
            #for j in range(len(multiplicators)):
            p = P
            size = S
            #n = N
            result_base = eval(baseline_function_python)
            result_modeled = eval(modeled_function_python)
            one_percent = result_base / 100
            # limit = max result noise allowed in one direction
            limit = (one_percent * noise)
            #print(limit)
            difference_absolute = abs(result_base - result_modeled)
            if difference_absolute > limit*5:
                #difference_percent = difference_absolute / one_percent
                numbers[z] += 1
    #print(numbers)
    results.append(numbers)

    #print(results)
    functions_number = len(filepaths)
    #print("total functions:",functions_number)
    one_percent = functions_number / 100
    for i in range(len(results)):
        for j in range(len(results[i])):
            total = results[i][j]
            relativ = total / one_percent
            results[i][j] = relativ
    #print(results)
    for i in range(len(results)):
        for j in range(len(results[i])):
            incorrect = results[i][j]
            correct = 100 - incorrect
            results[i][j] = correct
    print("y-axis 2 step further:",results)
    data = "y-axis 2 step further:"+str(results)
    data_set.append(data)

    ###################################################################################################################################

    filename = input("Please input the filename for the result file: ")
    f = open(str(filename)+".txt", "w")
    for i in range(len(data_set)):
        line = data_set[i]
        f.write(line+"\n")
    f.close()
