import base64
import re
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
from xcapi.xray.app.proxyman.config_pb import SenderConfig
from xcapi.xray.app.proxyman.command.command_pb import AddOutboundRequest
from xcapi.xray.common.serial.typed_message_pb import ToTypedMessage, GetMessageType, TypedMessage
from xcapi.xray.proxy.vless.outbound.config_pb import Config as VlessOutboundConfig
from xcapi.xray.common.protocol.server_spec_pb import ServerEndpoint
from xcapi.xray.common.net.address_pb import IPOrDomain
from xcapi.xray.common.protocol.user_pb import User
from xcapi.xray.proxy.vless.account_pb import Account as VlessAccount
from xcapi.xray.transport.internet.config_pb import StreamConfig, TransportConfig
from xcapi.xray.transport.internet.websocket.config_pb import Config as WebsocketConfig
from xcapi.xray.transport.internet.tls.config_pb import Config as TlsConfig
from urllib.parse import parse_qs
from xcapi.constant import Protocol, Transport, SecurityType
from xcapi.xray.core.config_pb import OutboundHandlerConfig


@dataclass
class KeyValuePair(object):
    Key: str
    Value: str


class ParamKey(object):
    Encryption: str = "encryption"
    Flow: str = "flow"
    Security: str = "security"
    Sni: str = "sni"
    Alpn: str = "alpn"
    Type: str = "type"
    Host: str = "host"
    Path: str = "path"
    Fp: str = "fp"
    AllowInsecure: str = "allowInsecure"

    Id: str = "id"
    Address: str = "address"
    Port: str = "port"
    Remarks: str = "remarks"
    Protocol: str = "protocol"


class Constants(object):
    Host: str = "host"


updateParam: Dict[str, KeyValuePair] = {
    ParamKey.Type: KeyValuePair("ws", "websocket")
}


class XrayN(object):

    @staticmethod
    def Transform(outbound: str) -> List[AddOutboundRequest]:
        requests: List[AddOutboundRequest] = []
        s: Optional[str] = None
        try:
            b = base64.b64decode(outbound)
            s = b.decode()
        except Exception:
            s = outbound
        servers = [part for part in s.split("\r\n") if part]
        for server in servers:
            requests.append(XrayN.GetAddOutboundRequest(server))
        return requests

    @staticmethod
    def FormatDict(dt: Dict[str, List[Any]]) -> Dict[str, Any]:
        data: Dict[str, Any] = {}
        for key in dt:
            if len(dt[key]) == 1:
                data[key] = dt[key][0]
            else:
                data[key] = dt[key]
        for pKey in updateParam:
            if data.get(pKey) and data.get(pKey) == updateParam.get(pKey).Key:
                data[pKey] = updateParam.get(pKey).Value
        return data

    @staticmethod
    def GetAddOutboundRequest(server: str) -> AddOutboundRequest:
        param: Dict[str, Any] = {}
        # Parse
        # todo Other Protocol
        if re.match(f'^{Protocol.Vless}', server):
            r = r'([^:]+)://([^@]+)@([^:]+):(\d+)\?([^#]+)#{0,1}(.+){0,1}'
            match = re.match(r, server)
            if match:
                data = parse_qs(match.group(5)),
                param = XrayN.FormatDict(data[0])
                param[ParamKey.Protocol] = match.group(1)
                param[ParamKey.Id] = match.group(2)
                param[ParamKey.Address] = match.group(3)
                param[ParamKey.Port] = match.group(4)
                param[ParamKey.Remarks] = match.group(6)
        outbound = OutboundHandlerConfig(
            tag=param.get(ParamKey.Remarks),
            proxy_settings=XrayN.GetProxySettings(param),
            sender_settings=ToTypedMessage(
                SenderConfig(
                    stream_settings=StreamConfig(
                        protocol_name=param.get(ParamKey.Type),
                        transport_settings=[
                            TransportConfig(
                                protocol_name=param.get(ParamKey.Type),
                                settings=XrayN.GetTransportConfigSettings(param),
                            )
                        ],
                        security_type=XrayN.GetSecurityType(param),
                        security_settings=[XrayN.GetSecuritySettings(param)]
                    )
                )
            )
        )
        request: AddOutboundRequest = AddOutboundRequest(
            outbound=outbound,
        )
        return request

    @staticmethod
    def GetProxySettings(param: Dict[str, Any]) -> TypedMessage:
        message: Optional[TypedMessage] = None
        # todo Other Protocol
        if Protocol.Vless == param.get(ParamKey.Protocol):
            oc = VlessOutboundConfig(
                vnext=[ServerEndpoint(
                    address=IPOrDomain(domain=param.get(ParamKey.Address)),
                    port=int(param.get(ParamKey.Port)),
                    user=[
                        User(
                            account=XrayN.GetAccount(param),
                        )
                    ]
                )]
            )
            message = ToTypedMessage(oc)
        return message

    @staticmethod
    def GetAccount(param: Dict[str, Any]) -> TypedMessage:
        message: Optional[TypedMessage] = None
        # todo Other Protocol
        if Protocol.Vless == param.get(ParamKey.Protocol):
            account = VlessAccount(
                id=param.get(ParamKey.Id),
                flow=param.get(ParamKey.Flow),
                encryption=param.get(ParamKey.Encryption),
            )
            message = ToTypedMessage(account)
        return message

    @staticmethod
    def GetTransportConfigSettings(param: Dict[str, Any]) -> TypedMessage:
        message: Optional[TypedMessage] = None
        # todo Other Transport
        if Transport.Ws == param.get(ParamKey.Type):
            config = WebsocketConfig(
                path=param.get(ParamKey.Path),
                host=param.get(ParamKey.Host),
                header={Constants.Host: param.get(ParamKey.Host)} if param.get(ParamKey.Host) else None,
            )
            message = ToTypedMessage(config)
        return message

    @staticmethod
    def GetSecurityType(param: Dict[str, Any]) -> str:
        s: Optional[str] = None
        # todo Other SecurityType
        if SecurityType.Tls == param.get(ParamKey.Security):
            s = GetMessageType(TlsConfig)
        return s

    @staticmethod
    def GetSecuritySettings(param: Dict[str, Any]) -> TypedMessage:
        message: Optional[TypedMessage] = None
        # todo Other SecurityType
        if SecurityType.Tls == param.get(ParamKey.Security):
            cg = TlsConfig(
                allow_insecure=param.get(ParamKey.AllowInsecure),
                fingerprint=param.get(ParamKey.Fp),
            )
            message = ToTypedMessage(cg)
        return message
