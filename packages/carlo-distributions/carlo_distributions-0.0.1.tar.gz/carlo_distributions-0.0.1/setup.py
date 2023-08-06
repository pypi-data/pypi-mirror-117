import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="carlo_distributions",
    version="0.0.1",
    author="John Carlo Roberto",
    author_email="john.devera.roberto@gmail.com",
    description="Basic Gaussian and Binomial distributions classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['carlo_distributions'],
    zip_safe=False
)