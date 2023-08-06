# cloud2cloud
This is a simple tool to interpolate N-dimensional data between two M-dimensional meshes as fast as possible.
At any point of the target mesh the data is computed from K nearest neighbours in the source mesh.


## cloud2cloud interface
For structured meshes.
```py
result = cloud2cloud(source, values, target)

source # ndarray(*shape_sce, dim_msh)
target # ndarray(*shape_tgt, dim_msh)
values # ndarray(*shape_sce, *shape_val)
result # ndarray(*shape_tgt, *shape_val)
```


## Raw interface
The underlying method used to interpolate.
```py
base = CloudInterpolator(source, target)
result = base.interp(values)

source # ndarray(dim_msh, points_sce) or tuple(ndarray(points_sce),...)
target # ndarray(dim_msh, points_tgt) or tuple(ndarray(points_tgt),...)
values # ndarray(points_sce, *shape_val)
result # ndarray(points_tgt, *shape_val)
```
