# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
from xcapi.xray.app.router.command import command_pb


class RoutingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeRoutingStats = channel.unary_stream(
            '/xray.app.router.command.RoutingService/SubscribeRoutingStats',
            request_serializer=command_pb.SubscribeRoutingStatsRequest.SerializeToString,
            response_deserializer=command_pb.RoutingContext.FromString,
            _registered_method=True)
        self.TestRoute = channel.unary_unary(
            '/xray.app.router.command.RoutingService/TestRoute',
            request_serializer=command_pb.TestRouteRequest.SerializeToString,
            response_deserializer=command_pb.RoutingContext.FromString,
            _registered_method=True)
        self.GetBalancerInfo = channel.unary_unary(
            '/xray.app.router.command.RoutingService/GetBalancerInfo',
            request_serializer=command_pb.GetBalancerInfoRequest.SerializeToString,
            response_deserializer=command_pb.GetBalancerInfoResponse.FromString,
            _registered_method=True)
        self.OverrideBalancerTarget = channel.unary_unary(
            '/xray.app.router.command.RoutingService/OverrideBalancerTarget',
            request_serializer=command_pb.OverrideBalancerTargetRequest.SerializeToString,
            response_deserializer=command_pb.OverrideBalancerTargetResponse.FromString,
            _registered_method=True)
        self.AddRule = channel.unary_unary(
            '/xray.app.router.command.RoutingService/AddRule',
            request_serializer=command_pb.AddRuleRequest.SerializeToString,
            response_deserializer=command_pb.AddRuleResponse.FromString,
            _registered_method=True)
        self.RemoveRule = channel.unary_unary(
            '/xray.app.router.command.RoutingService/RemoveRule',
            request_serializer=command_pb.RemoveRuleRequest.SerializeToString,
            response_deserializer=command_pb.RemoveRuleResponse.FromString,
            _registered_method=True)