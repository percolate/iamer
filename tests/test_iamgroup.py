import unittest
from iamer.iamgroup import IamGroup


class TestIamGroup(unittest.TestCase):

    def test_iamgroup_diff(self):
        g1 = IamGroup(u'some-group', set())
        g2 = IamGroup(u'another-group', set())

        assert g1 != g2

    def test_iamgroup_eq(self):
        g1 = IamGroup(u'some-group', set())
        g2 = IamGroup(u'some-group', set())

        assert g1 == g2

    def test_iamgroup_lt(self):
        g1 = IamGroup(u'some-group', set())
        g2 = IamGroup(u'another-group', set())

        assert g2 < g1

    def test_iamgroup_gt(self):
        g1 = IamGroup(u'some-group', set())
        g2 = IamGroup(u'another-group', set())

        assert g1 > g2

    def test_iamgroup_not_lt_gt(self):
        g1 = IamGroup(u'some-group', set())
        g2 = IamGroup(u'some-group', set())

        assert not (g1 > g2)
        assert not (g1 < g2)
