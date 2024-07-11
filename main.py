import boto3



class S3Processor:

    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')


    def list(self):
        buckets_list = []

        for bucket in self.s3_resource.buckets.all():
            buckets_list.append(bucket.name)

        return buckets_list

    def get(self, bucket_name, file_name, download_path):
        try:
            self.s3_client.download_file(bucket_name, file_name, download_path)
        except Exception as e:
            print(f"Error:{e}")

    def put(self, bucket_name, file_name, upload_path):
        try:
            self.s3_client.upload_file(upload_path, bucket_name, file_name)
        except Exception as e:
            print(f"Error: {e}")

    def remove(self, bucket_name, file_name):

        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        except Exception as e:
            print(f"Error: {e}")

s3_processor = S3Processor()
# print(s3_processor.list())
# print(s3_processor.get('first-bucket-aaslanyann', 'error.txt', "./error.txt"))
# print(s3_processor.put('first-bucket-aaslanyann', 'error.txt', "./error.txt"))
print(s3_processor.remove('first-bucket-aaslanyann', 'error.txt'))

