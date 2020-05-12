from setuptools import setup, find_packages

setup(
    name="nlp_datasets",
    version="0.0.1",
    packages=find_packages(),  # exclude=('tests.*', 'tests')
    install_requires=["pandas", "requests", "tqdm"],
    package_data={"nlp_datasets": ["urls/urls.json"]},
    url="",
    license="",
    author="Vatolin Alexey",
    author_email="vatolinalex@gmail.com",
    description="NLP russian datasets",
)
