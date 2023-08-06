from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ['numpy>=1.16.5', 'pandas>=1.0.0', 'ogb>=1.1.0',
                    'torch>=1.7.1', 'dgl>=0.6.1']
setup_requires = []
tests_require = []

classifiers = [
    'Development Status :: 4 - Beta',

    'Programming Language :: Python :: 3.6',

]

setup(
    name = "testopenhgnn",
    version = "1.1",
    author = "",
    author_email = "",
    maintainer = "",
    license = "",

    description = "OpennHGNN: an open-source toolkit for Heterogeneous Graph Neural Network",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    
    url = "https://github.com/BUPT-GAMMA/OpenHGNN",
    download_url = "https://github.com/BUPT-GAMMA/OpenHGNN",

    python_requires='>=3.6',

    packages = find_packages(),
    
    install_requires = install_requires,
    include_package_data = True,

    classifiers = classifiers
)
    
    
