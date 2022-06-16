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
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_rtd_theme
# import platform
from datetime import datetime
from backports.zoneinfo import ZoneInfo

import sphinx
import sphinx_material

# Time during compiling
now = datetime.now(tz=ZoneInfo("America/New_York"))

# -- Project information -----------------------------------------------------
project = 'CR3BP'
copyright = '2021-2022, Matt Werner and contributors'
author = 'Matt Werner'
version = f"{now.year}-{now.month:02}-{now.day:02} {now.hour:02}H ({now.tzinfo})"
language = 'en'
#version = 
#release = 

# -- General configuration ---------------------------------------------------

# IGNORE DUPLICATE LABEL ENTRIES
suppress_warnings = ['epub.duplicated_toc_entry']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions=[
	"sphinx.ext.autosectionlabel",
	"myst_parser",
	"sphinx_design",
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
	]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

myst_enable_extensions = ["colon_fence", "deflist", "substitution", "html_image"]
myst_substitutions = {
    "loremipsum": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed iaculis arcu vitae odio gravida congue. Donec porttitor ac risus et condimentum. "
    "Phasellus bibendum ac risus a sollicitudin. "
    "Proin pulvinar risus ac mauris aliquet fermentum et varius nisi. "
    "Etiam sit amet metus ac ipsum placerat congue semper non diam. "
    "Nunc luctus tincidunt ipsum id eleifend. Ut sed faucibus ipsum. "
    "Aliquam maximus dictum posuere. Nunc vitae libero nec enim tempus euismod. "
    "Aliquam sed lectus ac nisl sollicitudin ultricies id at neque. "
    "Aliquam fringilla odio vitae lorem ornare, sit amet scelerisque orci fringilla. "
    "Nam sed arcu dignissim, ultrices quam sit amet, commodo ipsum. "
    "Etiam quis nunc at ligula tincidunt eleifend."
}

show_authors = False # Show .. sectionauthor:: and .. codeauthor:: (True or False)

# -- Options for Code output -------------------------------------------------
add_function_parentheses = True # Adds parentheses to functions (example :func:`myfunc`)


# -- Options for Figs, Tables, and code-blocks ("listings") output -----------
numfig = True # Number figures
numfig_secnum_depth = 2


# -- Options for Math output -------------------------------------------------
math_eqref_format = '({number})'
math_numfig = True # Default is true


# -- Options for HTML output -------------------------------------------------
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinxdoc' # Nice text size
#html_theme = 'classic'
#html_theme = 'cloud' # Nice scrollbar
#html_theme = 'sizzle'
#html_theme = 'pydata_sphinx_theme'
html_theme = 'sphinx_book_theme'

if html_theme == "sphinx_book_theme":
    html_theme_options = {
        "repository_url": "https://github.com/3allan/cr3bp",
        "use_repository_button": True,
        "use_edit_page_button": True,
        "use_issues_button": True,
        "repository_branch": "2bp",
        "path_to_docs": "docs",
        "home_page_in_toc": False,
        "logo_only": True,
        "search_bar_text": "Search this book...",
    }
if html_theme == "sphinx_rtd_theme":
	# Add RTD code from https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
	html_theme_options = {
		'analytics_id': 'G-DLCCJ41JJ8',
		'analytics_anonymize_ip': True,
		'logo_only': True,
		'display_version': True,
		'prev_next_buttons_location': 'bottom',
		'style_external_links': False,
		'vcs_pageview_mode': '',
		'style_nav_header_background': 'black',
		# Toc options
		'collapse_navigation': False,
		'sticky_navigation': True,
		'navigation_depth': -1,
		'includehidden': True,
		'titles_only': False,
	}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Options
html_baseurl = 'https://cr3bp.com'
html_logo = "icon-horseshoe.svg"
html_favicon = "favicon-horseshoe.svg" # Should be 16x16 or 32x32 pixel, Windows icon file (.ico)
html_last_updated_fmt = '%b %d, %Y' # Last updated in footer
html_permalinks = True
html_permalinks_icon = '@'
html_show_search_summary = True
html_show_sphinx = True
html_show_copyright = True
html_split_index = False
html_output_encoding = 'utf-8'
html_secnumber_suffix = " " # Removes the trailing period on header numbers
html_math_renderer = 'mathjax'
html_sourcelink_suffix=""

# -- Options for epub output -------------------------------------------------
# Not too sure what this is, so I've skipped it


# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'lualatex'
latex_logo = 'static/logo_wide.svg'
latex_toplevel_sectioning = 'section'
latex_show_pagerefs = True
latex_show_urls = 'footnote'
latex_docclass = {'article': 'howto', 'report': 'manual'}
latex_elements = {
    'papersize': 'letterpaper', # 'letterpaper' or 'a4paper'
	'pointsize': '10pt', # The font size ('10pt', '11pt' or '12pt')
	'preamble': r'\usepackage{unicode-math}', # Additional stuff for the LaTeX preamble.
	'figure_align': 'htbp', # Latex figure (float) alignment
}

# -- Options for text output--------------------------------------------------
text_newlines = 'unix'
text_sectionchars = '*=-~"+`'
text_add_secnumbers = True
text_secnumber_suffix = " "

# -- Setup -------------------------------------------------------------------
def setup(app):
	# Right-align equation numbers in RTD (otherwise they're overhead...)
	app.add_css_file('rtd_eq.css')
    # Google analytics
	app.add_js_file("https://www.googletagmanager.com/gtag/js?id=G-DLCCJ41JJ8")
	app.add_js_file("google_analytics_tracker.js")
    
    

