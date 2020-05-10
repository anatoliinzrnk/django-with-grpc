from google.protobuf import empty_pb2

from django_grpc_framework.protobuf.json_format import (
    message_to_dict, parse_dict
)


class CreateModelMixin:
    def Create(self, request, context):
        """
        Create a model instance.

        The request shoule be a proto message of ``get_protobuf_class()``.  If
        an object is created this returns a proto message of
        ``get_protobuf_class()``.
        """
        data = message_to_dict(request)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        protobuf_class = self.get_protobuf_class()
        return parse_dict(serializer.data, protobuf_class())

    def perform_create(self, serializer):
        """Save a new object instance."""
        serializer.save()


class ListModelMixin:
    def List(self, request, context):
        """
        List a queryset.  This sends a sequence of messages of
        ``get_protobuf_class()`` to the client.

        .. note::

            This is a server streaming RPC.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        protobuf_class = self.get_protobuf_class()
        for data in serializer.data:
            yield parse_dict(data, protobuf_class())


class RetrieveModelMixin:
    def Retrieve(self, request, context):
        """
        Retrieve a model instance.

        The request have to include a field corresponding to
        ``lookup_request_field``.  If an object can be retrieved this returns
        a proto message of ``get_protobuf_class()``.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        protobuf_class = self.get_protobuf_class()
        return parse_dict(serializer.data, protobuf_class())


class UpdateModelMixin:
    def Update(self, request, context):
        """
        Update a model instance.

        The request shoule be a proto message of ``get_protobuf_class()``.  If
        an object is updated this returns a proto message of
        ``get_protobuf_class()``.
        """
        instance = self.get_object()
        data = message_to_dict(request)
        serializer = self.get_serializer(instance, data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        protobuf_class = self.get_protobuf_class()
        return parse_dict(serializer.data, protobuf_class())

    def perform_update(self, serializer):
        """Save an existing object instance."""
        serializer.save()


class DestroyModelMixin:
    def Destroy(self, request, context):
        """
        Destroy a model instance.

        The request have to include a field corresponding to
        ``lookup_request_field``.  If an object is deleted this returns
        a proto message of ``google.protobuf.empty_pb2.Empty``.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return empty_pb2.Empty()

    def perform_destroy(self, instance):
        """Delete an object instance."""
        instance.delete()
