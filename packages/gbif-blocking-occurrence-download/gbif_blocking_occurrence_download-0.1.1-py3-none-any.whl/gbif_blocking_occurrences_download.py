import logging
import pathlib
from time import sleep

import requests


def download_occurrences(
    predicate: dict,
    username: str,
    password: str,
    output_path: pathlib.Path,
    sleep_duration: int = 20,
) -> None:
    """
    Request an occurrence download at GBIF, wait for it to be ready and finally save the result.

    :param predicate: a predicate to select included occurrences. See: https://www.gbif.org/developer/occurrence#predicates
    :param username: a valid username (on GBIF.org)
    :param password: a valid password (on GBIF.org)
    :param output_path: a path and filename where the download will be saved
    :param sleep_duration: when waiting for the results to be ready, how long to wait between retries
    :return: nothing
    :raise: requests.exceptions.HTTPError when the occurrence download cannot be requested (i.e. 401 if credentials are invalid)
    """

    download_trigger = requests.post(
        "https://api.gbif.org/v1/occurrence/download/request",
        json=predicate,
        auth=(username, password),
    )

    download_trigger.raise_for_status()

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
