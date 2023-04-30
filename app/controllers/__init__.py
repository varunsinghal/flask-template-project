import logging
from uuid import uuid4

from sqlalchemy.orm import Session


class Controller:
    def __init__(self, session: Session):
        self.log = logging.getLogger(__class__.__name__)
        self.request_id = uuid4().hex
        self.session = session
