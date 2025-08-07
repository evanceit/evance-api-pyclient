from setuptools import setup, find_packages

setup(
    name="evance_api_pyclient",
    version="0.2",
    description="Python client for the Evance API",
    author="Kaito Jacobson",
    author_email="info@azexis.com",
    url="https://github.com/evanceit/evance-api-pyclient",
    packages=find_packages(),
    install_requires= [
        "setuptools==75.6.0",
        "twine==6.0.1",
        "requests~=2.32.3",
        "jwt==1.3.1",
        "urllib3~=2.2.3",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
