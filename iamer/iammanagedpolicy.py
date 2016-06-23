from functools import total_ordering


@total_ordering
class IamManagedPolicy(object):
    def __init__(self, name, arn, version, document):
        assert isinstance(name, unicode)
        assert isinstance(arn, unicode)
        assert isinstance(version, unicode)
        assert isinstance(document, dict)

        self._name = name
        self._arn = arn
        self._version = version
        self._document = document

    @property
    def name(self):
        """
        Returns:
            unicode
        """
        return self._name

    @property
    def arn(self):
        """
        Returns:
            unicode
        """
        return self._arn

    @property
    def version(self):
        """
        Returns:
            unicode
        """
        return self._version

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
