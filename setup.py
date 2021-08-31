from setuptools import setup, find_packages
classifiers = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
]

setup(
    name='saleforce-bulkv2',
    version='0.0.1',
    description='Salesforce Bulk API 2.0 python library',
    Long_description='simple python library to use salesforce Bulk API v2.0',
    url='',
    author='Benhar Mariasoosai',
    author_email='mailbenhar@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    package=find_packages(),
    install_requries=['requests']
)
