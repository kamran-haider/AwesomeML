import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="awesome_ml",
    version="0.0.1",
    author="Kamran Haider",
    author_email="kamranhaider.mb@gmail.com",
    description="A Python package to demonstrate packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamran-haider/AwesomeML",
    packages=setuptools.find_packages()
)