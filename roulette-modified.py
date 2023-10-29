import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import cmasher as cmr
import json
import os
from datetime import datetime
import sys

# cmap taken from https://matplotlib.org/stable/tutorials/colors/colormaps.html or https://github.com/1313e/CMasher
# Function can be found at https://www.desmos.com/3d/2f4cccd86c
# For a standard roulette curve, set v = 1 and u = something big

def roulette(parameters):
    dt = datetime.now()
    # Assign parameters from setup file
    cmap = parameters.get("colormap")
    n = parameters.get("number")
    periods = parameters.get("periods")
    aspectratio = parameters.get("aspectRatio")
    bigR = parameters.get("bigR")
    littleR = parameters.get("littleR")
    offset = parameters.get("offset")
    u = parameters.get("u")
    v = parameters.get("v")
    bigRRand = parameters.get("bigRRand")
    littleRRand = parameters.get("littleRRand")
    offsetRand = parameters.get("offsetRand")
    uRand = parameters.get("uRand")
    vRand = parameters.get("vRand")
    xErr = parameters.get("horizontalError")
    yErr = parameters.get("verticalError")
    maxd = parameters.get("connectionDistance")
    scaling = parameters.get("colorScaling")
    
    x = np.array([])
    y = np.array([])
    fig = plt.figure(figsize=(aspectratio*5,5))
    map = plt.get_cmap(cmap).resampled(100)
    # Deals with log scaling of colors in colormap
    space = np.logspace(math.log(1,10), math.log(1 + scaling,10), num=20) - 1
    space = space / scaling
    
    # Generate points
    for i in np.linspace(0, periods * 2 * np.pi, num=n):
        # Adjust parameters based on values for random
        scale = 1.0/(v*(bigR - littleR) + offset + (1/u))
        bigR += random.gauss(0,1) * bigRRand
        bigR = abs(bigR)
        littleR += random.gauss(0,1) * littleRRand
        littleR = abs(littleR)
        offset += random.gauss(0,1) * offsetRand
        offset = abs(offset)
        u += random.gauss(0,1) * uRand
        u = abs(u)
        v += random.gauss(0,1) * vRand
        v = abs(v)
        rand = random.gauss(0,1) * xErr
        # New coordinates (this is where the function goes)
        x = np.append(x, scale*(v*(bigR - littleR)*np.cos(i) + (offset - (np.cos(bigR*i))/u)*np.cos(((bigR - littleR)/littleR)*i)))
        rand = random.gauss(0,1) * yErr
        y = np.append(y, scale*(v*(bigR - littleR)*np.sin(i) - (offset - (np.cos(bigR*i))/u)*np.sin(((bigR - littleR)/littleR)*i)))
    # Tell me roughly every ten percent
    progress = np.linspace(n/10,n, num=10)
    
    for i in range(x.size - 1):
        # Plot line between points
        plt.plot([x[i],x[i+1]],[y[i],y[i+1]],c='xkcd:grey', lw=0.3)
        for j in range(y.size - 1):
            dist = math.sqrt(abs((np.power(y[j]-y[i],2) + np.power(x[j]-x[i],2))))
            if (dist <= maxd): # if points close enough to connect
                # Value closest to dist/maxd ends up nearest to zero (min of absolute())
                colors = np.absolute(space + (-1 * (dist / maxd)))
                index = (np.ravel(np.asarray(np.where(colors == np.amin(colors)))))[0]
                # Plot lines connecting points w/ decreasing width by distance
                plt.plot([x[i],x[j]],[y[i],y[j]],c=map(space[index]),lw=0.03 - (((0.03 / maxd) - 0.003) * dist))
        if (i in progress):
            print(i)
    # Save figure
    timestamp = dt.strftime("%Y%m%d %H;%M;%S")
    str=(timestamp+' n={} R={}; {} r={}; {} offset={};{} u={} v={} maxd={} err={}'.format(n, bigR, bigRRand, littleR, littleRRand, offset, u, v, offsetRand, maxd, xErr, yErr))
    plt.axis('off')
    plt.axis('scaled')
    plt.savefig(fname=str+'.png', dpi=400, format='png')
    plt.close()
    
cwd = os.getcwd()
if len(sys.argv) == 1: # no extra command line args
    # Generate an image for each set of parameters in setup directory
    for entry in os.listdir(f'{cwd}/setup/'):
        file = open(f'{cwd}/setup/{entry}')
        params = json.load(file)
        roulette(params)

else:
    # Generate an image for the parameters in files given as args
    for i in range(len(sys.argv-1)):
        name = sys.argv[i+1]
        file = open(f'./config/{name}')
        params = json.load(file)
        roulette(params)
