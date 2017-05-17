
from webapp2 import RequestHandler
from google.appengine.api import app_identity
from google.cloud import storage
import uuid
import os

from models.assets import Assets

bucket_name = os.environ.get('WIX_BUCKET_NAME', app_identity.get_default_gcs_bucket_name())


class AssetsHandler(RequestHandler):

    def post(self):
        uploaded_file = self.request.POST.get("file")
        uploaded_file_content = uploaded_file.file.read()
        uploaded_file_filename = uploaded_file.filename
        uploaded_file_type = uploaded_file.type

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(str(uuid.uuid4()))

        blob.upload_from_string(uploaded_file_content, content_type=uploaded_file_type)
        blob.make_public()

        name = self.request.get('name')
        description = self.request.get('description')

        Assets(name=name, description=description, url=blob.public_url, original=uploaded_file_filename).put()

        self.redirect('/')
