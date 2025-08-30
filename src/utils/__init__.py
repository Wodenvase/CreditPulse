import logging
import datetime

def setup_logger(name="creditpulse"):
    """
    Set up a basic logger.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

def format_currency(value, currency="USD"):
    """
    Format a number as currency.
    """
    return f"{currency} {value:,.2f}"

def validate_bond_data(bond_data):
    """
    Validate required fields in bond data.
    """
    required = ["bond_id", "issuer", "sector", "rating", "yield", "spread"]
    missing = [field for field in required if field not in bond_data or bond_data[field] is None]
    if missing:
        return False, f"Missing fields: {', '.join(missing)}"
    return True, "Valid"

def current_timestamp():
    """
    Return the current timestamp as a string.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")