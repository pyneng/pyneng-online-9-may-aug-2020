import sys
from datetime import datetime, timedelta

try:
    from github import Github
except ModuleNotFoundError:
    print("Установите PyGithub: pip install PyGithub")

#### Укажите свой логин, пароль и имя репозитория:
#Имя пользователя GitHub:
username = ''
#Пароль пользователя на GitHub
password = ''
#Название репозитория. Например pyneng/online-3-natasha-samoylenko
repo_name = 'pyneng/'


error_message = '''
Скрипт надо вызывать с одним аргументом - текст сообщения в двойных кавычках

$ python submit_tasks.py "Сделал задания 3.1, 3.2, 3.3"
К последнему коммиту добавлен такой комментарий:
Сделал задания 3.1, 3.2, 3.3
'''


def post_comment_to_last_commit(msg, delta_days=14):
    '''
    msg - текст комментария
    delta_days - просматриваются коммиты только за последние delta_days дней
                 по умолчанию - 14 дней
    '''
    since = datetime.now() - timedelta(days=delta_days)

    g = Github(username, password)
    repo = g.get_repo(repo_name)

    commits = repo.get_commits(since=since)

    try:
        last = commits[0]
    except IndexError:
        print("За указанный период времени не найдено коммитов")
    else:
        last.create_comment(msg)
        print("К последнему коммиту добавлен такой комментарий:\n{}".format(msg))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        commit_comment = sys.argv[1]
        post_comment_to_last_commit(commit_comment)
    else:
        print(error_message)

