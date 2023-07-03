"""Методы для проверки наших запросов"""
import json

from requests import Response


class Checking():


    """Метод для проверки  статус кодов"""
    @staticmethod
    def check_status_code(response: Response, statsus_code):
        assert statsus_code == response.status_code
        if response.status_code == statsus_code:
            print("Усаешно  Статус код ="  + str(response.status_code))
        else:
            print("Провал Статус код = " + str(response.status_code))

    #
    """Метод проверки наличя полей в ответе запроса"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод проверки наличя значений обязательных  полей в ответе запроса"""
    @staticmethod
    def check_json_value(response: Response,field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + "  верен !")


    """Метод проверки наличя значений по наличию конкретного слова  в ответе запроса"""

    @staticmethod
    def check_json_word_in_value(response: Response, field_name, search_word):
        check = response.json()

        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово" + search_word + " присутствует")
        else:
            print("Слово" + search_word + " отсутствует")
            
