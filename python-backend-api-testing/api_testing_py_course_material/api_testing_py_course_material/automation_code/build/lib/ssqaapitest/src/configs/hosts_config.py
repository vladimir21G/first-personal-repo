
API_HOSTS = {
    "test": "https://baharmustafa.com/vladi",
    "dev": "",
    "prod": ""
}
WOO_API_HOSTS = {
    "test": "https://baharmustafa.com/vladi",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
              "test": {"host": "127.0.0.1",
                       "database": "wp398",
                       "table_prefix": "wp2p_",
                       "socket": "/Users/admas/Library/Application Support/Local/run/5MQbIjSnl/mysql/mysqld.sock",
                       "port": 3306
                       },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'docker': {
              "test": {
                  "host": "host.docker.internal",
                  "database": "wp398",
                  "table_prefix": "wp2p_",
                  "socket": None,
                  "port": 3306
              },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'machine2': {
        "test": {"host": "localhost",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "/Users/akinfu/Library/Application Support/Local/run/d84nqkpSm/mysql/mysqld.sock",
                 "port": 3306
                 },
        "dev": {
                  "host": "host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
        "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
    }
}
