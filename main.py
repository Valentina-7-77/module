# Рассылка писем
# (Способы вызова функции)
def send_email(massege, recepient, *, sender = 'university.help@gmail.com'):
    # Проверяем условие:
    # "Если строки recipient и sender не содержит "@" или не оканчиваются на ".com"/".ru"/".net",
    # то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    if '@' not in recepient or not recepient.endswith(('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print('Невозможно отправить письмо с адреса', 'sender', 'на адрес', 'recepient')
    # Проверяем следующее условие:
    # "Если же sender и recipient совпадают, то вывести сообщение: "Нельзя отправить письмо самому себе!"
    if sender == recepient:
        print('Нельзя отправить письмо самому себе!')
    # Проверяем условие:
    # "Если же отправитель по умолчанию - university.help@gmail.com,
    # то вывести сообщение: "Письмо успешно отправлено с адреса sender на адрес recipient".
    elif sender != 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', str(sender), 'на адрес', str(recepient))

send_email('message', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender ='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
