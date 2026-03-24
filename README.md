# Selenium Pytest Automation Framework

Run tests:
pytest --alluredir=allure-results
allure serve allure-results

Exemple:
1) Rulezi doar fișierul (cel mai simplu)
pytest tests/test_login_negative.py --alluredir=allure-results

2) Rulezi doar funcția de test (foarte util)
pytest tests/test_login_negative.py::test_login_negative --alluredir=allure-results

3) Rulezi doar un caz din parametrize (SUPER util)
pytest -k "wrong and SuperSecretPassword" --alluredir=allure-results

4) Rulezi după marker + filtrare
pytest -m regression -k "login_negative"

Când debug-ui un test:
pytest tests/test_login_negative.py::test_login_negative -v

pytest tests/test_login_negative.py -v