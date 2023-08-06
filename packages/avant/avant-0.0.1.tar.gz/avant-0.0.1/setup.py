import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="avant",
    version = "0.0.1",
    author="Nicola Farmer",
    author_email="nkf679@gmail.com",
    description="A Python package to create informed prior probability distributions for reflectometry analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nf679/avant",
    project_urls={
        "docs": "https://avant.readthedocs.io/en/latest/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    )
