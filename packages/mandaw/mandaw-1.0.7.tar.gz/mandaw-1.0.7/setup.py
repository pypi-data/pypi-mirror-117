import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
      name='mandaw',
      version='1.0.7',
      description='A Game Engine Made In Python',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='mandaw2014',
      author_email='mandawbuisness@gmail.com',
      url='https://github.com/mandaw2014/MandawEngine',
      packages=['mandaw'],
      package_dir={'':'mandaw_engine'},
      python_requires=">=3.6",
      install_requires=["pygame"]
)