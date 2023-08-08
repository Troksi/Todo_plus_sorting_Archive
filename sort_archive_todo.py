import re
from datetime import datetime, timedelta
def extract_info(text):
    match = re.search(r'@started\((\d{2}-\d{2}-\d{2} \d{2}:\d{2})\)', text)
    if match:
        timestamp = datetime.strptime(match.group(1), '%y-%m-%d %H:%M')

        return str(timestamp)
    else:
        match = re.search(r'@done\((\d{2}-\d{2}-\d{2} \d{2}:\d{2})\)', text)
        if match:
           timestamp = datetime.strptime(match.group(1), '%y-%m-%d %H:%M')
        
        return str(timestamp)
    return None

def custom_sort(strings):
    def extract_info(text):
        match = re.search(r'@started\((\d{2}-\d{2}-\d{2} \d{2}:\d{2})\)', text)
        if match:
            timestamp = datetime.strptime(match.group(1), '%y-%m-%d %H:%M')
            
            return str(timestamp)
        
        return None

    def extract_wasted(text):
        match = re.search(r'@wasted\((\d+)m(\d+)s\)', text)
        if match:
            minutes = int(match.group(1))
            seconds = int(match.group(2))
            return str(timedelta(minutes=minutes, seconds=seconds))
        return str(timedelta())

    def sort_key(item):
        timestamp = extract_info(item)
        return timestamp

    sorted_strings = sorted(strings, key=sort_key)
    return sorted_strings

# Example list of strings
string_list = [
    "[-] написать консольное меню и управление @started(23-07-26 17:13) @cancelled(23-07-26 18:00) @wasted(47m27s) @project(Website)",
    "[x] написать простой ввод из одностраничного сайтаcl @done(23-07-25 17:47) @project(Website) На Flask получилось. С React проблема. Хз, находит уязвимости->фиксю -> нахожу еще больше уязвимости и тд",
    "[x] создать api  yaml файл с помощью Swagger @done(23-07-31 00:20) @project(Website)"
]

# Call the function and print the sorted list
# sorted_list = custom_sort(string_list)
# for item in sorted_list:
#     print(item)

def extract_tasks(input_string):
    lines = input_string.split('\n')
    tasks = []
    current_task = None

    for line in lines:
        match = re.match(r'^\s*\[([-x])\]\s+(.*)$', line)
        if match:
            status = match.group(1)
            task_description = match.group(2)
            if current_task is not None:
                tasks.append(current_task)
            current_task = {'status': status, 'description': [task_description], 'timestamp': extract_info(task_description)}
        elif current_task is not None:
            current_task['description'].append(line.strip())
    
    if current_task is not None:
        tasks.append(current_task)

    return tasks

def parsing_archive(string_data):
    string_archive_data = string_data.split('Archive:\n')[1]
    string_list = extract_tasks(string_archive_data)
    
    return string_list

def debug_print(sorted_list_pars_text):
    for line in sorted_list_pars_text:
        print('Description: {} Time: {}'.format(line['description'][0][:20], line['timestamp']))

def realise_print(sorted_list_pars_text):
    for line in sorted_list_pars_text:
        print('  [{}] {}'.format(line['status'], line['description'][0]))
        if len(line['description'])>1:
            for item in line['description'][1:]:
                print('    {}'.format(item))

string_data = """Tasks:
    [] LSC-3	Configure a company table for the database
    [] LSC-4	Configure the scripts for adding or remove a profile.
    [] LSC-5	Configure the profile extraction scripts.
    [] LSC-6	Configure the profile update scripts.
    [] LSC-34	initial user registration and authorization
    [] LSC-35	displaying the profile card
    [] LSC-36	receiving and storing template
            
         

    


Website:
    [] написать консольное меню и управление_next
    [] обработать все эндпоинты
    [] НАписать странички на React

Docker:
    [] понять как настроить все окружение для react
    [] понять как связывать портам связь между PostgreSQL - Python - React
    [] разобратся CICD 
    [] настроить автотесты

    run:
        [] linkedinsalescopilotdesign\backend\tests>>> python -m unittest
    Linters:
        ignore: 
            [] E501 -из-за длины строк кода зачастую >79
            [] E402 из-за переопределения пути
        [] flake8
        [] autopep8

    environment:
        [] bs4
        [] selenium
        [] langchain
        [] openai
        [] psycopg2
        [] tiktoken
        [] qdrant-client
        [] lxml
        [] flask
        [] Chrome

Archive:
  [-] LSC-2	Configure the user table for the database @started(23-08-04 11:42) @cancelled(23-08-04 20:23) @wasted(8h41m34s) @project(Tasks)
  [x] составить ЕР диаграмму @done(23-07-25 11:11) @project(DB)
  [x] составить документацию UmlPlant @started(23-07-25 13:19) @done(23-07-25 14:21) @lasted(1h2m8s) @project(DB)
  [x] создать базу в PostgreSQL @started(23-07-25 14:21) @done(23-07-25 15:10) @lasted(49m59s) @project(DB)
  [x] исправить имена полей name на user_name @done(23-07-30 15:29) @project(DB)
  [x] исправить use_case на template @started(23-07-30 15:20) @done(23-07-30 15:30) @lasted(10m33s) @project(DB)
  [x] занести в словари данные @started(23-07-26 15:36) @done(23-07-26 17:11) @lasted(1h35m51s) @project(DB)
  [x] добавить таблицу тегов слов @done(23-07-30 22:12) @project(DB)
  [x] исправить таблицу skill_ownership, разделив id компании и пользователей @done(23-08-01 17:21) @project(DB)
  [x] исправить таблицу publication, разделив id компании и пользователей @done(23-08-02 16:20) @project(DB)
  [x] составить unittests @started(23-08-03 13:25) @done(23-08-03 21:03) @lasted(7h38m45s) @project(DB)
  [x] get_sale_profile @started(23-08-07 19:14) @done(23-08-07 19:44) @lasted(30m26s) @project(DB.sale_profile)
  [x] get_all_sale_profile @done(23-08-07 19:43) @project(DB.sale_profile)
  [x] delete_sale_profile @done(23-08-07 19:43) @project(DB.sale_profile)
  [x] новый пользователь @started(23-07-27 11:15) @done(23-07-27 16:12) @lasted(4h57m28s) @project(DB.составить запрос на внесения данных)
  [x] новых компаний @done(23-08-03 20:36) @project(DB.составить запрос на внесения данных)
  [x] новых клиентов @done(23-08-03 20:36) @project(DB.составить запрос на внесения данных)
  [x] новых шаблонов @done(23-08-03 02:56) @project(DB.составить запрос на внесения данных)
  [x] инициализация связи user-sales-company-useCase @done(23-07-28 01:44) @project(DB.составить запрос на внесения данных)
  [x] занести профаил клиента @done(23-08-03 20:36) @project(DB.составить запрос на внесения данных.профаил)
  [-] занести профаил компании @started(23-07-31 16:39) @cancelled(23-08-01 10:34) @wasted(17h55m51s) @project(DB.составить запрос на внесения данных.профаил)
  [x] занести профаил компании @done(23-08-03 20:37) @project(DB.составить запрос на внесения данных.профаил)
  [-] редактирование имя компании @started(23-07-27 17:01) @cancelled(23-07-28 01:42) @wasted(8h41m8s) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование имя компании @done(23-08-03 02:57) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование описание компании @done(23-08-03 02:56) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование клиента @done(23-08-03 20:40) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование имя шаблона @done(23-08-03 02:57) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование описания шаблона @done(23-08-03 02:57) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование тегов шаблона @done(23-08-03 02:57) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] редактирование шаблона @done(23-08-03 02:57) @project(DB.составить запрос на изменения данных.карточка компании)
  [x] удаление при ошибки регистрации @done(23-07-28 01:45) @project(DB.составить запрос на удаления данных)
  [x] удаление пользователя @done(23-08-03 20:43) @project(DB.составить запрос на удаления данных)
  [x] удаление клиента @done(23-08-03 20:43) @project(DB.составить запрос на удаления данных)
  [x] удаление шаблона @done(23-08-03 20:43) @project(DB.составить запрос на удаления данных)
  [x] удаление кампании @done(23-08-03 20:43) @project(DB.составить запрос на удаления данных)
  [x] авторизация @done(23-07-27 16:14) @project(DB.составить запрос на извлечении данных)
  [x] получить карточку компании @done(23-07-28 01:44) @project(DB.составить запрос на извлечении данных)
  [x] получить список шаблонов @done(23-08-03 03:00) @project(DB.составить запрос на извлечении данных)
  [x]  получение credentials пользователя @done(23-08-03 20:45) @project(DB.составить запрос на извлечении данных)
  [x] получить шаблон @done(23-08-03 20:45) @project(DB.составить запрос на извлечении данных)
  [x] получить компанию @done(23-08-03 20:45) @project(DB.составить запрос на извлечении данных)
  [x] получить клиента @done(23-08-03 20:45) @project(DB.составить запрос на извлечении данных)
  [x] авторизация @done(23-08-03 20:47) @project(DB.tests)
  [x] компании @done(23-08-03 20:47) @project(DB.tests)
  [x] клиентов @done(23-08-03 20:47) @project(DB.tests)
  [x] шаблонов @done(23-08-03 20:47) @project(DB.tests)
  [x] sales_profile @done(23-08-07 18:57) @project(DB.tests)
  [x] insert @started(23-08-07 19:45) @done(23-08-07 21:38) @lasted(1h53m4s) @project(DB.tests.sale_profile)
  [x] get_sale_profile @started(23-08-07 19:45) @done(23-08-07 21:38) @lasted(1h53m4s) @project(DB.tests.sale_profile)
  [x] get_all_sale_profile @started(23-08-07 19:45) @done(23-08-07 21:38) @lasted(1h53m4s) @project(DB.tests.sale_profile)
  [x] delete_sale_profile @started(23-08-07 19:45) @done(23-08-07 21:38) @lasted(1h53m4s) @project(DB.tests.sale_profile)
  [x] исправление таблиы sale_profile -> удаление поля template_id @done(23-08-07 18:59) @project(HatFix)
  [x] исправление таблиы template -> добавление поля template_id @done(23-08-07 19:00) @project(HatFix)
  [x] Исправление "from models.company import UserProfile" @done(23-08-07 19:01) @project(HatFix)
  [x] переименовать каталоги и почистить файлы @started(23-07-30 15:30) @done(23-07-31 00:19) @lasted(8h49m30s) @project(app)
  [x] решить проблему импорта файлов выше уровнем каталога @started(23-07-31 13:18) @done(23-07-31 16:13) @lasted(2h55m6s) @project(app)
    пришлось оставить костыль - импорт модуля не видит если сразу явно указывать.
    нужно sys.path. указать от какого католога нужно смотреть, в данном случае на родительский pardir каталог.
    '''
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    sys.path.append(parent_dir)
    '''
  [x] ревью на add user parser @started(23-08-01 12:32) @done(23-08-01 15:00) @lasted(2h28m31s) @project(app)
  [x] подключить api @started(23-07-26 12:23) @done(23-07-26 13:26) @lasted(1h3m37s) @project(Обработка ChatGPT)
  [-] получить ответ с возможностью отпарсить @started(23-07-26 14:34) @cancelled(23-07-26 15:36) @wasted(1h2m19s) @project(Обработка ChatGPT)
  [x] получить ответ с возможностью отпарсить_продолжение @done(23-08-03 03:00) @project(Обработка ChatGPT)
  [x] добавить promts для загрузки в базу @done(23-08-03 03:00) @project(Обработка ChatGPT)
  [-] запустить все выполнение программы с консоли @started(23-07-25 15:11) @cancelled(23-07-25 15:43) @wasted(32m16s) @project(Website)
  [x] запустить все выполнение программы с консоли_продолжение @done(23-07-25 18:12) @project(Website)
  [-] написать консольное меню и управление @started(23-07-26 17:13) @cancelled(23-07-26 18:00) @wasted(47m27s) @project(Website)
  [x] написать простой ввод из одностраничного сайтаcl @done(23-07-25 17:47) @project(Website)
    На Flask получилось. С Reackt проблема. Хз , находит уязвимости->фиксю -> нахожу еще больше уязвимости и тд
  [x] создать api  yaml файл с помощью Swagger @done(23-07-31 00:20) @project(Website)
  [x] прослушивать сайт @done(23-08-04 11:31) @project(Website)

"""
list_pars_text = parsing_archive(string_data)
#sorted_list_pars_text = sorted(list_pars_text, key=lambda x: datetime.strptime((x['timestamp']), '%Y-%m-%d %H:%M:%S')) # NOTE: тоже работает но слишком усложнено
sorted_list_pars_text = sorted(list_pars_text, key=lambda x: (x['timestamp']))

realise_print(sorted_list_pars_text)

#debug_print(sorted_list_pars_text)
