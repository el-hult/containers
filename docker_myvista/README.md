A docker image for headless VTK with open GL support

```bash
docker build -t myvista .
docker run -v .:/work myvista /myenv/bin/python /work/sphere.py
```
