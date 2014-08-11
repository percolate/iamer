from setuptools import setup


setup(
    name='iamer',
    version='0.1.0',
    description='AWS IAM dump and load tool',
    url='https://github.com/percolate/iamer',
    author='Laurent Raufaste',
    author_email='analogue@glop.org',
    license='GPL',
    keywords='aws iam boto',
    install_requires=[
        'boto',
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'iamer=iamer.main:main'
        ]
    }
)
