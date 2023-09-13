# Publish xkcd comics to VK group
With this script you can easily publish random [xkcd picture](https://xkcd.com) to your VK community wall.

## Install
Install deps with [Poetry](https://python-poetry.org):

```sh
poetry install
```

## Add Credentials
Add environment variables `VK_ACCESS_TOKEN` and `VK_GROUP_ID` to `.env` file using `.env.example` as a template:

```sh
cp .env.example .env
```

`VK_ACCESS_TOKEN` you can [generate here](https://vk.com/dev/implicit_flow_user) and `VK_GROUP_ID` is your community id which you can [check here](https://regvk.com/id/).

## Run
Run this command to download random xkcd comic and publish it to your VK group:

```sh
poetry run python main.py
```
