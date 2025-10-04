

central_registry = {}


def set_central_registry(key, object):
    central_registry[key] = object
    return object

def get_central_registry(key):
    return central_registry.get(key)