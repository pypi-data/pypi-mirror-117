# installed-packages-diff - Compare packages and versions on servers

## Prerequisites

* GNU make
* python >= 3.9
* pipenv

## Usage

### Setup

```bash
make install_deps
```

### Run tests

```bash
make tests
```

### Create a config config.yml

```yaml
groups:
  web:
    servers:
      - username: root
        hostname: web-dev
        excludes:
          - "missing"
      - username: root
        hostname: web-live
```

### Run installed-packages-diff

```bash
make run
```

## License

Copyright (c) 2021 by [Cornelius Buschka](https://github.com/cbuschka).

[MIT](./license.txt)