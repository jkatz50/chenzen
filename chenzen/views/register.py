from chenzen import chenzen, base_url
from entriesapi import EntriesAPI
from userapi import UserAPI


def register_api(view, endpoint, url, pk='id'):
    view_func = view.as_view(endpoint)
    chenzen.add_url_rule(url, defaults={pk: None},
                         view_func=view_func, methods=['GET', ])
    chenzen.add_url_rule(url, view_func=view_func, methods=['POST', ])
    chenzen.add_url_rule('%s<%s>' % (url, pk), view_func=view_func,
                         methods=['GET', 'PUT', 'DELETE'])

register_api(EntryAPI, 'entry_api', '/entries/', pk='id')
register_api(UserAPI, 'user_api', '/users/', pk='id')
