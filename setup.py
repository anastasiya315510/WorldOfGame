from setuptools import setup, find_packages

setup(
    name="worldofgames",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "worldofgames=main:main",  # allows running `worldofgames` from terminal
        ]
    },
    python_requires='>=3.6',
    install_requires=[],
    author="Your Name",
    description="World of Games - A mini game collection in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/worldofgames",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
