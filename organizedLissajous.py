import numpy as np
import matplotlib.pyplot as plt
import random
import math
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import cmasher as cmr
from datetime import datetime
from shutil import copyfile
import json

# cmap taken from https://matplotlib.org/stable/tutorials/colors/colormaps.html or https://github.com/1313e/CMasher
# n is number of points
# A & B are horizontal and vertical scaling
# a and b are what really affect the shape; see wikipedia article for more details
# d is how out of phase the sine waves are
# maxd is maximum distance of points to draw line between
# scaling affects color distribution; very high values give more weight to earlier parts of colormap, 1 is linear
# aRand, bRand are random changes to a and b; xRand, yRand are random changes to position

dt = datetime.now()
timestamp = dt.strftime("%Y%m%d%H%M%S")
copyfile('./setup.json',f'./config/{timestamp}.json')

def liss():
    file = open('setup.json')
    parameters = json.load(file)

    a = parameters.get("horizontalFactor")
    b = parameters.get("verticalFactor")
    n = parameters.get("number")
    colormap = parameters.get("colormap")
    periods = parameters.get("periods")
    A = parameters.get("horizontalSize")
    B = parameters.get("verticalSize")
    d = parameters.get("delay")
    maxd = parameters.get("connectionDistance")
    scaling = parameters.get("colorScaling")
    aRand = parameters.get("horizontalRandom")
    bRand = parameters.get("verticalRandom")
    xRand = parameters.get("horizontalError")
    yRand = parameters.get("verticalError")
    
    x = np.array([])
    y = np.array([])
    fig = plt.figure(figsize=(7,5))
    map = mpl.colormaps[colormap].resampled(20)
    # Deals with log scaling of colors in colormap
    space = np.logspace(math.log(1,10), math.log(1 + scaling,10), num=20) - 1
    space = space / scaling
    # Generate points
    for i in np.linspace(0, periods * np.pi, num=n):
        rand = random.gauss(0,1) * xRand
        a += random.gauss(0,1) * aRand
        x = np.append(x, (rand + (np.sin(a * i + d) * A)))
        rand = random.gauss(0,1) * yRand
        b += random.gauss(0,1) * bRand
        y = np.append(y, (rand + (np.sin(b * i) * B)))
    # Progress roughly every ten percent
    progress = np.linspace(n/10,n, num=10)
    print(progress)
    
    np.savetxt(f'./points/{timestamp}', np.vstack((x,y)))
    
    for i in range(x.size - 1):
        # Plot line between points
        plt.plot([x[i],x[i+1]],[y[i],y[i+1]],c='xkcd:grey', lw=0.3)
        for j in range(y.size - 1):
            dist = math.sqrt(abs((np.power(y[j]-y[i],2) + np.power(x[j]-x[i],2))))
            if (dist <= maxd):
                # Value closest to dist/maxd ends up nearest to zero (min of absolute())
                colors = np.absolute(space + (-1 * (dist / maxd)))
                index = (np.ravel(np.asarray(np.where(colors == np.amin(colors)))))[0]
                # Plot lines connecting points w/ decreasing width by distance
                plt.plot([x[i],x[j]],[y[i],y[j]],c=map(space[index]),lw=0.03 - (((0.03 / maxd) - 0.003) * dist))
        if (i in progress):
            print(i)
    
    plt.axis('off')
    plt.axis('scaled')
    plt.savefig(fname=f'./static/{timestamp}', dpi=400, format='png')
    plt.close()

liss()
