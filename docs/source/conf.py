# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Wedding 2026'
copyright = '2026'
author = 'Puti & Birol'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
]

templates_path = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Language configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

# Respect RTD language if present so translated projects don't render as English
import os
# RTD provides READTHEDOCS_LANGUAGE like 'en', 'zh-cn', 'tr'.
# Normalize so our root_doc mapping works, and let Sphinx accept common aliases.
_rtd_lang = os.environ.get('READTHEDOCS_LANGUAGE')
if _rtd_lang:
    lang_norm = _rtd_lang.strip().lower().replace('_', '-')
    # Map common aliases to Sphinx-preferred codes
    if lang_norm in ('zh', 'zh-cn', 'zh-hans'):
        language = 'zh_CN'
    elif lang_norm in ('tr', 'tr-tr'):
        language = 'tr'
    else:
        language = _rtd_lang
else:
    language = 'en'
locale_dirs = ['../locale/']
gettext_compact = False

# Supported languages: English, Turkish, Chinese
# To add translations later, create locale/tr/LC_MESSAGES/ and locale/zh_CN/LC_MESSAGES/ directories

# Root document depends on language so each translation can have its own landing page
root_doc = 'index'
if language.lower().replace('_', '-') in ('zh-cn', 'zh-hans', 'zh'):
    root_doc = 'index_zh'
elif language.lower().startswith('tr'):
    root_doc = 'index_tr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/images/putiBirol.png'

# HTML theme options
html_theme_options = {
    'logo_only': False,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

