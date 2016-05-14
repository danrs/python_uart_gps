from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='python_uart_gps',
    version='0.1',
    description='Library for reading gps sensor over uart',
    long_description=readme(),
    url='https://github.com/danrs/python_uart_gps',
    author='Daniel Smith',
    author_email='danrs@users.noreply.github.com',
    license='MIT',
    packages=['python_uart_gps'],
    install_requires=[],
    zip_safe=False)
