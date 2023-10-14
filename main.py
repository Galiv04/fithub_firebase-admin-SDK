
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./ServiceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()
# doc_ref = store.collection('exercises').limit(2)

# try:
#     docs = doc_ref.get()
#     for doc in docs:
#         print('Doc Data:{}'.format(doc.to_dict()))
# except google.cloud.exceptions.NotFound:
#     print('Missing data')

doc_ref = store.collection('test').document("ciao")
doc_ref.set({'name': 'test', 'added': 'just now'})