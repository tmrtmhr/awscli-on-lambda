import subprocess


# sync buckets
def handle(event, context):
    command = [
        "./aws", "s3", "sync", "s3://from-bucket/path/",
        "s3://to-bucket/path/", "--exact-timestamps", "--delete"
    ]
    print(subprocess.call(command, stderr=subprocess.STDOUT))
