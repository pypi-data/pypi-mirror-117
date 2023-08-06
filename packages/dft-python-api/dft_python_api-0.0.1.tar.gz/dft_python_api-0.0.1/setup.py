import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dft_python_api",
    version="0.0.1",
    author="Peter Byrne",
    author_email="peter.byrne+dftpythonapi@york.ac.uk",
    description="Python DFT code APIe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/byornski/dft-python-api",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['ase', 'pint']
)
