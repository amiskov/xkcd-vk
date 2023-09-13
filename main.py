import logging

from environs import Env
import requests

from xkcd import download_random_xkcd
from vk import post_to_vk_group, VKAPIError
from pathlib import Path


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    env = Env()
    env.read_env()
    vk_access_token = env('VK_ACCESS_TOKEN')
    vk_group_id = env('VK_GROUP_ID')

    images_dir = Path('.')
    images_dir.mkdir(exist_ok=True)

    comic_path, comic_alt = None, ''
    try:
        comic_path, comic_alt = download_random_xkcd(images_dir)
        post_to_vk_group(vk_access_token, vk_group_id, comic_path, comic_alt)
    except VKAPIError as e:
        logging.error(f'VK API: {e}')
    except requests.RequestException as e:
        logging.error(f'HTTP: {e}')
    finally:
        if isinstance(comic_path, Path):
            logging.info(f'Removing {comic_path}...')
            comic_path.unlink()


if __name__ == '__main__':
    main()
