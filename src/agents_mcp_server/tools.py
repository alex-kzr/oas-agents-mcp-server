"""Safe synthetic/local tools; no filesystem, shell, network or account access."""


def echo(text: str) -> dict:
    """Echo at most 200 printable synthetic characters."""
    if len(text)>200 or not text.isprintable():
        raise ValueError('Synthetic echo input outside limits')
    return {'text':text,'source':'synthetic'}


def lookup(key: str) -> dict:
    """Look up an allowlisted synthetic task fixture."""
    if key != 'sample.discount':
        raise ValueError('Unknown synthetic fixture key')
    return {'fixture_id':key,'order_total':100,'discount_percent':10,'expected_total':90,'source':'synthetic'}


def controlled_error() -> str:
    """Return a controlled failure for diagnostics, without user data."""
    raise ValueError('Synthetic controlled tool failure')
