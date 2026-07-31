from google.cloud import storage


# Google Cloud configuration

PROJECT_ID = "macro-data-platform1"
BUCKET_NAME = "wb-imf-datalake-1"


# Authenticate Google Cloud Storage

client = storage.Client(project=PROJECT_ID)


# Create upload function

def upload_to_gcs(source_file_name, destination_blob_name):

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to "
        f"{destination_blob_name}."
    )