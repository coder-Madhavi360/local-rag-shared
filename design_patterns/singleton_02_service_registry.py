from threading import Lock


class ServiceRegistry:
    """Singleton registry for sharing reusable application services."""

    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._services = {}
        return cls._instance

    def register(self, name: str, service: object) -> None:
        self._services[name] = service

    def get(self, name: str) -> object:
        if name not in self._services:
            raise KeyError(f"Service not registered: {name}")
        return self._services[name]

    def has(self, name: str) -> bool:
        return name in self._services


if __name__ == "__main__":
    first_registry = ServiceRegistry()
    second_registry = ServiceRegistry()

    first_registry.register("embedding_model", "BAAI/bge-small-en-v1.5")

    print(first_registry is second_registry)
    print(second_registry.get("embedding_model"))

