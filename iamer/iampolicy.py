from functools import total_ordering


@total_ordering
class IamPolicy(object):
    def __init__(self, name, document):
        assert isinstance(name, unicode)
        assert isinstance(document, dict)

        self._name = name
        self._document = document

    @property
    def name(self):
        """
        Returns:
            unicode
        """
        return self._name

    @property
    def document(self):
        """
        Returns:
            unicode
        """
        return self._document

    def __eq__(self, other):
        return (self.name == other.name)

    def __lt__(self, other):
        return (self.name < other.name)

    def __hash__(self):
        return hash((self.__class__, self.name))
