# Publish xkcd comics to VK group

## Install
Install deps with [Poetry](https://python-poetry.org):

```sh
poetry install
```

Grab your [VK access token](https://vk.com/dev/implicit_flow_user) and [group id](https://regvk.com/id/) and paste it into `.env`. Use `.env.example` as a template.

## Run
Run this command to download a random xkcd comic and publish it to your VK group:

```sh
poetry run python main.py
```
