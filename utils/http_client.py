import requests
from utils.logger import logger

def post_json(url: str, data: dict = None, timeout: int = 10):
    try:
        response = requests.post(url, json=data or {}, timeout=timeout)
        response.raise_for_status()
        return response.json(), response.status_code

    except requests.exceptions.HTTPError as errh:
        logger.warning(f"[HTTP Error] {url} | {errh}")
        return None, response.status_code if response else 500

    except requests.exceptions.ConnectionError as errc:
        logger.warning(f"[Connection Error] {url} | {errc}")
        return None, 502

    except requests.exceptions.Timeout as errt:
        logger.warning(f"[Timeout] {url} | {errt}")
        return None, 504

    except requests.exceptions.RequestException as err:
        logger.error(f"[Unknown Error] {url} | {err}")
        return None, 500
