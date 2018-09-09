`Conftest.py`

This plugin contain directory-specific hooks and fixtures(Explained below). 


Some uses of conftest plugin:
- Fixture: fixtures are defined for static data used by tests. This could be data as well as helpers of modules which will be passed to all tests.This data is accessed by all tests in the suite unless specified. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins.

- Hooks: Pytest implements all aspects of configuration, collection, running and reporting by calling well specified hooks. Hook functions are implemented by 'pytest_' prefix. Session and test running activities will invoke all hooks defined in conftest.py files closer to the root of the filesystem.
