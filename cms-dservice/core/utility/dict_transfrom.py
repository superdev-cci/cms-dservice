def dict_to_list(data, use_key=True):
    pool = []

    for k, v in data.items():
        if use_key is True:
            v['key'] = k
        pool.append(v)

    return pool


def list_to_dict(data, key):
    pool = {}

    for x in data:
        key_value = x.get(key)
        pool[key_value] = x

    return pool
