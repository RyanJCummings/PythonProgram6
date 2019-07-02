# ----------------------------------------------------------------
# Program 6: Pandas
# CSCI 127
# Ryan Cummings
# Last Modified: 12/08/2017
# ----------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------
# processes data file and creates scatter plot showing age, relative
# value and construction class of buildings on campus
# ----------------------------------------------------------------
def scatter(dataFrame):
    scatter_data = pd.DataFrame(data=dataFrame, columns=['Construction Class', 'Year Built', 'Building Value'])

    n = scatter_data['Building Value']
    x = scatter_data['Year Built']
    y = scatter_data['Construction Class']

    window = plt.figure()
    window.canvas.set_window_title("CSCI 127, Program 6")
    plt.scatter(x, y, s=0.00001*n, marker='o', color='b')
    plt.title("Age, Construction Class, and Relative Value of Buildings")
    plt.xlabel("Year Built")
    plt.ylabel("Construction Class")
    
    plt.legend(['Dot Size = Relative Value'])
    plt.show()

# ----------------------------------------------------------------
# process data file and plots percentage of high HazMat risk buildings
# with backup power, fire sprinklers, both, and neither
# ----------------------------------------------------------------
def pie_chart(dataFrame):
# processes data
    pie_data = pd.DataFrame(data=dataFrame, columns=['HazMat Risk', 'Backup Power', 'Fire Sprinklers'])
    hazardous = pie_data[pie_data['HazMat Risk'] == 'H']
    
    power_only = hazardous[(hazardous['Backup Power'] == 'Y') & (hazardous['Fire Sprinklers'] == 'N')]
    sprinkler_only = hazardous[(hazardous['Backup Power'] =='N') & (hazardous['Fire Sprinklers'] == 'Y')]
    neither = hazardous[(hazardous['Backup Power'] == 'N') & (hazardous['Fire Sprinklers'] == 'N')]
    both = hazardous[(hazardous['Backup Power'] == 'Y') & (hazardous['Fire Sprinklers'] == 'Y')]

    hazard_len = len(hazardous)
    both_percent = len(both)/hazard_len
    neither_percent = len(neither)/hazard_len
    sprinkler_percent = len(sprinkler_only)/hazard_len
    power_percent = len(power_only)/hazard_len

# creates pie chart
    labels = 'Sprinklers Only', 'Backup Power Only', 'Both', 'Neither', 'Partial'
    sizes = [sprinkler_percent, power_percent, both_percent, neither_percent]
    other = 1 - sum(sizes)
    sizes.append(other)
    explode = [0, 0, 0, 0.1, 0]

 
    fig, ax1 = plt.subplots()
    fig.canvas.set_window_title('CSCI 127, Program 6')
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=15)
    ax1.axis('equal')
    plt.title("Emergency Preparedness in Buildings with High HazMat Risk") 
    plt.show()
    
# ----------------------------------------------------------------
def main():
    data = pd.read_csv('buildings.csv')
    scatter(data)
    pie_chart(data)
# ---------------------------------------------------------------- 
main()
