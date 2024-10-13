from grpc import insecure_channel, Channel
from xcapi.xray.app.proxyman.command.command_grpc_pb import HandlerServiceStub
from xcapi.xray.app.proxyman.config_pb import SenderConfig
from xcapi.xray.app.proxyman.command.command_pb import AddOutboundRequest
from xcapi.xray.core.config_pb import OutboundHandlerConfig
from xcapi.xray.common.serial.typed_message_pb import ToTypedMessage, GetMessageType
from xcapi.xray.proxy.vless.outbound.config_pb import Config as VlessOutboundConfig
from xcapi.xray.common.protocol.server_spec_pb import ServerEndpoint
from xcapi.xray.common.net.address_pb import IPOrDomain
from xcapi.xray.common.protocol.user_pb import User
from xcapi.xray.proxy.vless.account_pb import Account as VlessAccount
from xcapi.xray.transport.internet.config_pb import StreamConfig, TransportConfig
from xcapi.xray.transport.internet.websocket.config_pb import Config as WebsocketConfig
from xcapi.xray.transport.internet.tls.config_pb import Config as TlsConfig
from xcapi.xray.app.proxyman.config_pb import MultiplexingConfig

if __name__ == '__main__':
    host: str = '127.0.0.1'
    port: str = '11514'
    channel: Channel = insecure_channel(f'{host}:{port}')
    handlerServiceStub: HandlerServiceStub = HandlerServiceStub(channel)
    # add outbound
    handlerServiceStub.AddOutbound(
        AddOutboundRequest(
            outbound=OutboundHandlerConfig(
                tag="outbound-1",
                proxy_settings=ToTypedMessage(
                    VlessOutboundConfig(
                        vnext=[
                            ServerEndpoint(
                                address=IPOrDomain(
                                    domain="xxx.xxx.com"
                                ),
                                port=443,
                                user=[
                                    User(
                                        level=0,
                                        email="user@qq.com",
                                        account=ToTypedMessage(
                                            VlessAccount(
                                                id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                                flow="",
                                                encryption="none"

                                            )
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                ),
                sender_settings=ToTypedMessage(
                    SenderConfig(
                        stream_settings=StreamConfig(
                            protocol_name="websocket",
                            transport_settings=[
                                TransportConfig(
                                    protocol_name="websocket",
                                    settings=ToTypedMessage(
                                        WebsocketConfig(
                                            path="/tls",
                                            accept_proxy_protocol=False
                                        )
                                    ),
                                )
                            ],
                            security_type=GetMessageType(TlsConfig),
                            security_settings=[
                                ToTypedMessage(
                                    TlsConfig(
                                        allow_insecure=False,
                                        fingerprint="",
                                    )
                                )
                            ]
                        ),
                        multiplex_settings=MultiplexingConfig(
                            enabled=True,
                            concurrency=8
                        )
                    )
                ),
            )
        )
    )
    handlerServiceStub.AddOutbound(
        AddOutboundRequest(
            outbound=OutboundHandlerConfig(
                tag="outbound-2",
                proxy_settings=ToTypedMessage(
                    VlessOutboundConfig(
                        vnext=[
                            ServerEndpoint(
                                address=IPOrDomain(
                                    domain="xxx.xxx.com"
                                ),
                                port=443,
                                user=[
                                    User(
                                        level=0,
                                        email="user@gmail.com",
                                        account=ToTypedMessage(
                                            VlessAccount(
                                                id="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                                                flow="",
                                                encryption="none"

                                            )
                                        )
                                    )
                                ]
                            )
                        ]
                    )
                ),
                sender_settings=ToTypedMessage(
                    SenderConfig(
                        stream_settings=StreamConfig(
                            protocol_name="websocket",
                            transport_settings=[
                                TransportConfig(
                                    protocol_name="websocket",
                                    settings=ToTypedMessage(
                                        WebsocketConfig(
                                            path="/tls",
                                            accept_proxy_protocol=False
                                        )
                                    ),
                                )
                            ],
                            security_type=GetMessageType(TlsConfig),
                            security_settings=[
                                ToTypedMessage(
                                    TlsConfig(
                                        allow_insecure=False,
                                        fingerprint="",
                                    )
                                )
                            ]
                        ),
                        multiplex_settings=MultiplexingConfig(
                            enabled=True,
                            concurrency=8
                        )
                    )
                ),
            )
        )
    )
