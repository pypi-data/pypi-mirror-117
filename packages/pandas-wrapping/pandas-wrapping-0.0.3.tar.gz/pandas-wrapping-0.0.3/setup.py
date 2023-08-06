from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="pandas-wrapping",
    version="0.0.3",
    description="""A Python package for working with rest APIs
                and Pandas dataframes""",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/renzobecerra/pandas-wrapping",
    author="Renzo Becerra",
    author_email="rbecerra@nameless.ai",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pandas_wrapping"],
    include_package_data=True,
    install_requires=["requests", "pandas"],
    entry_points={
        "console_scripts": [
            "pandas_wrapping=pandas_wrapping.cli:main",
        ]
    },
)