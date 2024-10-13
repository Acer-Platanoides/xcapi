# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
from xcapi.xray.transport.internet.grpc.encoding import stream_pb


class GRPCServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Tun = channel.stream_stream(
            '/xray.transport.internet.grpc.encoding.GRPCService/Tun',
            request_serializer=stream_pb.Hunk.SerializeToString,
            response_deserializer=stream_pb.Hunk.FromString,
            _registered_method=True)
        self.TunMulti = channel.stream_stream(
            '/xray.transport.internet.grpc.encoding.GRPCService/TunMulti',
            request_serializer=stream_pb.MultiHunk.SerializeToString,
            response_deserializer=stream_pb.MultiHunk.FromString,
            _registered_method=True)
