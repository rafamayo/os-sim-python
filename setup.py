from setuptools import setup, find_packages

setup(
    name="os_sim",
    version="0.1.0",
    description="OS Simulator course modules",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
)
