import json
import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
from iqos_backend.exceptions import ApiException
from iqos_backend.settings import COREZOID


@api_view(['POST'])
def test_survey(request):
    data = request.data
    try:
        if type(data) is not dict:
            raise ApiException(400, 1000, f"Type request not correct. The data in the request must be of the dictionary type but not {type(data).__name__}.")
        if len(data) == 0:
            raise ApiException(400, 1001, f"The request is empty. Dictionary must contain data.")
        if "questions" not in data:
            raise ApiException(400, 1002, f"Questions missing in request data")
        if (type(data["questions"])) is not list:
            raise ApiException(400, 1003, f"Type not correct. Type questions must by list but not {type(data['questions']).__name__}.")
        if (len(data["questions"])) > 3 or (len(data["questions"])) < 2:
            raise ApiException(400, 1004, "Incorrect number of questions. The number of questions must be 2 or 3.")
        for key in data["questions"]:
            if "question" not in key:
                raise ApiException(400, 1005, "Missing key 'question'")
            if "answer" not in key:
                raise ApiException(400, 1006, "Missing key 'answer'")
        if "token" not in data or (len(data["token"])) == 0:
            raise ApiException(401, 1005, 'Unauthorized')

         # Post to Corezoid https://www.corezoid.com
        data["title"] = "TEST_deeplace_heets_flavour_quiz"
        value = json.dumps(data)
        requests.post(COREZOID, data=value)

    except ApiException as api_ex:
        return api_ex.response

    return HttpResponse()


