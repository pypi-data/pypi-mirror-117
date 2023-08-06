from setuptools import find_packages
from setuptools import setup


setup(
    name='gocept.month',
    version='3.0',
    author='gocept gmbh & co. kg',
    author_email='mail@gocept.com',
    url='https://github.com/gocept/gocept.month',
    project_urls={
        'Issue Tracker':
            'https://github.com/gocept/gocept.month/issues',
        'Sources': 'https://github.com/gocept/gocept.month',
        'Changelog':
            'https://raw.githubusercontent.com/gocept/gocept.month/'
            'main/CHANGES.rst',
    },
    description="A datatype which stores a year and a month.",
    long_description=(
        open('README.rst').read() +
        '\n\n' +
        open('CHANGES.rst').read()),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    classifiers="""\
License :: OSI Approved
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Development Status :: 5 - Production/Stable
Framework :: Zope :: 3
Framework :: Zope :: 4
Framework :: Zope :: 5
Framework :: Pyramid
Framework :: Plone
Intended Audience :: Developers
Natural Language :: English
Operating System :: OS Independent
Topic :: Software Development
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
""".splitlines(),
    namespace_packages=['gocept'],
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface >= 4.0',
        'zope.schema',
    ],
    extras_require=dict(
        form=[
            'z3c.form >= 3.0',
            'zope.formlib >= 4.0',
        ],
        test=[
            'plone.testing >= 5.1',
        ]),
)
