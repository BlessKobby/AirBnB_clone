#!/usr/bin/python3
"""__init__ (initialization) for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
