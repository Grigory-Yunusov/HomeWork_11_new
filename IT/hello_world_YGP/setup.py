from setuptools import setup, find_namespace_packages

setup(
    name='hello_world_YGP',
    version='0.0.1',
    description='Very nice code',
    author='Yunusov G.P',
    author_email='grigoriyzawr@gmail.com',
    license='MIT',
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['greeting=hello_world_YGP.main:greeting']}
)