import dataclasses

from whoi_nlu_server_messages.CBorMessage import CBorMessage
from nri_data_server.messages.EmptyMessage import EmptyMessage


@dataclasses.dataclass
class NetworkDescribe(EmptyMessage):
    pass
