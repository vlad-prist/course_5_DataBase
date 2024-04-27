import requests

@staticmethod
def get_company(company_list):
    url = 'https://api.hh.ru/employers'
    comp_list = []
    for company in company_list:
        response = requests.get(url, params={
            'text': company,
            'page': 0,
            'per_page': 100,
            'area': 113,
            'only_with_vacancies': True,
            'only_with_salary': True
        })
        if response.status_code != 200:
            print(f"Ошибка {response.status_code}")
        else:
            companies = response.json()['items']
            for el in companies:
                comp_list.append({
                    'employer_id': el['id'],
                    'name': el['name'],
                    'url': el['alternate_url'],
                    'vacancies_url':el['vacancies_url'],
                    'open_vacancies':el['open_vacancies'],
                })
    return comp_list

@staticmethod
def get_company_vacancies(companies_list=[]):
    vacs_list = []
    for company in companies_list:
        vacancies_url = company['vacancies_url']
        response = requests.get(vacancies_url)
        if response.status_code != 200:
            print(f'Ошибка {response.status_code}')
        else:
            vacs = response.json()['items']
            for el in vacs:
                vacs_list.append(el)
    return vacs_list