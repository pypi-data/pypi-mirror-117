import setuptools

from plots import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyplots",
    version=__version__,
    author="Jakob Stigenberg",
    description="Wraps matplotlib for easier plotting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakkes/plots",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.7",
    install_requires=["matplotlib~=3.4.3"]
)

### Publish
### python3 setup.py sdist bdist_wheel
### twine upload dist/*