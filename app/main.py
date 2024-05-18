from minio import Minio
# Initialize MinIO client
client = Minio('localhost:9000',
               access_key='minio_access_key',
               secret_key='minio_secret_key',
               secure=False)

source_file = "d:/Geek_Brains/Project/misc/minio-python-app/app/tmp/kc_house_data.csv"
bucket_name = "python-test-bucket"
destination_file = "kc_house_data.csv"

# Make a bucket
found = client.bucket_exists(bucket_name)
if not found:
    client.make_bucket(bucket_name)
    print("Created bucket", bucket_name)
else:
    print("Bucket", bucket_name, "already exists")

# Upload an object
client.fput_object(bucket_name, destination_file, source_file)

# List objects
objects = client.list_objects(bucket_name, recursive=True)
for obj in objects:
    print(obj.object_name)