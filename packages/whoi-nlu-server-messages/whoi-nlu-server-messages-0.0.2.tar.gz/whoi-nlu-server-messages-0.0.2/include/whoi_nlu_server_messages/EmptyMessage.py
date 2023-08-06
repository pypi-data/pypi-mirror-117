import dataclasses

from whoi_nlu_server_messages.CBorMessage import CBorMessage


@dataclasses.dataclass
class EmptyMessage(CBorMessage):
    __empty__: str
