import os
from typing import Dict

import requests
from requests import Response, HTTPError

from ..io_tools.exception import EndpointError


class ApiHandler:
    url = os.environ.get("LUNA_APP_URL")
    body = {"username": os.environ.get("LUNA_APP_USERNAME"),
            "password": os.environ.get("LUNA_APP_PASSWORD")}

    def __init__(self):
        self._generate_token()

    def _generate_token(self) -> None:
        try:
            authorization = self._authorize()
        except HTTPError:
            raise EndpointError
        if authorization.status_code != 204:
            self.token = authorization.json()["access"]
            self.headers = {"Authorization": f"Bearer {self.token}"}
        else:
            raise HTTPError

    def _authorize(self) -> Response:
        response = requests.post(f"{self.url}api-auth/token/", data=self.body)
        response.raise_for_status()
        return response

    def get_module_list(self) -> list[Dict]:
        response = requests.get(f"{self.url}hydroponics/industrial-hydroponic/", headers=self.headers, data=self.body)
        response.raise_for_status()
        return response.json()

    def get_module_history(self, module_id: int,
                           start_date: str = None, end_date: str = None, count: str = None) -> list:
        body = self.body | {"start_date": start_date, "end_date": end_date, "measurements_count": count}
        response = requests.get(f"{self.url}hydroponics/"
                                f"industrial-hydroponic-measurements/{module_id}/",
                                headers=self.headers, data=body)
        response.raise_for_status()
        return response.json()
