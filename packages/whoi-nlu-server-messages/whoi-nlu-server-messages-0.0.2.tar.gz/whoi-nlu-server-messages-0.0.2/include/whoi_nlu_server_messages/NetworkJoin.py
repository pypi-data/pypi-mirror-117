import dataclasses

from nri_data_server.messages.EmptyMessage import EmptyMessage


@dataclasses.dataclass
class NetworkJoin(EmptyMessage):
    pass
