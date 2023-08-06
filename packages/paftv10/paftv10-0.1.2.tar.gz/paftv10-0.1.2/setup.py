from setuptools import setup, find_packages

setup(
    name="paftv10",
    version='0.1.2',
    packages= find_packages(),
    install_requires=[
          'biopython',
      ],
    entry_points={
        'console_scripts': [
            'paftv10 = paftv.paftv:main',
        ],
    },
    license='MIT',
    description='Visualization for PAF files using AliTV',
    author='Sebastian Vorbrugg',
    author_email='sebastian.vorbrugg@tuebingen.mpg.de',
    url='https://github.com/MoinSebi/paftv'

)
