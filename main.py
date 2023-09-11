import logging

from environs import Env

from xkcd import download_random_xkcd
from vk import post_to_vk_group
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

    comic_path, comic_alt = None, ''
    try:
        comic_path, comic_alt = download_random_xkcd()
        post_to_vk_group(vk_access_token, vk_group_id, comic_path, comic_alt)
    finally:
        if isinstance(comic_path, Path):
            logging.info(f'Removing {comic_path}...')
            comic_path.unlink()

    logging.info(f'Done!')


if __name__ == '__main__':
    main()
