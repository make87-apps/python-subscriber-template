import logging
import time

from make87_messages.text.text_plain_pb2 import PlainText
from make87.encodings import ProtobufEncoder
from make87.interfaces.zenoh import ZenohInterface

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    format="[%(asctime)sZ %(levelname)s  %(name)s] %(message)s", level=logging.INFO, datefmt="%Y-%m-%dT%H:%M:%S"
)


def main():
    message_encoder = ProtobufEncoder(message_type=PlainText)
    zenoh_interface = ZenohInterface(name="zenoh")
    subscriber = zenoh_interface.get_subscriber("incoming_message")

    for sample in subscriber:
        message = message_encoder.decode(sample.payload.to_bytes())
        logging.info(f"Received: '{message}'")


if __name__ == "__main__":
    main()
