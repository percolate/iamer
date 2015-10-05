from setuptools import setup


setup(
    name='iamer',
    version='0.1.4',
    description='AWS IAM dump and load tool',
    url='https://github.com/percolate/iamer',
    author='Laurent Raufaste',
    author_email='analogue@glop.org',
    license='GPLv3',
    keywords='aws iam boto',
    packages=['iamer'],
    install_requires=[
        'boto',
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'iamer=iamer.main:main'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration"
    ]
)
