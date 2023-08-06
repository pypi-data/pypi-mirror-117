import logging
from time import sleep

import requests


def download_occurrences(
    predicate: dict,
    username: str,
    password: str,
    output_path: str,
    sleep_duration: int = 20
) -> None:

    download_trigger = requests.post(
        "https://api.gbif.org/v1/occurrence/download/request",
        json=predicate,
        auth=(username, password),
    )
    download_id = download_trigger.text
    logging.info(f"Download triggered, download_id is {download_id}")

    while True:
        logging.info(f"(re)trying to get download {download_id}...")
        download_get = requests.get(
            f"https://api.gbif.org/v1/occurrence/download/request/{download_id}"
        )
        status = download_get.status_code

        if status != 404:  # 404: not ready yet
            if status == 200:
                logging.info(f"Download is ready, getting it")
                with open(output_path, "wb") as f:
                    f.write(download_get.content)
            else:
                logging.warning(f"Status is {status}, why?")
                logging.warning(download_get)
            break

        sleep(sleep_duration)