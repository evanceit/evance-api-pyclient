from setuptools import setup, find_packages

setup(
    name="evance_api_pyclient",
    version="0.1",
    description="Python client for the Evance API",
    author="Kaito Jacobson",
    author_email="info@azexis.com",
    url="https://github.com/evanceit/evance-api-pyclient",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
