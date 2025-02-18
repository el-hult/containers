import pyvista as pv

# Create a simple sphere
sphere = pv.Sphere()

# Create a plotter and add the mesh
plotter = pv.Plotter()
plotter.add_mesh(sphere, color="lightblue", show_edges=True)
plotter.screenshot('/work/sphere_render.png')
print(plotter.render_window)
if plotter.render_window is not None:
    print(plotter.render_window.ReportCapabilities())
