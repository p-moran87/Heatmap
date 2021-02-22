from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

###################################################################
###                                                             ###
###         Heatmap of TP(%) as a function of vehicle speeds    ###
###                                                             ###
###################################################################


###        Read in the CSV data file                ###


data = csv.reader(open('Data.csv', 'rb'), delimiter=",", quotechar='|')

#######################################################

###       Create arrays for each column            ###

x, y = [], []

########################################################


### Populate each array with the corresponding data  ###


for row in data:
    y.append(row[0])
    x.append(row[1])
    
########################################################


### Store data as numpy arrays ###

x = np.array(x)
y = np.array(y)

#########################################################


### Convert from type String to integer and float ###

x = x.astype(np.int)
y = y.astype(np.float)

########################################################

###  Convert from float to rounded integer ###

y = np.rint(y)

########################################################


### Convert from number of annotations (x) to car speed (kph) [30 fps, distance = 10 m] ###

x = (3.6*10.0)/(x/30.0)
x = np.rint(x)

########################################################


### Combine two 1D arrays into a single 2D array ###

z = np.vstack((x, y)).T

#######################################################


### Create a 2D array full of Zeros np.zeros((R,C)) number of rows and columns ###

map = np.zeros((101,1081))

#######################################################

### Loop through the array elements and count up the occurences of 
### various combinations of TP(%) and Speed

for n in range(0,16068):
    a = y[n]
    b = x[n]
    map[a][b] = map[a][b] + 1
    
#######################################################

### Crop the map to be of the right size 100 Rows x 40 Columns  ###

heatmap = map[0:101,0:41]

######################################################

    
### Plot the heatmap along with a colorbar

plt.imshow(heatmap, extent=(0,40,50,100), cmap='spectral')
plt.ylabel('TP (%)')
plt.xlabel('Speed (kph)')

plt.colorbar()


###########################################################################
###                                                                     ###
### Histogram of TP(%) distribution for various vehicle speeds (kph)    ###
### 0,1,2,3, ... 10 15,20,25,30,35,40 kph                               ###
###                                                                     ###
###########################################################################
   
v0 = heatmap[0:101,0:1]
v1 = heatmap[0:101,1:2]
v2 = heatmap[0:101,2:3]
v3 = heatmap[0:101,3:4]
v4 = heatmap[0:101,4:5]
v5 = heatmap[0:101,5:6]
v6 = heatmap[0:101,6:7]
v7 = heatmap[0:101,7:8]
v8 = heatmap[0:101,8:9]
v9 = heatmap[0:101,9:10]
v10 = heatmap[0:101,10:11]
v11 = heatmap[0:101,11:12]
v12 = heatmap[0:101,12:13]
v13 = heatmap[0:101,13:14]
v14 = heatmap[0:101,14:15]
v15 = heatmap[0:101,15:16]
v16 = heatmap[0:101,16:17]
v17 = heatmap[0:101,17:18]
v18 = heatmap[0:101,18:19]
v19 = heatmap[0:101,19:20]
v20 = heatmap[0:101,20:21]
v21 = heatmap[0:101,21:22]
v22 = heatmap[0:101,22:23]
v23 = heatmap[0:101,23:24]
v24 = heatmap[0:101,24:25]
v25 = heatmap[0:101,25:26]
v26 = heatmap[0:101,26:27]
v27 = heatmap[0:101,27:28]
v28 = heatmap[0:101,28:29]
v29 = heatmap[0:101,29:30]
v30 = heatmap[0:101,30:31]
v31 = heatmap[0:101,31:32]
v32 = heatmap[0:101,32:33]
v33 = heatmap[0:101,33:34]
v34 = heatmap[0:101,34:35]
v35 = heatmap[0:101,35:36]
v36 = heatmap[0:101,36:37]
v37 = heatmap[0:101,37:38]
v38 = heatmap[0:101,38:39]
v39 = heatmap[0:101,39:40]
v40 = heatmap[0:101,40:41]


###     Plot the histrograms for each vehicle speed    ###

### e.g. TP(%) distribution for vehicle speed of 0 kph ###

plt.plot(v0)
plt.xlabel('TP (%)')
plt.ylabel('Frequency')

###########################################################
###                                                     ###
###   Scaled Cumulative frequency distribution          ###
###                                                     ###
###########################################################

### Regular cumulative freq. distribution = np.cumsum(array) ###

### scale cumulative freq. by number of detections np.cumsum(array)/sum(array) ###

### reverse order of array  array[::-1] if needed ###

### To get the cumlumative freq. as TP(%) increases need to get:
###         1 - np.cumsum(v0)/sum(v0)                              ###


cumsum_v0 = 1 - np.cumsum(v0)/sum(v0)
cumsum_v5 = 1 - np.cumsum(v5)/sum(v5)
cumsum_v10 = 1 - np.cumsum(v10)/sum(v10)
cumsum_v15 = 1 - np.cumsum(v15)/sum(v15)
cumsum_v20 = 1 - np.cumsum(v20)/sum(v20)
cumsum_v25 = 1 - np.cumsum(v25)/sum(v25)
cumsum_v30 = 1 - np.cumsum(v30)/sum(v30)
cumsum_v35 = 1 - np.cumsum(v35)/sum(v35)
cumsum_v40 = 1 - np.cumsum(v40)/sum(v40)


### Plot the cumulative frequency distribution for a given vehicke speed (kph) ###

plt.plot(cumsum_v40)
plt.xlabel('TP (%)')
plt.ylabel('Cumulative Frequency')
plt.title('40 Kph')


###########################################################
###                                                     ###
###           Average TP(%) per vehicle speeds          ###
###                                                     ###
###########################################################

###         Define an array of percentages 0--100 %      ###

TP = np.array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
        26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
        39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
        52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
        65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
        78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
        91,  92,  93,  94,  95,  96,  97,  98,  99, 100])
       
##################################################################

### Calculate the average TP(%) per each vehicle speed: 0--40 kph  ###

mean_TP_v0 = sum(sum((v0.T)*(TP.T)))/sum(v0)
mean_TP_v1 = sum(sum((v1.T)*(TP.T)))/sum(v1)
mean_TP_v2 = sum(sum((v2.T)*(TP.T)))/sum(v2)
mean_TP_v3 = sum(sum((v3.T)*(TP.T)))/sum(v3)
mean_TP_v4 = sum(sum((v4.T)*(TP.T)))/sum(v4)
mean_TP_v5 = sum(sum((v5.T)*(TP.T)))/sum(v5)
mean_TP_v6 = sum(sum((v6.T)*(TP.T)))/sum(v6)
mean_TP_v7 = sum(sum((v7.T)*(TP.T)))/sum(v7)
mean_TP_v8 = sum(sum((v8.T)*(TP.T)))/sum(v8)
mean_TP_v9 = sum(sum((v9.T)*(TP.T)))/sum(v9)
mean_TP_v10 = sum(sum((v10.T)*(TP.T)))/sum(v10)
mean_TP_v11 = sum(sum((v11.T)*(TP.T)))/sum(v11)
mean_TP_v12 = sum(sum((v12.T)*(TP.T)))/sum(v12)
mean_TP_v13 = sum(sum((v13.T)*(TP.T)))/sum(v13)
mean_TP_v14 = sum(sum((v14.T)*(TP.T)))/sum(v14)
mean_TP_v15 = sum(sum((v15.T)*(TP.T)))/sum(v15)
mean_TP_v16 = sum(sum((v16.T)*(TP.T)))/sum(v16)
mean_TP_v17 = sum(sum((v17.T)*(TP.T)))/sum(v17)
mean_TP_v18 = sum(sum((v18.T)*(TP.T)))/sum(v18)
mean_TP_v19 = sum(sum((v19.T)*(TP.T)))/sum(v19)
mean_TP_v20 = sum(sum((v20.T)*(TP.T)))/sum(v20)
mean_TP_v21 = sum(sum((v21.T)*(TP.T)))/sum(v21)
mean_TP_v22 = sum(sum((v22.T)*(TP.T)))/sum(v22)
mean_TP_v23 = sum(sum((v23.T)*(TP.T)))/sum(v23)
mean_TP_v24 = sum(sum((v24.T)*(TP.T)))/sum(v24)
mean_TP_v25 = sum(sum((v25.T)*(TP.T)))/sum(v25)
mean_TP_v26 = sum(sum((v26.T)*(TP.T)))/sum(v26)
mean_TP_v27 = sum(sum((v27.T)*(TP.T)))/sum(v27)
mean_TP_v28 = sum(sum((v28.T)*(TP.T)))/sum(v28)
mean_TP_v29 = sum(sum((v29.T)*(TP.T)))/sum(v29)
mean_TP_v30 = sum(sum((v30.T)*(TP.T)))/sum(v30)
mean_TP_v31 = sum(sum((v31.T)*(TP.T)))/sum(v31)
mean_TP_v32 = sum(sum((v32.T)*(TP.T)))/sum(v32)
mean_TP_v33 = sum(sum((v33.T)*(TP.T)))/sum(v33)
mean_TP_v34 = sum(sum((v34.T)*(TP.T)))/sum(v34)
mean_TP_v35 = sum(sum((v35.T)*(TP.T)))/sum(v35)
mean_TP_v36 = sum(sum((v36.T)*(TP.T)))/sum(v36)
mean_TP_v37 = sum(sum((v37.T)*(TP.T)))/sum(v37)
mean_TP_v38 = sum(sum((v38.T)*(TP.T)))/sum(v38)
mean_TP_v39 = sum(sum((v39.T)*(TP.T)))/sum(v39)
mean_TP_v40 = sum(sum((v40.T)*(TP.T)))/sum(v40)

########################################################

### combine mean TPs in an array for each vehicle speed  ###

mean_TP_V = np.array([mean_TP_v0, mean_TP_v1,mean_TP_v2,mean_TP_v3,
                     mean_TP_v4,mean_TP_v5,mean_TP_v6,mean_TP_v7,
                     mean_TP_v8,mean_TP_v9,mean_TP_v10,mean_TP_v11,
                     mean_TP_v12,mean_TP_v13,mean_TP_v14,mean_TP_v15,
                     mean_TP_v16,mean_TP_v17,mean_TP_v18,mean_TP_v19,
                     mean_TP_v20,mean_TP_v21,mean_TP_v22,mean_TP_v23,
                     mean_TP_v24,mean_TP_v25,mean_TP_v26,mean_TP_v27,
                     mean_TP_v28,mean_TP_v29,mean_TP_v30,mean_TP_v31,
                     mean_TP_v32,mean_TP_v33,mean_TP_v34,mean_TP_v35,
                     mean_TP_v36,mean_TP_v37,0,mean_TP_v39,mean_TP_v40])
                     
##########################################################

### Plot the distribution of mean TP per vehichle speed  ###

plt.plot(mean_TP_V,'bs')	
plt.xlabel('Speed (Kph)')
plt.ylabel('Average TP (%)')
plt.xlim([0,40])
plt.ylim([20,100])

############################################
###                                      ###
###   Add standard deviation error bars  ###
###                                      ###
############################################

     
#f1=open('./v0_list', 'w+')

### v = 0 kph ###
import sys
orig_stdout = sys.stdout
f = file('v0_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 0: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v0_list = []
data2 = open('v0_list.txt','r')
for row in data2:
    v0_list.append(row[0:3])
    
v0_list = np.array(v0_list)
v0_list = v0_list.astype(np.float)
v0_list = v0_list.astype(np.int)
######################################

orig_stdout = sys.stdout
f = file('v5_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 5: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v5_list = []
data2 = open('v5_list.txt','r')
for row in data2:
    v5_list.append(row[0:3])
    
v5_list = np.array(v5_list)
v5_list = v5_list.astype(np.float)
v5_list = v5_list.astype(np.int)

######################################

orig_stdout = sys.stdout
f = file('v10_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 10: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v10_list = []
data2 = open('v10_list.txt','r')
for row in data2:
    v10_list.append(row[0:3])
    
v10_list = np.array(v10_list)
v10_list = v10_list.astype(np.float)
v10_list = v10_list.astype(np.int)
##########################################

orig_stdout = sys.stdout
f = file('v15_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 15: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v15_list = []
data2 = open('v15_list.txt','r')
for row in data2:
    v15_list.append(row[0:3])
    
v15_list = np.array(v15_list)
v15_list = v15_list.astype(np.float)
v15_list = v15_list.astype(np.int)
########################################################

orig_stdout = sys.stdout
f = file('v20_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 20: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v20_list = []
data2 = open('v20_list.txt','r')
for row in data2:
    v20_list.append(row[0:3])
    
v20_list = np.array(v20_list)
v20_list = v20_list.astype(np.float)
v20_list = v20_list.astype(np.int)
########################################################

orig_stdout = sys.stdout
f = file('v25_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 25: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v25_list = []
data2 = open('v25_list.txt','r')
for row in data2:
    v25_list.append(row[0:3])
    
v25_list = np.array(v25_list)
v25_list = v25_list.astype(np.float)
v25_list = v25_list.astype(np.int)
############################################################

orig_stdout = sys.stdout
f = file('v30_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 30: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v30_list = []
data2 = open('v30_list.txt','r')
for row in data2:
    v30_list.append(row[0:3])
    
v30_list = np.array(v30_list)
v30_list = v30_list.astype(np.float)
v30_list = v30_list.astype(np.int)

########################################################

orig_stdout = sys.stdout
f = file('v35_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 35: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v35_list = []
data2 = open('v35_list.txt','r')
for row in data2:
    v35_list.append(row[0:3])
    
v35_list = np.array(v35_list)
v35_list = v35_list.astype(np.float)
v35_list = v35_list.astype(np.int)
##################################################

orig_stdout = sys.stdout
f = file('v40_list.txt', 'w')
sys.stdout = f

for n in range(0,16068):
    if z[n][0] == 40: 
        print(z[n][1])
        
sys.stdout = orig_stdout
f.close()

v40_list = []
data2 = open('v40_list.txt','r')
for row in data2:
    v40_list.append(row[0:3])
    
v40_list = np.array(v40_list)
v40_list = v40_list.astype(np.float)
v40_list = v40_list.astype(np.int)


#####################################################

###     Get the mean of the values      ###

v0_mean= np.mean(v0_list)
v5_mean= np.mean(v5_list)
v10_mean= np.mean(v10_list)
v15_mean= np.mean(v15_list)
v20_mean= np.mean(v20_list)
v25_mean= np.mean(v25_list)
v30_mean= np.mean(v30_list)
v35_mean= np.mean(v35_list)
v40_mean= np.mean(v40_list)

### Get the standard error (error on the mean = sigma/sqrt(N))  ###

v0_err = np.std(v0_list)/np.sqrt(sum(v0))
v5_err = np.std(v5_list)/np.sqrt(sum(v5))
v10_err = np.std(v10_list)/np.sqrt(sum(v10))
v15_err = np.std(v15_list)/np.sqrt(sum(v15))
v20_err = np.std(v20_list)/np.sqrt(sum(v20))
v25_err = np.std(v25_list)/np.sqrt(sum(v25))
v30_err = np.std(v30_list)/np.sqrt(sum(v30))
v35_err = np.std(v35_list)/np.sqrt(sum(v35))
v40_err = np.std(v40_list)/np.sqrt(sum(v40))

mean_V = np.array([v0_mean,v5_mean,v10_mean,v15_mean,v20_mean,v25_mean,
                   v30_mean,v35_mean,v40_mean])
                   

yerr_V = np.array([v0_err,v5_err,v10_err,v15_err,v20_err,v25_err,
                   v30_err,v35_err,v40_err])
                   
p = np.arange(0,45,5)

### Plot the distribution of average TP(%) with standard error error bars ###

plt.errorbar(p,mean_V, yerr_V, fmt='o')
plt.xlabel('Speed (Kph)')
plt.ylabel('Average TP (%)')
plt.xlim([-2,42])
plt.ylim([20,100])

##########################################################

###########################################################
###                                                     ###
###         Number of measurements per vehicle speeds   ###
###                                                     ###                                                                                                               
###########################################################


measurements = np.array([sum(v0),sum(v1),sum(v2),sum(v3),sum(v4),sum(v5),
                         sum(v6),sum(v7),sum(v8),sum(v9),sum(v10),sum(v11),
                        sum(v12),sum(v13),sum(v14),sum(v15),sum(v16),sum(v17),
                        sum(v18),sum(v19),sum(v20),sum(v21),sum(v22),sum(v23),
                        sum(v24),sum(v25),sum(v26),sum(v27),sum(v28),sum(v29),
                        sum(v30),sum(v31),sum(v32),sum(v33),sum(v34),sum(v35),
                        sum(v36),sum(v37),sum(v38),sum(v39),sum(v40)])
                        
### Plot the distribution of mean TP per vehichle speed  ###

plt.plot(measurements,'bs')	
plt.xlabel('Speed (Kph)')
plt.ylabel('Number of Detections (>50% CL)')
plt.xlim([-0.5,40.5])
plt.ylim([0,2500])

################################################################
value = 5
s = str(value)
