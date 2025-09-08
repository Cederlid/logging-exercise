import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
)
logger = logging.getLogger(__name__)
data = [1,2,3]

def fetch_data():
    logger.info("Hämtar data...")
    if not data:
        logger.warning("no data found")
    return data

def process_data(data):
    try:
        if not data:
            logger.warning("no data")
            return None
        logger.info("Bearbetar data: %s", data)
        return sum(data) / len(data)
    except Exception:
        logger.exception("Fel i process_data")
        return None

def main():
    logger.info("Program startar…")
    data = fetch_data()
    result = process_data(data)
    if result is not None:
        logger.info("Resultat: %s", result)
    logger.info("Program klart.")

if __name__ == "__main__":
    main()
