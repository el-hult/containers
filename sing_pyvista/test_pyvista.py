print(f"Running test file {__file__}")
import pyvista as pv
pv.start_xvfb()
pl=pv.Plotter(off_screen=True)
pl.add_mesh(pv.Sphere())
try:
    pl.show(screenshot='sphere.png')
    print('Wrote to ./sphere.png')
except OSError:
    print('It seems current folder is not writable, writing to /tmp/sphere.png instead')
    pl.show(screenshot='/tmp/sphere.png')