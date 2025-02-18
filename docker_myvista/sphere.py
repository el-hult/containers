import pyvista as pv
import sys
fname = sys.argv[1]

# Create a simple sphere
sphere = pv.Sphere()

# Create a plotter and add the mesh
plotter = pv.Plotter()
plotter.add_mesh(sphere, color="lightblue", show_edges=True)
print(f'Saving to {fname}')
plotter.screenshot(fname)
if plotter.render_window is not None:
    print(plotter.render_window.ReportCapabilities())
