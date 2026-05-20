from dataclasses import dataclass
from pathlib import Path
from threading import Lock


@dataclass(frozen=True)
class AppSettings:
    docs_dir: Path = Path("data/docs")
    uploaded_docs_dir: Path = Path("data/uploaded_docs")
    vector_db_dir: Path = Path("data/vector_db/chroma")
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    generation_model: str = "google/flan-t5-small"
    reranker_model: str = "BAAI/bge-reranker-base"


class ConfigManager:
    """Singleton that exposes one shared AppSettings object."""

    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.settings = AppSettings()
        return cls._instance

    def get_settings(self) -> AppSettings:
        return self.settings


if __name__ == "__main__":
    first_config = ConfigManager()
    second_config = ConfigManager()

    print(first_config is second_config)
    print(first_config.get_settings().embedding_model)

