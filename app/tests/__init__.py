import logging

logging.basicConfig(
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(),
    ],
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

logging.getLogger("faker").setLevel(logging.CRITICAL)
logging.getLogger("factory").setLevel(logging.CRITICAL)
logging.getLogger("sqlalchemy").setLevel(logging.CRITICAL)
