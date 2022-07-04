from rest_framework import mixins, viewsets


class ListRetrieveViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    Implement only List and Retrieve operations.
    """

    pass
