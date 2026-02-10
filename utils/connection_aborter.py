from utils.logger import setup_logger

logger = setup_logger()

def aborter (route):
    logger.info(f"Blocking image request: {route.request.url}")
    route.abort()