from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    l_d = f.read()

# Get the version.
version = {}
with open("nlmod/version.py") as fp:
    exec(fp.read(), version)

setup(
    name='nlmod',
    version=version['__version__'],
    description='nlmod module by Artesia',
    long_description=l_d,
    long_description_content_type="text/markdown",
    url='https://github.com/ArtesiaWater/nlmod',
    author='Artesia',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    platforms='Windows, Mac OS-X',
    install_requires=['flopy>=3.3.2',
                      'xarray>=0.16.1',
                      ],
    packages=find_packages(exclude=[]),
    package_data={"nlmod": ["data/*"]},
    include_package_data=True
)
