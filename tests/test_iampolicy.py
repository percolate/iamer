import unittest
from iamer.iampolicy import IamPolicy


class TestIamPolicy(unittest.TestCase):

    def test_iampolicy_diff(self):
        p1 = IamPolicy(u'some-policy', {})
        p2 = IamPolicy(u'another-policy', {})

        assert p1 != p2

    def test_iampolicy_eq(self):
        p1 = IamPolicy(u'some-policy', {})
        p2 = IamPolicy(u'some-policy', {})

        assert p1 == p2

    def test_iampolicy_lt(self):
        p1 = IamPolicy(u'some-policy', {})
        p2 = IamPolicy(u'another-policy', {})

        assert p2 < p1

    def test_iampolicy_gt(self):
        p1 = IamPolicy(u'some-policy', {})
        p2 = IamPolicy(u'another-policy', {})

        assert p1 > p2

    def test_iampolicy_not_lt_gt(self):
        p1 = IamPolicy(u'some-policy', {})
        p2 = IamPolicy(u'some-policy', {})

        assert not (p1 > p2)
        assert not (p1 < p2)
