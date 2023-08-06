import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "uavnoma",
    version = "1.0.0" ,
    author = "Brena Lima",
    author_email = "brenakslima@gmail.com",
    description = "UAV-NOMA System Model",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = "https://github.com/limabrena/uavnoma",
    packages = ['uavnoma'],
    install_requires = ['numpy', 'pandas', 'tabulate', 'matplotlib'],
    python_requires = '>=3.8',
    entry_points = {
        'console_scripts': ['uavnoma=uavnoma.command_line:main'],
    },
    extras_require = {
        'dev' : [
            'pytest',
            'pytest-cov',
            'pytest-console-scripts',
            'coverage',
            'codecov'
        ]
    }
)