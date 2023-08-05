# MediaAccount Python Client

Documentation for the api hier: <http://api.media-account.de/>

Package found here: <https://pypi.org/project/mediaaccount/>

## Usage

The client supports the python logging-package for detailed information.

### Request articles

```python
import datetime
from mediaaccount import MediaAccountClient

apiKey = '123456789'
mediaAccount = MediaAccountClient(key=apiKey)

# raw client
articles, nextlink, count = client.articles('ImportDatum', von = '01.05.2021', bis = '05.08.2021', maxItems=150)
articles, nextPageLink, count = mediaAccount.articleNext(nextPageLink)

# full request
scroll = client.scroll('ImportDatum', von = '04.08.2021', bis = '05.08.2021', maxItems=1000)
articlesAll = [i[0] for i in scroll]
```

## Development

### Publish

```bash
    ./publish.sh test     # publish to test
```

```bash
    ./publish.sh prod     # publish to prod
```

### Roadmap

Board: <https://github.com/CKrowiorsch/mediaaccount-py/projects/1>

* Integration Api-V3
