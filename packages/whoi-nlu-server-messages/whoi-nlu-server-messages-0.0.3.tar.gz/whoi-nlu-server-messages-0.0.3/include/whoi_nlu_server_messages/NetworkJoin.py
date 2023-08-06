import dataclasses

from whoi_nlu_server_messages.EmptyMessage import EmptyMessage


@dataclasses.dataclass
class NetworkJoin(EmptyMessage):
    pass
