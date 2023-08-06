class component:
    __type__ = str()
    data = object()


class query:
    __type__ = str()
    query_id = int()


class itemStack:
    __identifier__ = str()
    __type__ = str()
    count = str()
    item = str()


class block:
    __identifier__ = str()
    __type__ = str()
    block_position = object()
    ticking_area = object()
