# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from blog_proto import post_pb2 as blog__proto_dot_post__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class PostControllerStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/blog_proto.PostController/List',
                request_serializer=blog__proto_dot_post__pb2.PostListRequest.SerializeToString,
                response_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                )
        self.Create = channel.unary_unary(
                '/blog_proto.PostController/Create',
                request_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
                response_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/blog_proto.PostController/Retrieve',
                request_serializer=blog__proto_dot_post__pb2.PostRetrieveRequest.SerializeToString,
                response_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                )
        self.Update = channel.unary_unary(
                '/blog_proto.PostController/Update',
                request_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
                response_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/blog_proto.PostController/Destroy',
                request_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class PostControllerServicer(object):
    """Missing associated documentation comment in .proto file"""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PostControllerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=blog__proto_dot_post__pb2.PostListRequest.FromString,
                    response_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                    response_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=blog__proto_dot_post__pb2.PostRetrieveRequest.FromString,
                    response_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                    response_serializer=blog__proto_dot_post__pb2.Post.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=blog__proto_dot_post__pb2.Post.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blog_proto.PostController', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PostController(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blog_proto.PostController/List',
            blog__proto_dot_post__pb2.PostListRequest.SerializeToString,
            blog__proto_dot_post__pb2.Post.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blog_proto.PostController/Create',
            blog__proto_dot_post__pb2.Post.SerializeToString,
            blog__proto_dot_post__pb2.Post.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blog_proto.PostController/Retrieve',
            blog__proto_dot_post__pb2.PostRetrieveRequest.SerializeToString,
            blog__proto_dot_post__pb2.Post.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blog_proto.PostController/Update',
            blog__proto_dot_post__pb2.Post.SerializeToString,
            blog__proto_dot_post__pb2.Post.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blog_proto.PostController/Destroy',
            blog__proto_dot_post__pb2.Post.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
