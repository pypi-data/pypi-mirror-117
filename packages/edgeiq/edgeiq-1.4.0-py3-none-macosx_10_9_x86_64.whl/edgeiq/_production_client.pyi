from edgeiq import constants as constants
from edgeiq._token_mgmt import JsonFile as JsonFile
from typing import Any

RANGE: int
ENDPOINT: Any
CLIENT_ID: Any
PROJECT_DIR: Any
CERTIFICATE_FOLDER: str
CERTIFICATES: Any
CREDENTIALS_EXIST: bool

class ProjectFile(JsonFile):
    def __init__(self) -> None: ...
    @property
    def project_id(self): ...

PATH_TO_CERT: Any
PATH_TO_KEY: Any
PATH_TO_ROOT: Any
PROJECT_FILE: Any
PROJECT_TAG: Any
TOPIC_PREFIX: str
TOPIC: Any

class IotCoreClient:
    mqtt_connection: Any
    exit_event: Any
    topic: Any
    def __init__(self) -> None: ...
    def publish_analytics(self, results, type, base_service, tag) -> None: ...
    def publish(self, message, topic) -> None: ...
    def stop(self) -> None: ...

class JSONFileWriterClient:
    exit_event: Any
    def __init__(self) -> None: ...
    def publish_analytics(self, results, type, base_service, tag) -> None: ...
    def publish(self, message, topic) -> None: ...
    def stop(self) -> None: ...

class DummyClient:
    def __init__(self) -> None: ...
    def publish_analytics(self, results, type, base_service, tag) -> None: ...
    def publish(self, message, topic) -> None: ...
    def stop(self) -> None: ...

PRODUCTION_CLIENT: Any
