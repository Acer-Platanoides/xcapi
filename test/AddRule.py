from grpc import insecure_channel, Channel
from xcapi.xray.app.router.command.command_pb import AddRuleRequest
from xcapi.xray.app.router.command.command_grpc_pb import RoutingServiceStub
from xcapi.xray.common.serial.typed_message_pb import ToTypedMessage
from xcapi.xray.app.router.config_pb import Config, RoutingRule
if __name__ == '__main__':
    host: str = '127.0.0.1'
    port: str = '11514'
    channel: Channel = insecure_channel(f'{host}:{port}')
    # router
    routingServiceStub: RoutingServiceStub = RoutingServiceStub(channel)
    routingServiceStub.AddRule(
        AddRuleRequest(
            shouldAppend=False,
            config=ToTypedMessage(
                Config(
                    domain_strategy=Config.DomainStrategy.IpIfNonMatch,
                    rule=[
                        RoutingRule(
                            tag="outbound-1",
                            inbound_tag=["socks"],
                            rule_tag="outbound-1"
                        ),
                        RoutingRule(
                            tag="outbound-2",
                            inbound_tag=["http"],
                            rule_tag="outbound-2"
                        )
                    ]
                )
            )
        )
    )















