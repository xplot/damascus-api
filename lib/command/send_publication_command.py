import requests
import logging
import json
from requests.auth import HTTPBasicAuth

class SendPublicationViaHttpCommand(object):

    def __init__(self, publication):
        self.publication = publication

    def execute(self):
        """

        """
        response = None

        try:
            response = self._make_request(self.publication)

        except Exception, e:
            if response:
                logging.error(response.text)
        finally:
            pass

    def _make_request(self, publication):
        """
            Executes the actual request to the command url
            This method will take the following into consideration
            1 - It will assume the headers and params and body are already template filled
                for instance params like key={{key_value}}&key2=2 or
                urls like www.google.com/{{key_value}}/api, have already being replaced
            3 - It will fail whenever a non-200 status is obtained
        """
        request_auth = None

        if publication.username and publication.password:
            request_auth = HTTPBasicAuth(
                publication.username,
                publication.password
            )

        timeout = 30
        if publication.timeout:
            timeout = 60

        response = requests.request(
            publication.method or 'GET',
            publication.endpoint,
            headers=publication.headers,
            params=publication.params,
            data=publication.body,
            auth=request_auth,
            timeout=timeout
        )

        if response is not None:
            print response.text
            logging.info(response.text)

        response.raise_for_status()

        return response