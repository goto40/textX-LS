from __future__ import unicode_literals
from pytest import raises
import os
import textx.exceptions


def test_types_dsl():
    import types_data_flow_dsls
    mmT = types_data_flow_dsls.get_metamodel_types()
    current_dir = os.path.dirname(__file__)
    model = mmT.model_from_file(os.path.join(current_dir,
                                             'models',
                                             'types.type'))
    assert(model is not None)
    assert(len(model.types) == 2)

    with raises(textx.exceptions.TextXSyntaxError,
                match=r'.*lowercase.*'):
        mmT.model_from_file(os.path.join(current_dir,
                                         'models',
                                         'types_with_error.type'))
