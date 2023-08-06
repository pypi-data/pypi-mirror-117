# fastdb

## Firestore Example:

> NOTE: Make sure to export `GOOGLE_APPLICATION_CREDENTIALS` in environment variables which points to the service account file.

```py
from fastdb.firestore import Firestore

fs = Firestore()

user = fs.client.collection("users").document("4GH5IOyQVYCMMrdwRm0D").get()

```
