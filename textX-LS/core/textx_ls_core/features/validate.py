from typing import List, Optional

from textx.exceptions import TextXError

from ..languages import LanguageTemplate


def validate(lang: LanguageTemplate, model_str) -> Optional[List[TextXError]]:
    """Validates given model. For now returned list will contain maximum one
    error, since textX does not have built-in error recovery mechanism.
    """
    errors = []
    try:
        lang.metamodel.model_from_str(model_str)
    except TextXError as e:
        errors.append(e)
    return errors
