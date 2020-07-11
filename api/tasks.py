import requests

from ping_sites.celery import app
from api.models import Site


@app.task
def ping_site(site_id):

    site = Site.objects.get(site_id=int(site_id))
    resp = requests.get(site.site_url)
    if resp.status_code > 299:
        is_active = False
    else:
        is_active = True

    if is_active != site.is_active:
        site.is_active = is_active

    site.save(update_fields=['is_active'])

    if is_active:
        return f'site {site.site_url} is running'
    else:
        return f'site {site.site_url} is stopped'
