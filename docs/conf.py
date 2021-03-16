# -- Project information -----------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../meshpresso'))

project = "CoFEA Initiative"
copyright = "2020"
author = "BlogTechniczny.pl"

master_doc = "index"

# -- General configcduration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [

    'jupyter_sphinx',
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
    "sphinx_thebe",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'deflist',
    "ablog",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.8", None),
    "sphinx": ("https://www.sphinx-doc.org/en/3.x", None),
}
nitpick_ignore = [
    ("py:class", "docutils.nodes.document"),
    ("py:class", "docutils.parsers.rst.directives.body.Sidebar"),
]

numfig = True

myst_admonition_enable = True
myst_deflist_enable = True
myst_url_schemes = ("http", "https", "mailto")
panels_add_bootstrap_css = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/cofea-black.png"
html_title = "CoFEA Initiative"
html_copy_source = True
html_sourcelink_suffix = ""
html_favicon = "_static/cofea-black.png"

html_sidebars = {
    "reference/blog/*": [
        "sidebar-search-bs.html",
        "postcard.html",
        "recentposts.html",
        "tagcloud.html",
        "categories.html",
        "archives.html",
        "sbt-sidebar-nav.html",
        "sbt-sidebar-footer.html",
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]
jupyter_execute_notebooks = "cache"
# thebe_config = {
#     "repository_url": "https://github.com/binder-examples/jupyter-stacks-datascience",
#     "repository_branch": "master",
# }

html_theme_options = {
    "theme_dev_mode": True,
    "path_to_docs": "docs",
    "repository_url": "https://github.com/spolanski/CoFEA",
    # "repository_branch": "gh-pages",  # For testing
    # "launch_buttons": {
    #     "binderhub_url": "https://mybinder.org",
    #     # "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
    #     "colab_url": "https://colab.research.google.com/",
    #     "notebook_interface": "jupyterlab",
    #     "thebe": True,
    # },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    # For testing
    # "home_page_in_toc": True,
    # "single_page": True,
    # "extra_footer": "<a href='https://google.com'>Test</a>",  # DEPRECATED KEY
    # "extra_navbar": "<a href='https://google.com'>Test</a>",
}
html_baseurl = "https://cofea.readthedocs.io/"

# # -- ABlog config -------------------------------------------------
blog_path = "reference/blog"
blog_post_pattern = "reference/blog/*.md"
blog_baseurl = "https://cofea.readthedocs.io"
fontawesome_included = True
post_auto_image = 1
post_auto_excerpt = 2
execution_show_tb = "READTHEDOCS" in os.environ
# ------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
# ------------ Bibtex settings -----------------------------------------
bibtex_bibfiles = ['references.bib']
bibtex_encoding = 'latin'
bibtex_default_style = 'unsrt'
