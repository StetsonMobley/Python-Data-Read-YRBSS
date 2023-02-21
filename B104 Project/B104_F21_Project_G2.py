#Class: B104 Computer Programming Techniques
# Year: 2021 Fall Semester
#Programmers: Stetson Mobley [sdmobley@email.uscb.edu],
#Bao Pham [bpham@email.uscb.edu], Victor Lin [vwlin@email.sc.edu]
#Group: 2
#Assignment: Final Project Python Script


# Test of two continuous numeric data

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#from scipy.stats import chi2_contingency

from pandas import *
data = read_csv("csv_datasheet.csv")
quest23 = data['q23'] #bullied the past year Y/N
quest26 = data['q26'] #consider suicide past year Y/N
quest28 = data['q28'] #attempt suicide past year 0(1.0), 1, 2(2-3, 3.0), 3(4-5, 4.0), 4(6+, 5.0)
quest1 = data['q1'] #age
quest2 = data['q2'] #sex
quest3 = data['q3'] #grade 
quest6 = data['q6'] #height
quest7 = data['q7'] #weight


def DashLoop(): #quick practice with python functions
    print("-"*60)


df = pd.read_csv('csv_datasheet.csv')
myCrosstable = pd.crosstab(df.q23, df.q26, margins=True, rownames=["Q23"], colnames=["Q26"])
print(myCrosstable)

DashLoop()

# https://www.youtube.com/watch?v=hTsxJqw2zMM link used to do this coding of Chi-test

# chiVal, pVal, dof, exp = chi2_contingency(myCrosstable)
# print(chiVal, pVal, dof, exp)


#Hard-coded bar chart
# This graph will be changed probably frequently to accomodate for what I want
# from matplotlib import pyplot as plt
# plt.style.use('seaborn')
# questx = ['Been Bullied', 'Considered Suicide'] #for Question 23
# questy = [2657, 2587]
# plt.bar(questx, questy)
# plt.title('Number of Bullied Kids & Number of Considered Suicide', fontsize=14)
# # plt.xlabel('Yes / No', fontsize=14)
# plt.ylabel('Number of answers', fontsize=14)
# plt.show()
# https://datatofish.com/bar-chart-python-matplotlib/


#This is the main graph that shows the whole chi-square
yesBoth = 0
yes23No26 = 0
yes26No23 = 0
noBoth = 0
noAns = 0

for a, b in zip(quest23, quest26):
    if(a == 1 and b == 1):
        yesBoth += 1
    elif(a == 1 and b == 2):
        yes23No26 += 1
    elif(a == 2 and b == 1):
        yes26No23 += 1
    elif(a == 2 and b == 2):
        noBoth += 1
    else:
        noAns += 1
           
plt.style.use('seaborn')
questx1 = ['Yes to both', 'Yes to Bullied Only', 'Yes to Suicide Only', 'No to Both', 'No Answer'] #for Question 23
questy1 = [yesBoth, yes23No26, yes26No23, noBoth, noAns] #Hardcoded the values from the chi-test
plt.bar(questx1, questy1)
plt.title('Chi-square results to being Bullied and Considering Suicide', fontsize=14)
#plt.xlabel('Yes / No', fontsize=14)
plt.ylabel('Number of answers', fontsize=14)
plt.show()

DashLoop()

#Doubled bar graph showing if considering and attempting have any relation

considerAtt0 = 0
considerNoAtt0 = 0
considerAtt1 = 0
considerNoAtt1 = 0
considerAtt2_3 = 0
considerNoAtt2_3 = 0
considerAtt4_5 = 0
considerNoAtt4_5 = 0
considerAtt6 = 0
considerNoAtt6 = 0
blank = 0

for a, b in zip(quest26, quest28): #a is consider 1/2, b is 1-5
    if(a == 1):
        if(b == 1):
            considerAtt0 += 1
        elif(b == 2):
            considerAtt1 += 1
        elif(b == 3):
            considerAtt2_3 += 1
        elif(b == 4):
            considerAtt4_5 += 1
        elif(b == 5):
            considerAtt6 += 1
        else:
            blank += 1
    elif(a == 2):
        if(b == 1):
            considerNoAtt0 += 1
        elif(b == 2):
            considerNoAtt1 += 1
        elif(b == 3):
            considerNoAtt2_3 += 1
        elif(b == 4):
            considerNoAtt4_5 += 1
        elif(b == 5):
            considerNoAtt6 += 1
        else:
            blank += 1
    else:
        blank += 1

X = ['0 times', '1 time', '2-3 times','4-5 times', '6+ times']
consider = [considerAtt0, considerAtt1, considerAtt2_3, considerAtt4_5, considerAtt6]
notconsider = [considerNoAtt0, considerNoAtt1, considerNoAtt2_3, considerNoAtt4_5, considerNoAtt6]
X_axis = np.arange(len(X))
plt.bar(X_axis - 0.2, consider, 0.4, label = 'Considered')
plt.bar(X_axis + 0.2, notconsider, 0.4, label = 'Not Considered')
plt.xticks(X_axis, X)
plt.xlabel("Attempts at Suicide")
plt.ylabel("Number of answers")
plt.title("Considered Suicide and Attempted Suicide")
plt.legend()
plt.show()
#https://geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/

consAtt = pd.crosstab(df.q26, df.q28, margins=True, rownames=["Consider"], colnames=["Attempt"])
print(consAtt)

DashLoop()


#Graph for age and gender

fem12 = 0
fem13 = 0
fem14 = 0
fem15 = 0
fem16 = 0
fem17 = 0
fem18 = 0

man12 = 0
man13 = 0
man14 = 0
man15 = 0
man16 = 0
man17 = 0
man18 = 0
blank = 0

for a, b in zip(quest2, quest1):
    if(a == 1): #if female
        if(b == 1):
            fem12 += 1
        elif(b == 2):
            fem13 += 1
        elif(b == 3):
            fem14 += 1
        elif(b == 4):
            fem15 += 1
        elif(b == 5):
            fem16 += 1
        elif(b == 6):
            fem17 += 1
        elif(b == 7):
            fem18 += 1
        else:
            blank += 1 #if age is blank
    elif(a == 2): #if male
        if(b == 1):
            man12 += 1
        elif(b == 2):
            man13 += 1
        elif(b == 3):
            man14 += 1
        elif(b == 4):
            man15 += 1
        elif(b == 5):
            man16 += 1
        elif(b == 6):
            man17 += 1
        elif(b == 7):
            man18 += 1
        else:
            blank += 1 #if age is blank
    else: #if male/female is blank
        blank += 1
    


X = ['≤12', '13', '14', '15', '16', '17', '≥18']
female = [fem12, fem13, fem14, fem15, fem16, fem17, fem18]
male = [man12, man13, man14, man15, man16, man17, man18]
X_axis = np.arange(len(X))
plt.bar(X_axis - 0.2, female, 0.4, label = 'Female', color='hotpink')
plt.bar(X_axis + 0.2, male, 0.4, label = 'Male', color='deepskyblue')
plt.xticks(X_axis, X)
plt.xlabel("Age")
plt.ylabel("Number of answers")
plt.title("Sex and Ages")
plt.legend()
plt.show()


ageGen = pd.crosstab(df.q1, df.q2, margins=True, rownames=["Age"], colnames=["Sex"])
print(ageGen)

DashLoop()

#Graph for bullied and attempting suicide

bulsui0 = 0
bulsui1 = 0
bulsui2_3 = 0
bulsui4_5 = 0
bulsui6 = 0
notbulsui0 = 0
notbulsui1 = 0
notbulsui2_3 = 0
notbulsui4_5 = 0
notbulsui6 = 0

for a, b in zip(quest23, quest28):
    if(a == 1): #if female
        if(b == 1):
            bulsui0 += 1
        elif(b == 2):
            bulsui1 += 1
        elif(b == 3):
            bulsui2_3 += 1
        elif(b == 4):
            bulsui4_5 += 1
        elif(b == 5):
            bulsui6 += 1
        else:
            blank += 1 #if age is blank
    elif(a == 2): #if male
        if(b == 1):
            notbulsui0 += 1
        elif(b == 2):
            notbulsui1 += 1
        elif(b == 3):
            notbulsui2_3 += 1
        elif(b == 4):
            notbulsui4_5 += 1
        elif(b == 5):
            notbulsui6 += 1
        else:
            blank += 1 #if age is blank
    else: #if male/female is blank
        blank += 1


X = ['0 times', '1 time', '2-3 times','4-5 times', '6+ times']
bullied = [bulsui0, bulsui1, bulsui2_3, bulsui4_5, bulsui6]
notbullied = [notbulsui0, notbulsui1, notbulsui2_3, notbulsui4_5, notbulsui6]
X_axis = np.arange(len(X))
plt.bar(X_axis - 0.2, bullied, 0.4, label = 'Bullied')
plt.bar(X_axis + 0.2, notbullied, 0.4, label = 'Not bullied')
plt.xticks(X_axis, X)
plt.xlabel("Attempts at Suicide")
plt.ylabel("Number of answers")
plt.title("Been Bullied and Attempted Suicide")
plt.legend()
plt.show()

bullyAtt = pd.crosstab(df.q23, df.q28, margins=True, rownames=["Bullied"], colnames=["Attempt"])
print(bullyAtt)

DashLoop()


#Pie Charts
bullyCounter = 0
notBullyCounter = 0
nanCount = 0

for row in quest23:
    if(row == 1):
        bullyCounter += 1
    elif(row == 2):
        notBullyCounter += 1
    else:
        nanCount += 1

y = np.array([bullyCounter, notBullyCounter, nanCount])
mylabels = ['Bullied', 'Not Bullied', 'No Answer']
mycolors = 'dodgerblue', 'cornflowerblue', 'blue'
plt.pie(y, labels = mylabels, colors = mycolors, autopct='%1.1f%%', startangle = 90, shadow =True)
plt.title("Percent of Students Who Have Been Bullied")
plt.show()
#https://www.w3schools.com/python/matplotlib_pie_charts.asp

DashLoop()

suiCounter = 0
notSuiCounter = 0
nanCount = 0

for row in quest26:
    if(row == 1):
        suiCounter += 1
    elif(row == 2):
        notSuiCounter += 1
    else:
        nanCount += 1

y = np.array([suiCounter, notSuiCounter, nanCount])
mylabels = ['Consider Suicide and Bullied', 'Only Consider Suicide', 'No Answer']
mycolors = 'dodgerblue', 'cornflowerblue', 'blue'
plt.pie(y, labels=mylabels, colors=mycolors, autopct='%1.1f%%', shadow=True)
plt.title("All The Students Who Considered Suicide")
plt.show()

DashLoop()

bothCounter = 0
onlyBullyCounter = 0
nullvar = 0
for a, b in zip(quest23, quest26):
    if(a == 1 and b == 1):
        bothCounter += 1
    elif(a == 1 and b == 2):
        onlyBullyCounter += 1
    else:
        nullvar += 1

y = np.array([bothCounter, onlyBullyCounter])
mylabels = ['Consider Suicide and Bullied', 'Only Bullied']
mycolors = 'dodgerblue', 'cornflowerblue'
plt.pie(y, labels=mylabels, colors=mycolors, autopct='%1.1f%%', shadow=True)
plt.title("All The Students Who Were Bullied")
plt.show()

DashLoop()