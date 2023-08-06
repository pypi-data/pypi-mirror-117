import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='content_extractor-pi',
    version='0.0.9',
    license="MIT",
    author='Paolo Italiani',
    author_email='paoita@hotmail.it',
    description='Content extractor for files containing text',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/paoloitaliani/content-extractor-pi',
    packages=['content_extractor'],
    install_requires=[
        "gensim",
        "imbalanced-learn",
        "numpy",
        "pandas",
        "scikit-learn",
        "tqdm"
    ],
)
