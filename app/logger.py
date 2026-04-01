import logging
import json

def configure_logging():
    logger = logging.getLogger("api_logger")
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}'
    ))
    logger.addHandler(handler)
    return logger

def log_event(logger, level, event, **kwargs):
    log_data = {"event": event, **kwargs}
    log_method = getattr(logger, level, logger.info)
    log_method(json.dumps(log_data))