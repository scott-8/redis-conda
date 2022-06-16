import requests
import yaml

r = requests.get("https://raw.githubusercontent.com/ScoopInstaller/Main/master/bucket/redis.json")
d = r.json()

meta = {
    "package": {
        "name": "redis",
        "version": d["version"],
    },
    "source": {
        "url": d["architecture"]["64bit"]["url"],
        "sha256": d["architecture"]["64bit"]["hash"],
    },
    "build": {
        "skip": "True # [not win64]",
        "script": [f"copy {i} %LIBRARY_BIN%\\{i}" for i in d["bin"]],
    },
    "test": {
        "commands": [
            "redis-server --version",
            "redis-cli --version",
        ],
    },
    "about": {
        "home": d["homepage"],
        "license": d["license"],
        "summary": "Windows-compatible Redis package.",
        "description": d["description"],
        "dev_url": d["checkver"]["github"],
    },
    "extra": {
        "maintainers": [
            "scott",
        ]
    }
}

with open("meta.yaml", "w") as f:
    yaml.dump(meta, f, sort_keys=False)
