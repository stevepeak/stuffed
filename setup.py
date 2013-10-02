from setuptools import setup
from stuffed import version

setup(name='stuffed',
      version=version,
      description="All your belongings",
      long_description="",
      classifiers=["Development Status :: 1 - Planning",
                   "Environment :: Plugins",
                   "License :: OSI Approved :: Apache Software License",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.7",
                   "Topic :: Utilities"],
      keywords='credit card address phone',
      author='@iopeak',
      author_email='steve@stevepeak.net',
      url='https://github.com/stevepeak/stuffed',
      license='Apache v2',
      packages=['stuffed'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[i.strip() for i in open("requirements.txt").readlines()],
      entry_points="")
