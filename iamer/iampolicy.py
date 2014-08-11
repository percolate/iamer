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
