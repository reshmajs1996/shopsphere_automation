import logging
from pathlib import Path

LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)
logging.basicConfig(
    filename="logs/framework.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# dont need this, instead every class will use this with logger = logging.getLogger(__name__)


def get_logger(name):
    return logging.getLogger(name)

# this will be the usage in all the modules

# from utilities.logger import get_logger
# logger = get_logger(__name__)