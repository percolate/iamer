import unittest
from iamer.main import IamUser


class TestIamUser(unittest.TestCase):

    def test_iamuser_diff(self):
        u1 = IamUser(u'joe', set(), set())
        u2 = IamUser(u'bill', set(), set())

        assert u1 != u2

    def test_iamuser_eq(self):
        u1 = IamUser(u'joe', set(), set())
        u2 = IamUser(u'joe', set(), set())

        assert u1 == u2

    def test_iamuser_lt(self):
        u1 = IamUser(u'joe', set(), set())
        u2 = IamUser(u'bill', set(), set())

        assert u2 < u1

    def test_iamuser_gt(self):
        u1 = IamUser(u'joe', set(), set())
        u2 = IamUser(u'bill', set(), set())

        assert u1 > u2

    def test_iamuser_not_lt_gt(self):
        u1 = IamUser(u'joe', set(), set())
        u2 = IamUser(u'joe', set(), set())

        assert not (u1 > u2)
        assert not (u1 < u2)
