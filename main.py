import logging

from environs import Env

from xkcd import download_random_xkcd
from vk import post_to_vk_group


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

    env = Env()
    env.read_env()
    VK_ACCESS_TOKEN = env('VK_ACCESS_TOKEN')
    VK_GROUP_ID = env('VK_GROUP_ID')

    comic_path, comic_alt = download_random_xkcd()
    post_to_vk_group(VK_ACCESS_TOKEN, VK_GROUP_ID, comic_path, comic_alt)
    comic_path.unlink()
    logging.info(f'File {comic_path} was successfully posted and removed.')


if __name__ == '__main__':
    main()
