# visualisation
Visualisation tool for c+ project

# How to use
Create a csv file with the position data of each pedestrian at each timestep of the form:
```
<ped0 position x at t=0>, <ped0 position y at t=0>
<ped1 position x at t=0>, <ped1 position y at t=0>
...
<pedn position x at t=0>, <pedn position y at t=0>
<ped0 position x at t=t1>, <ped0 position y at t=t1>
...
<pedn position x at t=t_end>, <pedn position y at t=t_end>
```

Then run:
```
python visualise.py <path_to_csv_file> <num_of_passengers>
```
and it will save a file called "visualise.mp4" which you can play.

The tool requries `ffmpeg` so if not installed run `conda install ffmpeg`.

You can play with the `frames` parameter in the code which changes how many frames will be shown. The `interval` parameter changes how long each frame will last.