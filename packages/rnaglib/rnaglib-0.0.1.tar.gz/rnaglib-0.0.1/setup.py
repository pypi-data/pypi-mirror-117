import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["torch",
                "dgl",
                'networkx',
                "numpy",
                "seaborn",
                "sklearn",
                "tqdm",
                ]

setuptools.setup(
    name="rnaglib",
    version="0.0.1",
    author="Vincent Mallet, Carlos Oliver, Jonathan Broadbent, William L. Hamilton and Jérome Waldispuhl",
    author_email="vincent.mallet96@gmail.com",
    description="RNAglib: Tools for learning on the structure of RNA using 2.5D graph representations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jwgitlab.cs.mcgill.ca/cgoliver/rnaglib",
    packages=setuptools.find_packages(),
    package_data={'rnaglib': ['data_loading/graph_index_NR.json']},
    # include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.5',
    scripts=['rnaglib/bin/rnaglib_first',
             'rnaglib/bin/rnaglib_second']
)

# For the test pypi :
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository testpypi dist/*

# username : __token__
# pwd : pypi-AgENdGVzdC5weXBpLm9yZwIkNTlkMWY0ZDktYmUwMy00NGRkLWJjNGQtM2ZlNzA0N2E4NGIzAAIleyJwZXJtaXNzaW9ucyI6ICJ1c2VyIiwgInZlcnNpb24iOiAxfQAABiA44PvJsGRA556PeBaa8Xrc11mFGFNq1ese0Ugw9HZ-5A

# pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple rnaglib==0.0.10


# For the real pypi :
# python3 setup.py sdist bdist_wheel
# twine upload dist/*

# pwd : pypi-AgEIcHlwaS5vcmcCJDVjNTUwNTVkLTg0YjQtNGE4Ni1hNmUxLTg3Zjc3YTBmNTI5NQACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYghoEmZfLneT1zDI0Aa-_BJTj1KfZKdwxb-Rrzb-vYHn8