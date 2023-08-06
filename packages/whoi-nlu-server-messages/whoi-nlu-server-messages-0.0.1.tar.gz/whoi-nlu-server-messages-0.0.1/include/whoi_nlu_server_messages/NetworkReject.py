import dataclasses

from nri_data_server.messages.CBorMessage import CBorMessage


@dataclasses.dataclass
class NetworkReject(CBorMessage):
    reason: str
