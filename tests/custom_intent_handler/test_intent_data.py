intent_data = {
    "module_name": {
        "name": "module_name",
        "value": "Cannabis Vera",
        "confirmationStatus": "NONE",
        "source": "USER"
    }
}

wrong_intent_data = {
    "module_name": {
        "name": "module_name",
        "value": "Wrong Module Name",
        "confirmationStatus": "NONE",
        "source": "USER"
    }
}

mock_response = [
  {
    "id": 10,
    "device_id": "1234",
    "version": "1.0",
    "system_type": "TNS",
    "name": "Cannabis Vera",
    "measurements": {
      "date": None,
      "water_temperature": 19,
      "tds": None,
      "ph": 6,
      "ec": None,
      "do": None,
      "orp": None,
      "module": None
    },
    "device_status": False
  }
]
