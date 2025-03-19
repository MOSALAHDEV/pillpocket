#!/usr/bin/python3
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage_type = os.getenv("PILLPOCKET_TYPE_STORAGE")
if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
