from staticmetod import get_company, get_company_vacancies
from config import config
from src.utils import create_list_vacs, create_database, create_tables, save_to_table_vacs, save_to_table_comps, create_list_comps
def main():
    params = config()
    list_company = ['Тинькофф', 'Яндекс', 'Банк Открытие', 'ГК АГАТ', 'SOKOLOV', 'Арконт',
                    'Авиакомпания Победа', 'Аэрофлот', 'S7 Airlines', 'Автосалон CHERY']

    companies = get_company(list_company)
    vacancies = get_company_vacancies(companies)
    new_vacs = create_list_vacs(vacancies)
    new_comp = create_list_comps(companies)
    # create_database('hh2', params)
    create_tables('hh2', params)
    save_to_table_comps(new_comp, 'hh2', params)

    save_to_table_vacs(new_vacs, 'hh2', params)
    #print(new_vacs)

if __name__ == '__main__':
    main()


