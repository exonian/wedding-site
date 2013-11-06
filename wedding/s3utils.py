from storages.backends.s3boto import S3BotoStorage

media_root = lambda: S3BotoStorage(location='client_media')
static_root = lambda: S3BotoStorage(location='static_media')
