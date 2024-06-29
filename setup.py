from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Library to create gitignore files'
LONG_DESCRIPTION = "A package that allows you to get gitignore's for different languages and/or frameworks."

# Setting up
setup(
    name="python-gitignore-generator",
    version=VERSION,
    author="yeffian (Adit Chakraborty)",
    author_email="<mail@adit.chakraborty2009@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['selenium'],
    keywords=['python', 'github', 'git', 'tools'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)