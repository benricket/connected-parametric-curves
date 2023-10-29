# connected-parametric-curves
Simple python program to generate figures based off of connecting points of parametric curves.

This is a set of small programs I wrote primarily last November after seeing an example of connected Lissajous curves at <https://www.bit-101.com/blog/2022/11/coding-curves-04-lissajous-curves/> (The author later did a post on roulette curves and other examples, but I wrote this program after reading the post on Lissajous curves)

My first project (organizedLissajous) did the same random changes to parameters, but also included random variation off of the target position (so the points could jitter with the overall shape the same) and also varied connecting line width and color based on distance, using the matplotlib library's given colormaps.
![My first project](https://drive.google.com/file/d/1D_HLBHZaQiYeMldTZ6yDDcar30ZD30P5/view?usp=sharing.png)
![My first project](https://drive.google.com/file/d/1F1AV6U29GYO8UHw0QqYbEcp6eUvrXZgM/view?usp=sharing)

I followed this by trying to expand it into three dimensions, generating a figure with points x, y, and z, and then animating a view circling around this figure. The good news was that I learned how to make an animation with the matplotlib library, which was cool. The bad news was that it didn't look as good as I thought it would, and it didn't play nice with compression.
![More detailed attempts resulted in more artifacts than Indiana Jones would be able to handle](https://drive.google.com/file/d/1ZrRqervu5UIQ19db4jHQuV0Hmf_cF-Wm/view?usp=sharing)

However, a better use of animation was to show the figure as it was being drawn, rather than at the end. While still not as good as a static image, it was a bit fun to watch,
![I like watching this one](https://drive.google.com/file/d/14I2yxkgDD05CLPiiyUUM62mWfSc-9sPX/view?usp=sharing)

My most recent addition was to simply change the function that generates these curves, from a Lissajous curve to a roulette curve (path traced by a circle rolling on another circle, as with a spirograph.)

I then changed the function even further, adding two new parameters to give me more room to play around with the generated image. Because certain combinations of parameters just make junk, the function can be played around with ![here](https://www.desmos.com/3d/9be50dbfa1) to get some good ideas for starting parameters. 
