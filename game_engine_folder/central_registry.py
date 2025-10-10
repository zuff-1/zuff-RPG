

central_registry = {}


class CentralRegistryControls:

    def set_central_registry(
            key,
            object
            ):
        central_registry[key] = object

    def get_central_registry(key):
        return central_registry.get(key)
    
def test_CentralRegistryControls():
    (
    CentralRegistryControls.
    set_central_registry(
        "The Key",
        "Object In Registry!!!"
        )
    )
    obj = (
    CentralRegistryControls.
    get_central_registry("The Key")
    )
    print(obj)
    print(central_registry)


if __name__ == "__main__":
    test_CentralRegistryControls()