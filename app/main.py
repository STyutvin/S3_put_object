def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio("play.min.io",
        access_key="minio-access-key",
        secret_key="minio-secret-key",
    )

    # The file to upload, change this path if needed
    source_file = "/tmp/kc_house_data.csv"

    # The destination bucket and filename on the MinIO server
    bucket_name = "python-minio-bucket"
    destination_file = "kc_house_data.csv"

    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)