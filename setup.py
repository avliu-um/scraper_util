from setuptools import find_packages, setup

setup(
    name='scraper_util',
    packages=find_packages(),
    version='0.1.0',
    description='My first Python library',
    author='Me',
    license='MIT',
    url='https://github.com/avliu-um/scraper_util',
    install_requires=['beautifulsoup4', 'urllib3'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
