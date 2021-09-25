'''
reports
=======

The reports methods allow interaction into ContainerSecurity
reports API.

Methods available on ``cs.reports``:

.. rst-class:: hide-signature
.. autoclass:: ReportAPI

    .. automethod:: report
'''
from .base import CSEndpoint
from typing import Dict

class ReportAPI(CSEndpoint):
    def report(
            self,
            digest: str) -> Dict:
        '''
        Retrieves the image report by the image digest.

        Args:
            digest (str): The image digest.

        Returns:
            dict: The report resource record.
        '''

        _digest = self._check('digest', digest, str)
        return self._api.get(f'reports/{_digest}').json()
