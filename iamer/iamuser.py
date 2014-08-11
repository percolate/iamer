from functools import total_ordering

from iampolicy import IamPolicy


@total_ordering
class IamUser(object):
    """Represent a user in IAM"""
    def __init__(self, name, groups, policies):
        """
        Args:
            name (unicode)
            groups (set)
            policies (set)
        """
        assert isinstance(name, unicode)
        assert isinstance(groups, set)
        assert all(isinstance(group, unicode) for group in groups)
        assert isinstance(policies, set)
        assert all(isinstance(policy, IamPolicy) for policy in policies)

        self._name = name
        self._groups = groups
        self._policies = policies

    @property
    def name(self):
        """
        Returns:
            unicode
        """
        return self._name

    @property
    def groups(self):
        """
        Returns:
            set of unicode
        """
        return self._groups

    @property
    def policies(self):
        """
        Returns:
            set of IamPolicy
        """
        return self._policies

    def __eq__(self, other):
        return (self.name == other.name)

    def __lt__(self, other):
        return (self.name < other.name)

    def __hash__(self):
        return hash((self.__class__, self.name))
