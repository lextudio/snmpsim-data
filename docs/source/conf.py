# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import os


project = 'SNMP Simulation Data'
copyright = '2019, Ilya Etingof. © Copyright 2024-2026, LeXtudio Inc.'
author = 'LeXtudio Inc. <support@lextudio.com>'

# The full version, including alpha/beta/rc tags
version = '1.0'
release = "1.0.1"


language = 'en'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.viewcode',
    'sphinx_sitemap',
    'sphinx_copybutton',
    "notfound.extension",
]

notfound_urls_prefix = "/snmpsim-data/"

html_baseurl = 'https://docs.lextudio.com/snmpsim-data/'
sitemap_url_scheme = '{link}'
sitemap_suffix_included = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

pygments_style = 'sphinx'
pygments_dark_style = "monokai"

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "source_repository": "https://github.com/lextudio/snmpsim-data",
    "source_branch": "main",
    "source_directory": "docs/source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/lextudio/snmpsim-data",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_title = "SNMP Simulator Data Documentation"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

def setup(app):
    on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
    if not on_rtd:
        """Insert Google Analytics tracker
        Based on this Stackoverflow suggestion: https://stackoverflow.com/a/41885884
        """
        app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-DFLYZZK12P")
        app.add_js_file("google_analytics_tracker.js")
