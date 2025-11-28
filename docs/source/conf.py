# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CON2PHYS'
copyright = '2025, Mattia Chini, Irina Pochinok'
author = 'Mattia Chini, Irina Pochinok'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}
templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = [
    "attrs_block",
    "attrs_inline",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_theme = "sphinx_rtd_theme"

html_logo = 'license-plate-logo.png'

html_sidebars = {'**': ['globaltoc.html', 'searchbox.html']}

html_theme_options = {
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'logo_only': True,
}

html_css_files = ['custom.css',]
