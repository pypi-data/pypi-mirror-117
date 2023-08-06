import setuptools

setuptools.setup(
    name="lattice-stocks-data",
    version="1.0.2",

    description="An API for gathering RapidAPI stock info",
    long_description="An user friendly library to fetch data related to stock market in no time.",
    long_description_content_type="text/markdown",
    url="https://lattice.dev/products/stock-market-data",
    project_urls={
        "Source": "https://github.com/LatticeData/lattice-stocks-data",
        "Documentation" : "https://github.com/LatticeData/lattice-stocks-data/blob/master/README.md#Usage",
        "Bug Reports" : "https://github.com/LatticeData/lattice-stocks-data/issues",


    },
    py_modules = ["algorithms","buzz","economy","exchanges","financials","indices","market","screeners","search","similarity",
                    "stock","valuation","yahoo_finance"],
    
    author="ashkon@lattice.dev",
    package_dir={
        "": "./stocksdata",
    },
    
    tests_require=['pytest'],

    python_requires=">=3.7",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
