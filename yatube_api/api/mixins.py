from rest_framework import mixins, viewsets


class ListRetrieveViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Implement only List and Retrieve operations.
    """

    pass


class ListCreateViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    Implement only List and Create operations.
    """

    pass
