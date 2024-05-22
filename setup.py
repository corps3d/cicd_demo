from setuptools import setup, find_packages

setup(
    name='my_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            'my-app=my_app.main:hello_world',
        ],
    },
)
