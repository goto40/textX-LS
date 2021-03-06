import functools

from textx_ls_core.languages import LANG_EXTENSIONS, LANGUAGES
from textx_ls_core.utils import get_file_extension


def call_with_lang_template(func, languages=LANGUAGES):
    """Decorator which gets language template depending on file extension"""
    @functools.wraps(func)
    def decorator(ls, params, **kwargs):
        try:
            file_ext = get_file_extension(params.textDocument.uri).lower()
            lang_template = languages[file_ext]
            kwargs['lang_temp'] = lang_template
            return func(ls, params, **kwargs)
        except KeyError:
            pass
    return decorator


def is_ext_supported(uri, langs=LANG_EXTENSIONS):
    """Check if we have a support for model with given file extension."""
    file_ext = get_file_extension(uri)
    return file_ext.lower() in langs


def skip_not_supported_langs(func):
    """Decorator which checks if document is in the workspace and call
    decorated function.
    """
    @functools.wraps(func)
    def decorator(ls, params, **kwargs):
        try:
            doc = ls.workspace.documents[params.textDocument.uri]
            kwargs['doc'] = doc
            return func(ls, params, **kwargs)
        except KeyError:
            pass
    return decorator
