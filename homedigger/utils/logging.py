import logging

logging.basicConfig(
    filename="homedigger.log",
    datefmt="%d-%b-%y %H:%M:%S",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    force=True,
    level=logging.INFO,
)


def log_this(function):
    def wrapper(*args, **kwargs):
        try:
            logging.info(
                f"Running {function.__name__} with args {args} and kwargs {kwargs}"
            )
            return function(*args, **kwargs)
        except Exception as e:
            logging.error(e)
            raise e

    return wrapper
