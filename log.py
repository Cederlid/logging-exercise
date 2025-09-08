import logging

logging.basicConfig(level=logging.INFO)
data = [1,2,3]

def fetch_data():
    logging.info("Hämtar data...")
    if not data:
        logging.warning("no data found")
    return data

def process_data(data):
    try:
        if not data:
            logging.warning("no data")
            return None
        logging.info("Bearbetar data: %s", data)
        return sum(data) / len(data)
    except Exception:
        logging.exception("Fel i process_data")
        return None

def main():
    logging.info("Program startar...")
    data = fetch_data()
    result = process_data(data)
    if result is not None:
        logging.info("Resultat: %s", result)
    logging.info("Program klart.")

if __name__ == "__main__":
    main()
