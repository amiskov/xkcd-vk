from pathlib import Path
import logging

import requests

VK_API_URL = 'https://api.vk.com/method'


def post_to_vk_group(access_token: str, group_id: str, comic_path: Path,
                     comic_alt: str):
    upload_url = get_upload_url(access_token, group_id)
    uploaded_img = upload_img(comic_path, upload_url)
    wall_photo = save_wall_photo(access_token, group_id, uploaded_img['photo'],
                                 uploaded_img['server'], uploaded_img['hash'])
    post_to_wall(access_token, group_id, comic_alt, wall_photo['owner_id'],
                 wall_photo['id'])


def post_to_wall(access_token: str, group_id: str, message: str, owner_id: int,
                 media_id: int):
    url = f'{VK_API_URL}/wall.post'
    params = {
        'owner_id': f'-{group_id}',
        'message': message,
        'group_id': group_id,
        'access_token': access_token,
        'from_group': 1,
        'attachments': f'photo{owner_id}_{media_id}',
        'v': 5.131
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()


def upload_img(filename: Path, upload_url: str):
    with open(filename, 'rb') as file:
        files = {
            'photo': file,
        }
        resp = requests.post(upload_url, files=files)
        resp.raise_for_status()
        return resp.json()


def save_wall_photo(access_token: str, group_id: str, photo: str, server: int,
                    hash_: str):
    url = f'{VK_API_URL}/photos.saveWallPhoto'
    params = {
        'access_token': access_token,
        'group_id': group_id,
        'photo': photo,
        'server': server,
        'hash': hash_,
        'v': 5.131
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()['response'][0]


def get_upload_url(access_token: str, group_id: str) -> str:
    url = f'{VK_API_URL}/photos.getWallUploadServer'
    params = {
        'access_token': access_token,
        'group_id': group_id,
        'v': 5.131
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.json()['response']['upload_url']


def download_image(dir: str, url: str) -> Path:
    """Download an image by `url` to `dir`.

    `url` must have a file extension at the end (`.png`, `.jpg`, etc).
    """
    response = requests.get(url)
    response.raise_for_status()

    images_path = Path(dir)
    images_path.mkdir(exist_ok=True)

    filename = url.split('/')[-1]
    with open(images_path.joinpath(filename), 'wb') as file:
        file.write(response.content)
        logging.info(f'{filename} has been saved.')
        return images_path / filename
