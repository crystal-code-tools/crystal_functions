import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crystal_functions",
    version="2022.1.14",
    author="Bruno Camino",
    author_email="camino.bruno@gmail.com",
    description="Functions to be used with the CRYSTAL code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crystal-code-tools/crystal_functions",
    project_urls={
        "Bug Tracker": "https://github.com/crystal-code-tools/crystal_functions/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "crystal_functions"},
    packages=setuptools.find_packages(where="functions"),
    python_requires=">=3.6",
    install_requires=[
        "pymatgen",
        ]
)