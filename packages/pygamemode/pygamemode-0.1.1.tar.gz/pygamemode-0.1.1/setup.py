from setuptools import setup, Extension
import os.path

setup_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(setup_directory, 'README.md')) as readme_file:
    long_description = readme_file.read()

setup(
    name='pygamemode',
    version='0.1.1',
    description='A Python wrapper for the GameMode client API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aforren1/pygamemode',
    author='Alexander Forrence',
    author_email='alex.forrence@gmail.com',
    license='BSD 3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    ext_modules = [Extension('gamemode', ['pygamemode.c'],
                             extra_compile_args=['-std=c99', '-g0'],
                             py_limited_api=True)]
)
