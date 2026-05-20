# GoF Design Patterns

This folder contains small examples of Gang of Four design patterns used in a
Python style that fits this local RAG project.

## Singleton Pattern

The Singleton pattern makes sure a class has only one shared instance and gives
the application one global access point to it.

Use it when:

- An object is expensive to create repeatedly.
- The same configuration or service registry must be reused everywhere.
- Multiple parts of the app should share one consistent state.

Avoid it when:

- Normal dependency injection is enough.
- The shared state makes tests harder to isolate.
- Different parts of the app need different configurations.

## Examples

- `singleton_01_config_manager.py` - one shared application settings object.
- `singleton_02_service_registry.py` - one shared registry for reusable services.

