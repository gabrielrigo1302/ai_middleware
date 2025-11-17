from enum import Enum


class AgentIntenticEnum(str, Enum):
    generic_ask = "generic_ask"
    send_email = "send_email"
    create_log = "create_log"
