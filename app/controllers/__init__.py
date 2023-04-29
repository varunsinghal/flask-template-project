import logging
from uuid import uuid4

from commons.database import get_session


class Controller:
    def __init__(self):
        self.log = logging.getLogger(__class__.__name__)
        self.request_id = uuid4().hex
        self.session = get_session()
