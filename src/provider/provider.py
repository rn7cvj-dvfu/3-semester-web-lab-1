
from src.api.listener import Listener
from src.api.sender import Sender
from src.utils.converter import Converter



global CONVERTER_PROVIDER
CONVERTER_PROVIDER: Converter = Converter()

global LISTENER_PROVIDER
LISTENER_PROVIDER: Listener = Listener()

global SENDER_PROVIDER
SENDER_PROVIDER: Sender = Sender(CONVERTER_PROVIDER)

