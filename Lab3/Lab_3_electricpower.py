# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 02:33:19 2015

@author: nymph
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


############################## Your code for loading and preprocess the data ##
# NOTE: Load dataset household_power_consumption 
INPUT_FILE = "./data/household_power_consumption.txt"
OUTPUT_IMAGE = "./images/"

# Load dataset household_power_consumption 
def load_data(input_file):
   df = pd.read_csv(input_file, 
                  sep=';', 
                  parse_dates={'Datetime': ['Date', 'Time']}, 
                  infer_datetime_format=True, 
                  low_memory=False,
                  na_values=['nan','?'],
                  index_col='Datetime')
   return df

data = load_data(INPUT_FILE)
# print("-------------LOAD DATA----------------")
# print(data.head())

# NOTE: Preprocessing data
def preprocessing_data(data):
   ## finding all columns that have nan:
   droping_list_all=[]
   for j in range(0,7):
      if not data.iloc[:, j].notnull().all():
         droping_list_all.append(j)     
   
   # filling nan with mean in any columns
   for i in droping_list_all:
      data.iloc[:,i]=data.iloc[:,i].fillna(data.iloc[:,i].mean())
   return data

data = preprocessing_data(data)

print(f"-------------AFTER PREPROCESSING DATA----------------")
print(data.isnull().sum())
print(data.head())


############################ Complete the following 4 functions ###############
data_sub = data.loc['2007-02-01':'2007-02-02']

def plot1(df):
   plt.figure(figsize=(10,5))
   plt.hist(df['Global_active_power'], bins=13, color='red', edgecolor='black', linewidth=1)
   plt.xlabel('Global Active Power (kilowatts)')
   plt.ylabel('Frequency')
   plt.gca().spines[['top','right']].set_visible(False)
   plt.xticks(np.arange(0, 8, 2))
   plt.title('Global Active Power')
   plt.ylim(0,1400)
   plt.xlim(0,6,2)
   plt.savefig(OUTPUT_IMAGE + 'plot1.png')
   plt.show()

def plot2(df):
    plt.figure(figsize=(10,5))
    plt.plot(df.index, df['Global_active_power'], color='black')
    plt.xlabel('datetime')
    plt.ylabel('Global Active Power (kilowatts)')
    plt.title('Global Active Power')
    plt.savefig(OUTPUT_IMAGE + 'plot2.png')
    plt.show()

def plot3(df):
    plt.figure(figsize=(10,5))
    plt.plot(df.index, df['Sub_metering_1'], color='black')
    plt.plot(df.index, df['Sub_metering_2'], color='red')
    plt.plot(df.index, df['Sub_metering_3'], color='blue')
    plt.xlabel('datetime')
    plt.ylabel('Energy sub metering')
    plt.title('Energy sub metering')
    plt.legend(['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'], loc='upper right')
    plt.savefig(OUTPUT_IMAGE + 'plot3.png')
    plt.show()

def plot4(df):
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs[0, 0].plot(df.index, df['Global_active_power'], color='black')
    axs[0, 0].set_ylabel('Global Active Power')

    axs[1, 0].plot(df.index, df['Sub_metering_1'], color='black')
    axs[1, 0].plot(df.index, df['Sub_metering_2'], color='red')
    axs[1, 0].plot(df.index, df['Sub_metering_3'], color='blue')
    axs[1, 0].set_ylabel('Energy sub metering')
    axs[1, 0].legend(['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3'], loc='upper right')

    axs[0, 1].plot(df.index, df['Voltage'], color='black')
    axs[0, 1].set_xlabel('datetime')
    axs[0, 1].set_ylabel('Voltage')
        
    axs[1, 1].plot(df.index, df['Global_reactive_power'], color='black')
    axs[1, 1].set_xlabel('datetime')
    axs[1, 1].set_ylabel('Global_reactive_power')

    plt.savefig(OUTPUT_IMAGE + 'plot4.png')
    plt.show()

plot1(data_sub)
plot2(data_sub)
plot3(data_sub)
plot4(data_sub)
