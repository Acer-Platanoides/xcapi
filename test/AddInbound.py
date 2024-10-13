from grpc import insecure_channel, Channel
from xcapi.xray.app.proxyman.command.command_grpc_pb import HandlerServiceStub
from xcapi.xray.app.proxyman.config_pb import ReceiverConfig, SniffingConfig
from xcapi.xray.app.proxyman.command.command_pb import AddInboundRequest
from xcapi.xray.common.net.port_pb import PortList, PortRange
from xcapi.xray.core.config_pb import InboundHandlerConfig
from xcapi.xray.common.serial.typed_message_pb import ToTypedMessage
from xcapi.xray.common.net.address_pb import IPOrDomain
from xcapi.xray.proxy.socks.config_pb import ServerConfig as SocksServerConfig, AuthType
from xcapi.xray.proxy.http.config_pb import ServerConfig as HttpServerConfig

if __name__ == '__main__':
    host: str = '127.0.0.1'
    port: str = '11514'
    channel: Channel = insecure_channel(f'{host}:{port}')
    handlerServiceStub: HandlerServiceStub = HandlerServiceStub(channel)
    # add socks inbound
    handlerServiceStub.AddInbound(
        AddInboundRequest(
            inbound=InboundHandlerConfig(
                tag="socks",
                receiver_settings=ToTypedMessage(
                    ReceiverConfig(
                        port_list=PortList(
                            range=[
                                PortRange(
                                    From=10808,
                                    To=10808,
                                )
                            ]
                        ),
                        listen=IPOrDomain(
                            ip=bytes([0, 0, 0, 0])
                        ),
                        sniffing_settings=SniffingConfig(
                            enabled=True,
                            destination_override=["http", "tls"]
                        )
                    )
                ),
                proxy_settings=ToTypedMessage(
                    SocksServerConfig(
                        auth_type=AuthType.PASSWORD,
                        accounts={
                            "xray": "xray"
                        },
                        address=IPOrDomain(
                            ip=bytes([0, 0, 0, 0])
                        ),
                        udp_enabled=True,
                    )
                )
            )
        )
    )
    # add http inbound
    handlerServiceStub.AddInbound(
        AddInboundRequest(
            inbound=InboundHandlerConfig(
                tag="http",
                receiver_settings=ToTypedMessage(
                    ReceiverConfig(
                        port_list=PortList(
                            range=[
                                PortRange(
                                    From=10809,
                                    To=10809,
                                )
                            ]
                        ),
                        listen=IPOrDomain(
                            ip=bytes([0, 0, 0, 0])
                        ),
                        sniffing_settings=SniffingConfig(
                            enabled=True,
                            destination_override=["http", "tls"]
                        )
                    )
                ),
                proxy_settings=ToTypedMessage(
                    HttpServerConfig(
                        accounts={
                            "xray": "xray"
                        }
                    )
                )
            )
        )
    )
