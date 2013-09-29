from setuptools import setup
from stuff import version

setup(name='stuff',
      version=version,
      description="All your belongings",
      long_description="",
      classifiers=[],
      keywords='credit card address phone',
      author='@iopeak',
      author_email='steve@stevepeak.net',
      url='https://github.com/stevepeak/stuff',
      license='Apache v2',
      packages=['stuff'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      entry_points="")
