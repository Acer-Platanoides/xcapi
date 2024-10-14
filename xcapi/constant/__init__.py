class Protocol(object):
    Vless: str = "vless"
    Vmess: str = "vmess"
    Ss: str = "ss"
    Socks: str = "socks"
    Http: str = "http"
    Trojan: str = "trojan"
    Hysteria2: str = "hysteria2"
    Tuic: str = "tuic"
    Wireguard: str = "wireguard"


class Transport(object):
    Ws: str = "websocket"


class SecurityType(object):
    Tls: str = "tls"
