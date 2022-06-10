from setuptools import setup, find_packages

setup(
    name='cartography',
    packages=find_packages(),
    version='0.1.0',
    description='Fork from allenai/cartography ',
    author='itai@staircase.ai',
    url='https://github.com/staircase-ai/cartography.git',
    license='MIT'
)

#install_requires=['pandas','transformers','torch','scikit-learn','boto3','fastt5','cdifflib'],
#tests_require=['pytest','unittest'],
#test_suite='tests',
