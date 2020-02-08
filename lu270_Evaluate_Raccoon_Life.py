#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 19:17:25 2020

@author: lu270
"""

## import useful tool
import math
## open file
file = open("2008Male00006.txt","r")
## read file by lines
lines = file.readlines()
file.close()
## devide the original data into sub list
## remove the first and last row
## separate the data by comma
## take colmns needed
data = [0]*len(lines)
for i in range(1,len(lines)-1):
    data[i] = lines[i].strip().split(',')
    data[i][3:4] = map(str,data[i][3:4])
    data[i][4:6]  = map(float, data[i][4:6])
    data[i][8:15]  = map(float, data[i][8:15])
print (data)
  
## remove 0's in the first and last spot
data.pop(0)
data.pop(-1)
## first row
firstrow = lines[0].strip().split(',')
## build dictionary
dic = {firstrow[i]:[row[i] for row in data] for i in range(len(firstrow))}
## build fuctions

def mean(a):
    mean=sum(a)/len(a)
    return mean

## calculate values
ave_X = mean(dic[' X'])
ave_Y = mean(dic[' Y'])
ave_EL = mean(dic['Energy Level'])
dist = []
for i in range(len([' X'])):
    if i > 0:
        dist.append(math.sqrt((dic[' X'][i])-dic[' X'][i-1])**2+(dic[' Y'][i]-dic[' Y'][i-1])**2)
    dist.insert(0,0)

dic['Distance Traveled'] = dist
sum_dist = sum(dic['Distance Traveled'])

## new header

line = ['Raccoon name: <George>','Average Location:<'+ str(ave_X) +'>, <'+ str(ave_Y)+'>',
        'Distance traveled: <'+str(sum_dist)+'>','Average energy level: <'+ str(ave_EL)+'>',
        'Raccoon end status: <George number 6 died from starvation>']

f1 = open('Georges_life.txt','w')

## create new txt file with header
for i in range(len(line)):
    f1.write(line[i])
    f1.write('\n')
f1.write('\n')

## write data
for i in range(len(data)):
    for j in range(len(data[i])):
        if 0<j<3 or 4<j<9:
            f1.write(str(data[i][j]))
            f1.write('\t')
    f1.write('\n')
f1.close













