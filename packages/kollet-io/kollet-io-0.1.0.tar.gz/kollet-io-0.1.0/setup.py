import setuptools

with open("README.md", "r", encoding="utf-8") as file_handler:
    long_description = file_handler.read()


setuptools.setup(
    name="kollet-io",
    packages=setuptools.find_packages(exclude="tests"),
    version="0.1.0",
    license='MIT',
    author="Kollet.io",
    author_email="support@kollet.io",
    description="Python API wrapper for the Kollet Merchant API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kollet-io/kollet-python-api-wrapper.git",
    keywords="Kollet, Kollet API, Merchant API Wrapper, Kollet API Wrapper, Kollet Merchant API",
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)