# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Glue42(Component):
    """A Glue42 component.
The Glue42 initializer component. The component should be placed at the root of the application.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (optional):
    The ID of this component. Used to identify Dash components in
    callbacks.  The ID must be unique across all components in an app.

- fallback (a list of or a singular dash component, string or number; optional):
    An optional component to display while initializing Glue42.

- isEnterprise (boolean; optional):
    Indicates whether the application is running in Glue42 Enterprise
    or Glue42 Core.

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes to Dash in order to make them available for callbacks.

- settings (default {    type: CoreApplicationTypes.Client,}):
    A `settings` object containing configuration objects for the
    Glue42 library."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, isEnterprise=Component.UNDEFINED, settings=Component.UNDEFINED, fallback=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'fallback', 'isEnterprise', 'setProps', 'settings']
        self._type = 'Glue42'
        self._namespace = 'dash_glue42'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'fallback', 'isEnterprise', 'setProps', 'settings']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Glue42, self).__init__(children=children, **args)
