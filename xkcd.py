import random
from pathlib import Path
import logging

import requests


def download_random_xkcd(images_dir: Path) -> tuple[Path, str]:
    comic_id = get_random_comic_id()
    url, alt = get_comic_info(comic_id)
    return download_image(images_dir, url), alt


def get_comic_info(id: int) -> tuple[str, str]:
    """Return comic image URL and its description.

    > get_comic_info(353)
    ('https://imgs.xkcd.com/comics/python.png',
     "I wrote 20 short programs in Python yesterday...")
    """
    comic_url = f'https://xkcd.com/{id}/info.0.json'
    resp = requests.get(comic_url)
    resp.raise_for_status()
    comic_meta = resp.json()
    return comic_meta['img'], comic_meta['alt']


def get_random_comic_id() -> int:
    resp = requests.get('https://xkcd.com/info.0.json')
    resp.raise_for_status()
    return random.randint(1, resp.json()['num'])


def download_image(dir: Path, url: str) -> Path:
    """Download an image by `url` to `dir`.

    `url` must have a file extension at the end (`.png`, `.jpg`, etc).
    """
    response = requests.get(url)
    response.raise_for_status()

    filename = url.split('/')[-1]
    with open(dir.joinpath(filename), 'wb') as file:
        file.write(response.content)
    logging.info(f'{filename} has been saved.')
    return dir / filename
