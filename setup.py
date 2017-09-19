"""sphinx_psi_theme setup script"""

import os
root_dir = os.path.abspath(os.path.join(__file__, ".."))
os.chdir(root_dir)
import sys
import setuptools

opts = dict(
    packages=setuptools.find_packages(root_dir),
    package_data={
        "sphinx_psi_theme": ["themes/sphinx_psi_theme/*.*", "themes/sphinx_psi_theme/static/*.*"]
    },
    zip_safe=False,
    name="sphinx_psi_theme",
    author="Lori A. Burns",
    author_email="psi4aiqc@gmail.com",
    license = "BSD-3-Clause",
    url = "https://github.com/psi4/sphinx-psi-theme",

    install_requires=[
        "sphinx>=1.5"
    ],

    entry_points={
        'sphinx_themes': [
            'path = sphinx_psi_theme:get_theme_dir',
        ],
    },

    description= 
    "a nice sphinx theme for Psi4 derived from 'Cloud' and some related extensions",

    long_description="""\
This is a small package containing a Sphinx theme named "sphinx_psi_theme",
along with some related Sphinx extensions. To see an example
of the theme in action, check out `<http://psicode.org/psi4manual/master/index.html>`_.
    """,

    keywords="sphinx extension theme",

    classifiers="""
Development Status :: 5 - Production/Stable
Framework :: Sphinx :: Extension
Framework :: Sphinx :: Theme
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Topic :: Documentation
Topic :: Software Development :: Documentation
""".strip().splitlines(),

    script_args=sys.argv[1:],
    cmdclass={},
)

# pull version string from package
from sphinx_psi_theme import __version__ as version
opts['version'] = version

setuptools.setup(**opts)

