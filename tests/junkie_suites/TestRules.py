from test_junkie.objects import TestObject, SuiteObject
from test_junkie.rules import Rules


class TestRules(Rules):

    def __init__(self, **kwargs):

        Rules.__init__(self, **kwargs)

    def before_class(self):
        assert isinstance(self.kwargs.get("suite"), SuiteObject), "Suite Object must be passed to the before_test()"

    def before_test(self, **kwargs):
        assert isinstance(kwargs.get("test"), TestObject), "Test Object must be passed to the before_test()"
        assert isinstance(self.kwargs.get("suite"), SuiteObject), "Suite Object must be passed to the before_test()"

    def after_test(self, **kwargs):
        assert isinstance(kwargs.get("test"), TestObject), "Test Object must be passed to the before_test()"
        assert isinstance(self.kwargs.get("suite"), SuiteObject), "Suite Object must be passed to the before_test()"

    def after_class(self):
        assert isinstance(self.kwargs.get("suite"), SuiteObject), "Suite Object must be passed to the before_test()"
