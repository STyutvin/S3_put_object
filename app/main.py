from minio import Minio
# Initialize MinIO client
client = Minio('localhost:9001',
               access_key='minio_access_key',
               secret_key='minio_secret_key',
               secure=False)

source_file = "/tmp/kc_house_data.csv"
bucket_name = "python-test-bucket"
destination_file = "kc_house_data.csv"

# Make a bucket
client.make_bucket(bucket_name)

# Upload an object
client.fput_object(bucket_name, destination_file, source_file)

# List objects
objects = client.list_objects(bucket_name, recursive=True)
for obj in objects:
    print(obj.object_name)