import dataclasses

from nri_data_server.messages.CBorMessage import CBorMessage


@dataclasses.dataclass
class StringMessage(CBorMessage):
    value: str
