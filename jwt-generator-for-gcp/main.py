from datetime import datetime, timedelta
from jwt import JWT, jwk_from_pem
from jwt.utils import get_int_from_datetime

instance = JWT()

project_id = "<GCP Project ID>"

token = {
    # The time that the token was issued at
    'iat': get_int_from_datetime(datetime.utcnow()),
    # The time the token expires.
    # Google recommends a expiry after 20 minutes
    'exp': get_int_from_datetime(datetime.utcnow() + timedelta(minutes=20)),
    'aud': project_id
}

private_key_file = "path/to/rsaPrivatekey.pem"  # Key File should be in pem format

algorithm = 'RS256'

with open(private_key_file, 'rb') as f:
    private_key = jwk_from_pem(f.read())

generated_jwt = instance.encode(token, private_key, alg=algorithm)

print(generated_jwt)


