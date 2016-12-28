import os
import oauth2client
import oauth2client.client
from oauth2client.client import GoogleCredentials
from oauth2client.client import ApplicationDefaultCredentialsError
def getCredentials():
    client_credentials=os.environ["GOOGLE_CLOUD_CREDENTIALS"]
    if client_credentials is not None:
        credentials_type = client_credentials.get('type')
        if credentials_type == oauth2client.client.AUTHORIZED_USER:
            required_fields = set(['client_id', 'client_secret', 'refresh_token'])
        elif credentials_type == oauth2client.client.SERVICE_ACCOUNT:
            required_fields = set(['client_id', 'client_email', 'private_key_id',
                               'private_key'])
        else:
            raise ApplicationDefaultCredentialsError(
            "'type' field should be defined (and have one of the '" +
            oauth2client.client.AUTHORIZED_USER + "' or '" + oauth2client.client.SERVICE_ACCOUNT + "' values)")
        missing_fields = required_fields.difference(client_credentials.keys())
        if missing_fields:
            _raise_exception_for_missing_fields(missing_fields)
        if client_credentials['type'] == oauth2client.client.AUTHORIZED_USER:
            return GoogleCredentials(
                access_token=None,
                client_id=client_credentials['client_id'],
                client_secret=client_credentials['client_secret'],
                refresh_token=client_credentials['refresh_token'],
                token_expiry=None,
                token_uri=oauth2client.GOOGLE_TOKEN_URI,
                user_agent='Python client library')
        else:  # client_credentials['type'] == SERVICE_ACCOUNT
            from oauth2client import service_account
            return service_account._JWTAccessCredentials.from_json_keyfile_dict(
                   client_credentials)
    else:
        raise ApplicationDefaultCredentialsError("No environment variable found for credentials")   
        
def _raise_exception_for_missing_fields(missing_fields):
    raise ApplicationDefaultCredentialsError(
        'The following field(s) must be defined: ' + ', '.join(missing_fields))
    
