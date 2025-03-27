import pyvista as pv
import os

# Determine the output directory
output_dir = "/work" if os.path.isdir("/work") else "."
output_path = os.path.join(output_dir, "foo.png")

# Create a simple sphere
sphere = pv.Sphere()

# Create a plotter and add the mesh
plotter = pv.Plotter()
plotter.add_mesh(sphere, color="lightblue", show_edges=True)
plotter.screenshot(output_path)

if plotter.render_window is not None:
    print(plotter.render_window.ReportCapabilities())

print(pv.Report())
