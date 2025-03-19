from setuptools import setup

setup(
    name="dxpq",
    version="0.0.1",
    description="A Python wrapper for PostgreSQL interaction using a C extension",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Pedro Barbosa",
    author_email="pedrohsbarbosa99@gmail.com",
    url="https://github.com/pedrohsbarbosa99/dxpq_ext",
    packages=["src"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # TODO: include tests
)
