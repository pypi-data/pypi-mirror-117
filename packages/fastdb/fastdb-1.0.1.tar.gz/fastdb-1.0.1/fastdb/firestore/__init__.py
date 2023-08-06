import firebase_admin
from firebase_admin import firestore
from google.cloud.firestore import Client

from ..common import Singleton


class Firestore(metaclass=Singleton):
    def __init__(self) -> None:
        firebase_admin.initialize_app()
        self.client: Client = firestore.client()
