# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
#import sphinx_rtd_theme

#import git # from the package gitpython
#repo = git.Repo(search_parent_directories=True)
#sha = repo.head.object.hexsha

# -- Project information -----------------------------------------------------

project = 'CR3BP'
copyright = '2021-2022, The Multibody Astrodynamics Community'
author = 'Matt Werner'
#version = 'Last commit: ' + sha[0:6]
#release = version


# -- General configuration ---------------------------------------------------

# IGNORE DUPLICATE LABEL ENTRIES
suppress_warnings = ['epub.duplicated_toc_entry']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['myst_parser', 'sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

add_function_parentheses = True

numfig = True
today_fmt = '%b %d, %Y'

numfig_secnum_depth = 2


# Math options
math_eqref_format = '({number})'
math_numfig = True # Default is true


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinxdoc' # Nice text size
#html_theme = 'cloud' # Nice scrollbar
#html_theme = 'sizzle'
#html_theme = 'pydata_sphinx_theme'

# Add RTD code from...
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    'analytics_id': 'G-DLCCJ41JJ8',
    'analytics_anonymize_ip': True,
    #'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


# Add logo (when I have one)
html_logo = None
html_favicon = None

# Last updated in footer
html_last_updated_fmt = today_fmt

# Permalinks
html_permalinks = False
#html_permalinks_icon = 'Some sample text'
html_show_sphinx = True
html_secnumber_suffix = " "

# LaTeX
latex_engine = 'pdflatex'
latex_show_pagerefs = True
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def setup(app):
	# Right-align equation numbers in RTD (otherwise they're overhead...)
	app.add_css_file('rtd_eq.css')
    # Google analytics
	app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-DLCCJ41JJ8")
	app.add_js_file("google_analytics_tracker.js")
    
    

