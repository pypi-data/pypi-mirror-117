import pathlib
from setuptools import setup

__version__ = '1.0'

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name='latexpkges3',
    version=__version__,
    description='utility for cleaning unused LaTeX packages',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/TarasKuzyo/LaTeXpkges',
    author='Taras Kuzyo',
    author_email='kuzyo.taras@gmail.com',
    license='MIT',
    keywords='tools cleanup LaTeX',
    python_requires=">=3.5",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    py_modules=['latexpkges3'],
    entry_points={
        'console_scripts': [
            'latexpkges3=latexpkges3:main',
        ],
    }
)
