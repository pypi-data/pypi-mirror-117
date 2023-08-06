import os, sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def main():
    setup(
        name='CyberFloodPythonClient',
        version= '1.2.0',
        author='Matthew Jefferson',
        author_email='matthew.jefferson@spirent.com',
        url='https://github.com/matthewjefferson/CyberFloodPythonClient',
        description='CyberFloodPythonClient: Front end for CyberFlood ReST API',
        long_description = 'See https://github.com/matthewjefferson/CyberFloodPythonClient',
        license='http://www.opensource.org/licenses/mit-license.php',
        keywords='Cyber Flood API',
        classifiers=['License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Software Development :: Libraries',
                     'Topic :: Utilities',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3'],
        packages=['CyberFloodPythonClient'],
        install_requires=['requests>=2.7'],
        zip_safe=True,
        )


if __name__ == '__main__':
    main()
