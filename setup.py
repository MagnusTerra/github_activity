from setuptools import setup, find_packages

setup(
    name="github_activity",
    version="0.1.0",
    author="magnus_terra",
    author_email="escalantejose22@gmail.com",
    description="A small example package",
    url="https://github.com/magnus_terra/github_activity",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "github_activity=github_activity.main:main",
        ],
    },
)


