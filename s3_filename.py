import boto3

class s3_filename:
    def __init__(self, path, bucket_name, directory):
        self.path = path
        self.filenames = []
        self.directory = directory
        self.bucket_files = None
        self.s3r = None
        self.bucket = None
        self.bucket_name = bucket_name
        self.setup_boto()

    def setup_boto(self):
        s3 = boto3.client('s3')
        s3_client = boto3.client('s3')

        self.s3r = boto3.resource('s3')
        self.bucket = self.s3r.Bucket(self.bucket_name)
        self.bucket_files = list(self.bucket.objects.all())

    def get_filenames_hs3(self):
        for file in self.bucket_files:
            if(file.key[0:4] == self.directory and len(file.key) > len(self.directory)):
                self.filenames.append(file.key[4:])
        return self.filenames