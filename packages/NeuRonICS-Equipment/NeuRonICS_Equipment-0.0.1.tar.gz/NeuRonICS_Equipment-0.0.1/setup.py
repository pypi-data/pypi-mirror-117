import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = ["pyvisa"]

setuptools.setup(
    name="NeuRonICS_Equipment",
    version="0.0.1",
    author="Pratik Kumar",
    author_email="kumarpratik031@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pratik-kr/NeuRonICS_Equipments",
    project_urls={
        "Bug Tracker": "https://github.com/pratik-kr/NeuRonICS_Equipments/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "Equipments"},
    packages=setuptools.find_packages(where="Equipments"),
    python_requires=">=3.6",
)