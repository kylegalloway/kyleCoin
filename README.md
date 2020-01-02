# kyleCoin

A simple cryptocurrency based on the [Quincy Larson tutorial](https://www.freecodecamp.org/news/create-cryptocurrency-using-python/).

## Build with Docker

### Build Docker image

```sh
docker build -t kylecoin_image -f Dockerfile .
```

### Build application

```sh
docker run -it --rm --name=kyleCoin -v "$PWD":/src -u `id -u`:`id -g` kylecoin_image
```
