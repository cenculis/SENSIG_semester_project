import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.io.wavfile import read

numOfDataSamples =5

################################################## GOOD GLASS ##########################################################

f = read("goodGlass0.wav")
array = np.array(f[1],dtype=float)
cutOff = 500
maxPos = 0
minPos = 0
count = 0

for i in range(np.shape(array)[0]):
    if array[i] == array.max():
        maxPos = i

    if maxPos != 0:
        if count < 10:
            if abs(array[i]) < cutOff:
                count = count + 1
            else:
                count = 0
        if count == 10:
            minPos = i
            break

template = array[maxPos:minPos]
temLen_g = len(template)
clippedArray = np.zeros((numOfDataSamples, temLen_g))
twoTimesNumOfDataSamples = numOfDataSamples*2
s = (temLen_g, twoTimesNumOfDataSamples)
combinedArray = np.empty(s)
#print(combinedArray[:,0])

for j in range(numOfDataSamples):
    fh = read("goodGlass"+str(j)+".wav")
    array2 = np.array(fh[1],dtype=float)

    arrLen = np.shape(array2)[0]
    corr = array2[0:arrLen - temLen_g]
    maxCorPos = 0
    maxCor = 0

    for i in tqdm(range(arrLen - temLen_g)):
        corr[i] = sum(array2[i:i+temLen_g]*template)/temLen_g
        if corr[i] > maxCor:
            maxCor = corr[i]
            maxCorPos = i

    corr = abs(corr)
    fh = read("goodGlass"+str(j)+".wav")
    array3 = np.array(fh[1],dtype=float)
    clippedArray[j] = array3[maxCorPos:maxCorPos+temLen_g]
    combinedArray[:,j] = array3[maxCorPos:maxCorPos+temLen_g]
    fileName = "invGoodGlass"+str(j)+".npy"
    np.save(fileName, clippedArray[j])

'''
for i in range(len(clippedArray)):
    plt.figure(1)
    plt.plot(template, color="magenta")
    plt.figure(2)
    plt.plot(clippedArray[i], color="red")
    fh = read("goodGlass"+str(i)+".wav")
    origArray = np.array(fh[1],dtype=float)
    plt.figure(3)
    plt.plot(origArray, color="blue")
    plt.show()
'''

################################################## BAD GLASS ###########################################################
f = read("badGlass0.wav")
array = np.array(f[1],dtype=float)
cutOff = 500
maxPos = 0
minPos = 0
count = 0

for i in range(np.shape(array)[0]):
    if array[i] == array.max():
        maxPos = i

    if maxPos != 0:
        if count < 10:
            if abs(array[i]) < cutOff:
                count = count + 1
            else:
                count = 0
        if count == 10:
            minPos = i
            break

template = array[maxPos:minPos]
temLen_b = len(template)
clippedArray = np.zeros((numOfDataSamples, temLen_g))

for j in range(numOfDataSamples):
    fh = read("badGlass"+str(j)+".wav")
    array2 = np.array(fh[1],dtype=float)

    arrLen = np.shape(array2)[0]
    corr = array2[0:arrLen - temLen_b]
    maxCorPos = 0
    maxCor = 0

    for i in tqdm(range(arrLen - temLen_b)):
        corr[i] = sum(array2[i:i+temLen_b]*template)/temLen_b
        if corr[i] > maxCor:
            maxCor = corr[i]
            maxCorPos = i

    corr = abs(corr)
    fh = read("badGlass"+str(j)+".wav")
    array3 = np.array(fh[1],dtype=float)
    clippedArray[j] = array3[maxCorPos:maxCorPos+temLen_g]
    combinedArray[:,j+numOfDataSamples] = array3[maxCorPos:maxCorPos+temLen_g]
    fileName = "invBadGlass"+str(j)+".npy"
    np.save(fileName, clippedArray[j])

'''
for i in range(len(clippedArray)):
    plt.figure(1)
    plt.plot(template, color="magenta")
    plt.figure(2)
    plt.plot(clippedArray[i], color="red")
    fh = read("badGlass"+str(i)+".wav")
    origArray = np.array(fh[1],dtype=float)
    plt.figure(3)
    plt.plot(origArray, color="blue")
    plt.show()
'''

np.save("combinedArray.npy", combinedArray)



