# connected-parametric-curves
Simple python program to generate figures based off of connecting points of parametric curves.

This is a set of small programs I wrote primarily last November after seeing an example of connected Lissajous curves at <https://www.bit-101.com/blog/2022/11/coding-curves-04-lissajous-curves/> (The author later did a post on roulette curves and other examples, but I wrote this program after reading the post on Lissajous curves)

The basic idea is as follows: 
- Take a number of points, a parametric function, and the parameters
- Evenly distributed over a certain interval, generate that number of points on the function. After every point, change the parameters by a random value times a randomness parameter. Adjust each point’s coordinates by a random value times a random error parameter.
- Iterate over all pairs of points with a nested array. If the Euclidean distance is small enough, draw a line connecting them. The color of the line is sampled from a set of logarithmically spaced points on a colormap, so that very close points end up bright colors.

My first project (organizedLissajous) did the same random changes to parameters, but also included random variation off of the target position (so the points could jitter with the overall shape the same) and also varied connecting line width and color based on distance, using the matplotlib library's given colormaps.

![My first project](https://github.com/benricket/parametric-curve-gallery/blob/348df617bf645fb9ebf897a43d684eef57b41314/Screen%20Shot%202022-11-27%20at%2011.00.13%20PM.png)
![My first project](https://github.com/benricket/parametric-curve-gallery/blob/348df617bf645fb9ebf897a43d684eef57b41314/Screen%20Shot%202022-11-27%20at%2011.30.17%20PM.png)

I followed this by trying to expand it into three dimensions, generating a figure with points x, y, and z, and then animating a view circling around this figure. The good news was that I learned how to make an animation with the matplotlib library, which was cool. The bad news was that it didn't look as good as I thought it would, and it didn't play nice with compression.
![More detailed attempts resulted in more artifacts than Indiana Jones would be able to handle](https://github.com/benricket/parametric-curve-gallery/blob/ccef97400c5716807f698a04f2740ffab3293a33/lissAnimation%20(1).gif)

However, a better use of animation was to show the figure as it was being drawn, rather than at the end. While still not as good as a static image, it was a bit fun to watch,
![I like watching this one](https://github.com/benricket/parametric-curve-gallery/blob/d9a6d4eac50ec1081510e6cfe6cc3f9b401f2834/lissajous%20gif.gif)

My most recent addition was to simply change the function that generates these curves, from a Lissajous curve to a roulette curve (path traced by a circle rolling on another circle, as with a spirograph.)

![Pretty flower](https://github.com/benricket/parametric-curve-gallery/blob/348df617bf645fb9ebf897a43d684eef57b41314/20231015%2017%5C%3A29%5C%3A01n%3D1000%20R%3D4.5%3B%200.0001%20r%3D-0.75%3B%200.0001%20offset%3D3.5%3B%200.001%20maxd%3D0.4%20err%3D0.0005.png)
![Another pretty flower](https://github.com/benricket/parametric-curve-gallery/blob/40129b1ce813cc1dd86a7635f172f7f79411e8e5/20231015%2016%5C%3A34%5C%3A35n%3D1000%20R%3D7%3B%200.0005%20r%3D2%3B%200.0005%20offset%3D4%3B%200%20maxd%3D0.3%20err%3D0.png)

I then changed the function even further, adding two new parameters to give me more room to play around with the generated image. Because certain combinations of parameters just make junk, the function can be played around with [here](https://www.desmos.com/3d/9be50dbfa1) to get some good ideas for starting parameters. 

![Happy little hearts](https://github.com/benricket/parametric-curve-gallery/blob/40129b1ce813cc1dd86a7635f172f7f79411e8e5/20231017%2007%5C%3A16%5C%3A37f%20n%3D1500%20R%3D7%3B%205e-05%20r%3D2.5%3B%205e-05%20offset%3D1.3%3B2.1%20g%3D0.3%20c%3D0.0005%20maxd%3D0.2%20err%3D1e-05.png)
![whatever this thing is called, I like it](https://github.com/benricket/parametric-curve-gallery/blob/40129b1ce813cc1dd86a7635f172f7f79411e8e5/20231016%2021%5C%3A14%5C%3A13f%20n%3D1500%20R%3D7%3B%202e-05%20r%3D5%3B%202e-05%20offset%3D0.24%3B2.75%20g%3D0.4%20c%3D0.0001%20maxd%3D0.2%20err%3D1e-05.png)
![Interesting wreath thing](https://github.com/benricket/parametric-curve-gallery/blob/40129b1ce813cc1dd86a7635f172f7f79411e8e5/20231021%2018%5C%3A43%5C%3A49f%20n%3D3000%20R%3D7.002397893500363%3B%205e-05%20r%3D1.9955618225203422%3B%205e-05%20offset%3D5.0%3B0.1%20u%3D2.3%20v%3D0%20maxd%3D0.2%20err%3D0.0002.png)

I've found it fun just to see what effect these parameters can have. I'm sure there are other designs this function can create that I've yet to stumble upon, but as of right now, I'm decently pleased with them.
