# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
from xcapi.xray.app.proxyman.command import command_pb


class HandlerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddInbound = channel.unary_unary(
            '/xray.app.proxyman.command.HandlerService/AddInbound',
            request_serializer=command_pb.AddInboundRequest.SerializeToString,
            response_deserializer=command_pb.AddInboundResponse.FromString,
            _registered_method=True)
        self.RemoveInbound = channel.unary_unary(
            '/xray.app.proxyman.command.HandlerService/RemoveInbound',
            request_serializer=command_pb.RemoveInboundRequest.SerializeToString,
            response_deserializer=command_pb.RemoveInboundResponse.FromString,
            _registered_method=True)
        self.AlterInbound = channel.unary_unary(
            '/xray.app.proxyman.command.HandlerService/AlterInbound',
            request_serializer=command_pb.AlterInboundRequest.SerializeToString,
            response_deserializer=command_pb.AlterInboundResponse.FromString,
            _registered_method=True)
        self.AddOutbound = channel.unary_unary(
            '/xray.app.proxyman.command.HandlerService/AddOutbound',
            request_serializer=command_pb.AddOutboundRequest.SerializeToString,
            response_deserializer=command_pb.AddOutboundResponse.FromString,
            _registered_method=True)
        self.RemoveOutbound = channel.unary_unary(
            '/xray.app.proxyman.command.HandlerService/RemoveOutbound',
            request_serializer=command_pb.RemoveOutboundRequest.SerializeToString,
            response_deserializer=command_pb.RemoveOutboundResponse.FromString,
            _registered_method=True)
        self.AlterOutbound = channel.unary_unary(
            '/xray.app.proxyman.command.HandlerService/AlterOutbound',
            request_serializer=command_pb.AlterOutboundRequest.SerializeToString,
            response_deserializer=command_pb.AlterOutboundResponse.FromString,
            _registered_method=True)