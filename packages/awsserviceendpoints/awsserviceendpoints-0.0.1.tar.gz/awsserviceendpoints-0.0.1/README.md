# awsserviceendpoints
Micropackage that changes `boto3` to return the standard service endpoints

This package will replace the legacy AWS endpoints for all services with
the modern endpoints. Boto3 (really, botocore) is still using the legacy
endpoints for some services (most notably SQS) in order to support Python
2.6/2.7. This is unnecessary for Python 3 (and some Python 2.7) users, and 
causes problems with other libraries (and VPC endpoints) that have moved 
to the new service endpoints.

Note that this will only enable the modern endpoints if `ssl.HAS_SNI` returns
`True`.

To use, simply ensure that this library is imported prior to `boto3` being
imported.

```python
import awspython3serviceendpoints
import boto3
```
