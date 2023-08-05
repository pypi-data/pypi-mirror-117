# MediaAccount Python Client

Documentation for the api hier: <http://api.media-account.de/>

## Usage

```python
import datetime

apiKey = '123456789'
mediaAccount = MediaAccountClient(key=apiKey)

# raw client
(articles, nextPageLink, count) = mediaAccount.articles('ImportDatum', von=datetime(2021,1,1), bis=datetime(2021,2,1), maxItems=10)
(articles, nextPageLink, count) = mediaAccount.articleNext(nextPageLink)

# full request
scroll = client.scroll('ImportDatum', von = '04.08.2021', bis = '05.08.2021', maxItems=1000)
articlesAll = [i[0] for i in scroll]
```

## Development

### Build
```bash
    # publish to test
    ./publish.sh test

    # publish to prod
    ./publish.sh prod
```

### Roadmap

* Integration Api-V3
