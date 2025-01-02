from setuptools import setup
with open("README.md","r", encoding = "utf-8")as fh:
    long_description = fh.read()

REPO_NAME = "Movies-Recommendationr-System"
AUTHOR_NAME = "DEVANSHU KUMAR"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']

setup(

    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    description = 'A Simple package for Movie Recommendation System',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}"
    author_email = 'kumardevanshu553@gmail.com',
    packages = [SRC_REPO],
    python_requires = ">=3.12",
    install_requires = LIST_OF_REQUIREMENTS
)
