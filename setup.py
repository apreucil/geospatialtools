# filepath: /ncrc/home2/Anthony.Preucil/apscratch/HydroBlocks/geospatialtools/setup.py
from setuptools import setup, find_packages
from numpy.distutils.core import Extension, setup

extensions = [
    Extension(
        name="geospatialtools.terrain_tools_fortran",
        sources=["src/planchon_2001.f90", "src/terrain_tools.f90"],
        extra_f90_compile_args=["-fPIC", "-Wall", "-pedantic", "-O3"],
    ),
    Extension(
        name="geospatialtools.upscaling_tools_fortran",
        sources=["src/upscaling_tools.f90"],
        extra_f90_compile_args=["-fPIC", "-Wall", "-pedantic", "-O3"],
    ),
]

setup(
    name="geospatialtools",
    version="0.1.0",
    description="Geospatial tools for terrain and upscaling operations",
    packages=find_packages(),
    ext_modules=extensions,
)