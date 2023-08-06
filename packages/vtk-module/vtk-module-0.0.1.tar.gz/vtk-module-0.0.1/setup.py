from setuptools import _install_setup_requires, setup
with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='vtk-module',
    version='0.0.1',
    description='fixes the vtk problems',
    py_modules=['vtk_util'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['discretisedfield~=0.11.1']
)
