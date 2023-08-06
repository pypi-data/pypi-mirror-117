import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='metest',
     version='0.0.1',
     author="Kasper Hintz",
     author_email="kah@dmi.dk",
     description="Test, check and compare logs and data from meteorological computations.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     setup_requires=['wheel'],
     url="https://dmidk.github.io/metest/",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )
