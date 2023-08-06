import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='omdenalore',
    version='0.1',
    author="Omdena Collaborators",
    author_email="kaushal@omdena.com",
    description="AI for Good library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://omdena.com/omdenalore/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
    license="MIT License",
    keywords=['NLP', 'Computer Vision', 'datasets', 'data analysis', 'visualization', 'timeseries', 'python', 'notebooks']
)
