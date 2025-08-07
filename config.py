import os


def data(query, bookmark):

    data_dict = {
        "options": {
            "applied_unified_filters": None,
            "appliedProductFilters": "---",
            "article": None,
            "auto_correction_disabled": False,
            "corpus": None,
            "customized_rerank_type": None,
            "domains": None,
            "filters": None,
            "journey_depth": None,
            "page_size": None,
            "price_max": None,
            "price_min": None,
            "query_pin_sigs": None,
            "query": query,
            "redux_normalize_feed": True,
            "request_params": None,
            "rs": "typed",
            "scope": "pins",
            "selected_one_bar_modules": None,
            "seoDrawerEnabled": False,
            "source_id": None,
            "source_module_id": None,
            "source_url": "/search/pins/?q=машина&rs=typed",
            "top_pin_id": None,
            "top_pin_ids": None,
            "bookmarks": [bookmark]  # ← вот тут вставляем переменную
        },
        "context": {}
    }
    return data_dict


def headers():
    headers = {
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'accept-language': os.getenv('ACCEPT_LANGUAGE'),
        'content-type': 'application/x-www-form-urlencoded',
        'origin': os.getenv('ORIGIN'),
        'priority': 'u=1, i',
        'referer': os.getenv('REFERER'),
        'screen-dpr': '1',
        'sec-ch-ua': os.getenv('SEC_CH_UA'),
        'sec-ch-ua-full-version-list': os.getenv('SEC_CH_UA_FULL_VERSION_LIST'),
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': os.getenv('SEC_CH_UA_PLATFORM'),
        'sec-ch-ua-platform-version': os.getenv('SEC_CH_UA_PLATFORM_VERSION'),
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': os.getenv('USER_AGENT'),
        'x-app-version': os.getenv('X_APP_VERSION'),
        'x-b3-flags': '0',
        'x-b3-parentspanid': os.getenv('X_B3_PARENTSPANID'),
        'x-b3-spanid': os.getenv('X_B3_SPANID'),
        'x-b3-traceid': os.getenv('X_B3_TRACEID'),
        'x-csrftoken': os.getenv('X_CSRFTOKEN'),
        'x-pinterest-appstate': os.getenv('X_PINTEREST_APPSTATE'),
        'x-pinterest-pws-handler': os.getenv('X_PINTEREST_PWS_HANDLER'),
        'x-pinterest-source-url': os.getenv('X_PINTEREST_SOURCE_URL'),
        'x-requested-with': 'XMLHttpRequest'
    }

    return headers

def cookies():
    cookies = {
        '_pinterest_sess': os.getenv('PINTEREST_SESS'),
        '_auth': os.getenv('AUTH'),
        'csrftoken': os.getenv('CSRF_TOKEN'),
        '_routing_id': os.getenv('ROUTING_ID'),
        'sessionFunnelEventLogged': '1',
    }
    return cookies
