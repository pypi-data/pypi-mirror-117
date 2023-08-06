import dataclasses

from nri_data_server.messages.CBorMessage import CBorMessage


@dataclasses.dataclass
class EmptyMessage(CBorMessage):
    __empty__: str
