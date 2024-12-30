
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
import sys
# sys.path.insert(0, os.path.abspath('.'))
import time

# This approach does not currently work with Docker/Jenkins, so we set only the main doc hub for now

# import git

# # -- Get current branch and set hub's home page accordingly ------------------
# repo = git.Repo(search_parent_directories=True)
# branch = repo.active_branch

# if branch.name == 'pre_release' :
#     hubhome = 'http://zextrasdoc.s3-website-eu-west-1.amazonaws.com/landing/zextras_documentation.html'
# else :
#     hubhome = 'https://docs.zextras.com/landing/zextras_documentation.html'

hubhome = 'https://docs.zextras.com/landing/zextras_documentation.html'

# -- Get current year --------------------------------------------------------
current_year = time.strftime('%Y')

# -- Project information -----------------------------------------------------

project = 'Carbonio CE Admin'
copyright = '2024: ZEXTRAS'
author = 'The Zextras Team'

# The full version, including alpha/beta/rc tags
release = '24.12.0'
version = release

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx_design', 'sphinx_copybutton',
               'sphinx.ext.graphviz', 'sphinxcontrib.email', 'sphinx_multiversion' ]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_includes', 'common/cli', 'common/carbonio' ]

rst_prolog = """

.. |product| replace:: Carbonio CE
.. |storage| replace:: Carbonio Storages CE
""" + open("replace.txt").read()

# -- Configuration of extensions ---------------------------------------------

# copybutton, see https://sphinx-copybutton.readthedocs.io/en/latest/
copybutton_prompt_text = r'\$\s|#\s|carbonio>\s|zextras\$\s'
copybutton_prompt_is_regexp = True
copybutton_line_continuation_character = "\\"
copybutton_only_copy_prompt_lines = True

numfig = True

email_automode = True

graphviz_output_format = 'png'

## sphinx-multiversion

# Whitelist pattern for tags (set to None to ignore all tags)
#smv_tag_whitelist = r'^ZTD-81.*$
smv_tag_whitelist = r'None'

# Whitelist pattern for branches (set to None to ignore all branches)
smv_branch_whitelist = r'devel|ZTD-98.*$|ZTD-99.*$'
#smv_branch_whitelist = r'test'
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r'origin'

# Pattern for released versions
#smv_released_pattern = r'^refs/heads/.*$'
#smv_released_pattern = r'^refs/heads/ZTD-99.*$'

# Format for versioned output directories inside the build directory
#smv_outputdir_format = '{ref.name}'
smv_outputdir_format = '{config.version}/{ref.name}'

# Determines whether remote or local git branches/tags are preferred if their output dirs conflict
smv_prefer_remote_refs = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_show_sourcelink = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = [ 'css/community.css' ]
html_js_files = [ 'js/posthog.js' ]
html_favicon = 'img/favicon.ico'
html_title = project + ' Documentation'
html_last_updated_fmt = ''
templates_path = [ 'common/templates' ]
html_theme_options = {
    'use_download_button': False,
    'repository_url': 'https://github.com/zextras/tech-doc/',
    'repository_branch': 'master',
    'use_repository_button': True,
    'use_issues_button': True,
    'navigation_with_keys': False,
    'extra_footer': '<a href="https://docs.zextras.com/landing/privacy-legal.html" target="_blank">Privacy &amp; Legal</a> ',
    'logo': {
        'image_light': 'carbonio-black.svg',
        'image_dark': 'carbonio-white.svg',
        'text': '%s' %release,
    },

    # Add button for surveys at the bottom of the right-hand side menu
    # (local ToC)
    #'secondary_sidebar_items': ['page-toc', 'survey'],

    # Add button for surveys at the bottom of the right-hand side menu
    # (global ToC)
    #'primary_sidebar_end': ['survey'],
}
html_sidebars = { "**": [ 'navbar-logo.html',
                          'zxbrand',
                          'search-button-field.html',
                          'sbt-sidebar-nav.html', 'index.html', 'home.html' ] }

html_context = {
    'hubhome' : '%s' %hubhome,
}

html_extra_path = []

# -- Options for linkcheck output --------------------------------------------

# list of URLs to ignore
linkcheck_ignore = [ r'.*.example.com(:\d+)?/',
                     r'https:\/\/my-saml-provider\.org\/',
                     r'https:\/\/notifications.zextras.com\/firebase\/',
                     r'https://mycompany.okta.com/.*',
                     r'../../.*' ]

# there are more options, but at the moment we don't need them. They
# can be found at
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

###
# This custom code is required as a workaround for a build error
# caused by extension sphinx-new-tab-link
###

from sphinx.writers.html import HTMLTranslator
class PatchedHTMLTranslator(HTMLTranslator):
    def starttag(self, node, tagname, *args, **attrs):
        if (
            tagname == "a"
            and "target" not in attrs
            and (
                "external" in attrs.get("class", "")
                or "external" in attrs.get("classes", [])
            )
        ):
            attrs["target"] = "_blank"
            attrs["ref"] = "noopener noreferrer"
        return super().starttag(node, tagname, *args, **attrs)


def setup(app):
    app.set_translator("html", PatchedHTMLTranslator)
