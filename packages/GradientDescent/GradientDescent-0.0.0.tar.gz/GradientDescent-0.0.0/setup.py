from setuptools import setup, find_packages

with open('README.md','r') as f:
    long_description = f.read()
VERSION = '0.0.0'
DESCRIPTION = 'Makes learning gradient descent easy'
LONG_DESCRIPTION = 'Makes learning gradient descent easy and makes converting statistical concepts to code easier with transparent usage and flexible control'

# Setting up
setup(
    name="GradientDescent",
    version=VERSION,
    author="Aayushmaan Jain",
    author_email="<aayushmaan1306@gmail.com.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy','pandas'],
    keywords=['python', 'machine', 'learning', 'Machine Learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)