# MediaAccount Python Client

## Usage

```python
import datetime

apiKey = '123456789'
mediaAccount = MediaAccountClient(key=apiKey)

# raw client
(articles, nextPageLink, count) = mediaAccount.articles('ImportDatum', von=datetime(2021,1,1), bis=datetime(2021,2,1), maxItems=10)
(articles, nextPageLink, count) = mediaAccount.articleNext(nextPageLink)

```

## Development

### Build
```bash
    python -m build

    python -m twine upload --repository testpypi dist/*


```

### TODO

* Iterator
* Highlevel API #3
* V3 API #4
