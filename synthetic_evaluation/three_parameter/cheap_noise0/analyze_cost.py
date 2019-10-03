import tkinter as tk
from tkinter import filedialog
import os
import sys
import copy
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

class Measurement:
    def __init__(self,p,s,n,v,c):
        self.p = p
        self.s = s
        self.n = n
        self.v = v
        self.c = c

if __name__ == "__main__":
    path = select_folder()
    folders = get_file_names(path)
    s13_percentages = []
    s14_percentages = []
    for i in range(len(folders)):
        files = get_file_names(path+"/"+folders[i])
        for j in range(len(files)):
            file = path+"/"+folders[i]+"/"+files[j]
            with open(file) as f:
                lines = f.readlines()
            points = []
            for k in range(len(lines)):
                #print(lines[k])
                p = lines[k]
                pos = p.find("\"p\"")
                p = p[pos+4:]
                pos = p.find(",")
                p = p[:pos]
                p = float(p)
                #print("p:",p)
                v = lines[k]
                pos = v.find("value")
                v = v[pos+7:]
                pos = v.find("}")
                v = v[:pos]
                v = float(v)
                #print("time:",v)
                c = p * v
                #print("cost:",c)
                s = lines[k]
                pos = s.find("size")
                s = s[pos+6:]
                pos = s.find(",")
                s = s[:pos]
                s = float(s)
                #print("size:",s)
                n = lines[k]
                pos = n.find("n")
                n = n[pos+3:]
                pos = n.find("}")
                n = n[:pos]
                n = float(n)
                #print("n:",n)
                points.append(Measurement(p,s,n,v,c))
            points2 = []
            counter = 0
            for k in range(len(points)):
                if counter == 5:
                    counter = 0
                if counter == 0:
                    points2.append(points[k])
                counter += 1      
            points2 = sorted(points2, key=lambda Measurement: Measurement.c)
            
            total_cost = 0
            for k in range(len(points2)):
                total_cost += points2[k].c
            #print("total cost:",total_cost)

            s13_points = []
            for k in range(len(points2)):
                if points2[k].p == 4:
                    if points2[k].s == 10:
                        if points2[k].n == 4:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 10:
                        if points2[k].n == 6:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 10:
                        if points2[k].n == 8:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 10:
                        if points2[k].n == 10:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 10:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 20:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 30:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 40:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 4:
                    if points2[k].s == 50:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 8:
                    if points2[k].s == 10:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 16:
                    if points2[k].s == 10:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 32:
                    if points2[k].s == 10:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                if points2[k].p == 64:
                    if points2[k].s == 10:
                        if points2[k].n == 2:
                            s13_points.append(points2[k])
                
            s14_points = copy.deepcopy(s13_points)
            for k in range(len(points2)):
                if points2[k].p == 4:
                    if points2[k].s == 20:
                        if points2[k].n == 4:
                            s14_points.append(points2[k])

            #print(" --- S13 --- ")

            total_s13_cost = 0
            for k in range(len(s13_points)):
                total_s13_cost += s13_points[k].c
                #print(str(s13_points[k].p)+" "+str(s13_points[k].s)+" "+str(s13_points[k].n)+" "+str(s13_points[k].c))
            #print("total cost s13:",total_s13_cost)
            one_percent_cost = total_cost / 100
            percent_s13_cost = total_s13_cost / one_percent_cost
            #print("percent cost s13:",percent_s13_cost)
            s13_percentages.append(percent_s13_cost)

            #print(" --- S14 --- ")

            total_s14_cost = 0
            for k in range(len(s14_points)):
                total_s14_cost += s14_points[k].c
                #print(str(s14_points[k].p)+" "+str(s14_points[k].s)+" "+str(s14_points[k].n)+" "+str(s14_points[k].c))
            #print("total cost s14:",total_s14_cost)
            percent_s14_cost = total_s14_cost / one_percent_cost
            #print("percent cost s14:",percent_s14_cost)
            s14_percentages.append(percent_s14_cost)

            #print(" --- NEW --- ")
            

    #print(s13_percentages)
    print("S13 elements:",len(s13_percentages))
    sum_s13_percentages = 0
    for i in range(len(s13_percentages)):
        sum_s13_percentages += s13_percentages[i]
    print("S13 total percentage sum:",sum_s13_percentages)
    s13_average_percent = sum_s13_percentages / len(s13_percentages)
    print("S13 average percent cost:",s13_average_percent)

    #print(s14_percentages)
    print("S14 elements:",len(s14_percentages))
    sum_s14_percentages = 0
    for i in range(len(s14_percentages)):
        sum_s14_percentages += s14_percentages[i]
    print("S14 total percentage sum:",sum_s14_percentages)
    s14_average_percent = sum_s14_percentages / len(s14_percentages)
    print("S14 average percent cost:",s14_average_percent)
