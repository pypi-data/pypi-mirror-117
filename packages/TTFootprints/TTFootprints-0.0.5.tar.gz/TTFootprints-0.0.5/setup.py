import setuptools

with open("readme.md", 'r', encoding="UTF-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TTFootprints",
    version="0.0.5",
    author="Willem Hunt",
    author_email="Willem.Hunt@uvm.edu",
    description="A library for working with exported data from BMC Footprints 11.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.uvm.edu/whunt1/libfp",
    package_dir={"":"src"},
    packages=["footprints"],
    python_requires=">=3.6"
)

