import json
import os
import requests

from dataUtils.decor import retry


class DBClient:

    @staticmethod
    # https://www.python.org/dev/peps/pep-0484/#the-problem-of-forward-declarations
    def GetDBClient(apiKey: str) -> 'DBClient':
        return DBClient(apiKey)

    def __init__(self, apiKey: str):
        self._apiKey = apiKey
        self._devAPI = "https://ommunitystaging-enginedevapi.dev.rialtic.dev/"
        self._headers = {
            "Content-Type": "application/json",
            "x-api-key": self._apiKey
        }

    @retry
    def GetHistory(
            self,
            transactionId: str,
            noOfDays: int
    ) -> (list, str):
        if os.environ.get('RIALTIC_DATA_ENV') == 'local':
            return self._getHistoryLocal(os.environ.get('RIALTIC_HISTORY_FILE'))
        else:
            return self._getHistoryDev(transactionId, noOfDays)

    @retry
    def GetReferenceData(self, transactionId: str, query: str) -> (list, str):
        return self._getReferenceDataDev(transactionId, query)

    def _getHistoryDev(self, transactionId: str, noOfDays: int) -> (list, str):
        historyEvent = {
            'transactionId': transactionId,
            'daysOfHistory': noOfDays
        }
        res = requests.post(self._devAPI + "history", json=historyEvent, headers=self._headers)

        if res.ok:
            return res.json(), None
        else:
            try:
                return None, res.json()["Message"]
            except KeyError:
                return None, res.json()["message"]

    def _getHistoryLocal(self, filename: str) -> (list, str):
        with open(os.path.join(os.getcwd(), filename), 'r') as history_file:
            return json.loads(history_file.read()), None

    def _getReferenceDataDev(self, transactionId: str, query: str) -> (list, str):
        referenceDataEvent = {
            'transactionId': transactionId,
            'query': query,
        }

        res = requests.post(self._devAPI + "referencedata", json=referenceDataEvent, headers=self._headers)

        # LOGGER.info("%s", vars(res))
        if res.ok:
            return res.json(), None
        else:
            try:
                return None, res.json()["Message"]
            except KeyError:
                return None, res.json()["message"]
