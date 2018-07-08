import setuptools


with open("README.rst") as f:
    readme = f.read()


with open("LICENSE") as f:
    license = f.read()


setuptools.setup(
    author="Adam Cunnington",
    author_email="adamcunnington.info@gmail.com",
    description="",
    entry_points={"console_scripts": []},
    install_requires=[],
    license=license,
    long_description=readme,
    name="",
    packages=setuptools.find_packages(exclude=("tests")),
    test_requires=["pytest"],
    url="https://github.com/adamcunnington/",
    version=""
)
