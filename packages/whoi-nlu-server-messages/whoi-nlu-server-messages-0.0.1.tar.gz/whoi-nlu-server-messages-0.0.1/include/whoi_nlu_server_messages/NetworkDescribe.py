import dataclasses

from nri_data_server.messages.CBorMessage import CBorMessage
from nri_data_server.messages.EmptyMessage import EmptyMessage


@dataclasses.dataclass
class NetworkDescribe(EmptyMessage):
    pass
