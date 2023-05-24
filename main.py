import vk_api
import json
import utils
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from models import User
from config import *
from datetime import datetime

class MyLongPoll(VkBotLongPoll):
    def listen(self):
        while True:
            try:
                for event in self.check():
                    yield event
            except Exception as e:
                print(e)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }




class VkBot:
    def __init__(self):
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = MyLongPoll(self.vk_session, 218350278)

    try:
        def run(self):
            def send_message (user_id, message, keybord=None):
                post = {
                    "user_id": user_id,
                    "message": message,
                    "random_id": 0,
                }
                if keybord != None:
                    post["keyboard"] = keybord.get_keyboard()
                self.vk_session.method("messages.send", post)

            def vse (text, strp):
                file13 = open('GrupName.txt', 'r', encoding='utf=8')
                lines = file13.readlines()
                file13.close()
                st = 0
                p = 0
                kurs = current_datetime.year - 2000
                if current_datetime.month >= 9:
                    kurs = kurs + 1
                for r in range(len(lines)):
                    gruppa = lines[r].split(' ')
                    if strp in gruppa[0]:
                        if int(gruppa[1]) != 0:
                            fl = 0
                            if kurs - int(gruppa[0][:2])<=4 and strp == 'бо':
                                fl=1
                            if kurs - int(gruppa[0][:2])<=2 and strp == 'мо':
                                fl=1
                            if kurs - int(gruppa[0][:2])<=5 and strp == 'бз':
                                fl=1
                            if fl == 1:
                                self.vk_session.method('messages.send', {
                                    'chat_id': int(gruppa[1]),
                                    'message': f'{text}',
                                    'random_id': 0
                                })

            def vsekurs (text, nup, nom):
                file13 = open('GrupName.txt', 'r', encoding='utf=8')
                lines = file13.readlines()
                file13.close()
                st = 0
                p = 0
                kurs = current_datetime.year - 2000
                if current_datetime.month >= 9:
                    kurs = kurs + 1
                for r in range(len(lines)):
                    gruppa = lines[r].split(' ')
                    if kurs - int(gruppa[0][:2]) == nom and nup in gruppa[0]:
                        if int(gruppa[1]) != 0:
                            self.vk_session.method('messages.send', {
                                'chat_id': int(gruppa[1]),
                                'message': f'{text}',
                                'random_id': 0
                            })

            def kurs (text1, nup, nom):
                file13 = open('GrupName.txt', 'r', encoding='utf=8')
                lines = file13.readlines()
                file13.close()
                keybord = VkKeyboard()
                keybord.add_button(text1 + " всем", VkKeyboardColor.POSITIVE)
                keybord.add_line()
                st = 0
                p = 0
                kurs = current_datetime.year - 2000
                if current_datetime.month >= 9:
                    kurs = kurs + 1
                for r in range(len(lines)):
                    gruppa = lines[r].split(' ')
                    if kurs - int(gruppa[0][:2]) == nom and nup in gruppa[0]:
                        if int(gruppa[1]) != 0:
                            if st == 4:
                                keybord.add_line()
                                st = 0
                            keybord.add_button(gruppa[0], VkKeyboardColor.POSITIVE)
                            p = p + 1
                            st = st + 1
                if p != 0:
                    keybord.add_line()
                keybord.add_button("Назад", VkKeyboardColor.NEGATIVE)
                send_message(user_id, text1, keybord)

            flag = 0
            flag1 = 0
            flag2 = 0
            Belspis=0
            flaging = ''
            strp = ''
            kursz=['', '0']
            current_datetime = datetime.now()
            file2= open('StarostID.txt', 'r', encoding='utf=8')
            starostid = file2.readlines()
            strstarostid = ''
            for t in range(len(starostid)):
                strstarostid = strstarostid + starostid[t] + ' '
            file2.close()
            for event in self.longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    msg = event.object.message
                    user_id = msg['from_id']
                    user = utils.get_user_by_id(user_id)
                    text = msg['text']
                    fwd = self.vk_session.method('messages.getByConversationMessageId', {
                        'conversation_message_ids': msg['conversation_message_id'],
                        'peer_id': msg['peer_id']
                    })['items'][0]
                    # keybord = VkKeyboard()
                    # keybord.add_button("Всем", VkKeyboardColor.PRIMARY)
                    # keybord.add_line()
                    # st=0
                    # for f in range(10):
                    #     if st==4:
                    #         keybord.add_line()
                    #         st=0
                    #     keybord.add_button(str(f), VkKeyboardColor.PRIMARY)
                    #     st=st+1
                    # keybord.add_line()
                    # keybord.add_button("Назад", VkKeyboardColor.PRIMARY)
                    # send_message(user_id, "1", keybord)
                    keyboard = {
                        "one_time": False,
                        "buttons": [
                            [get_but('Написать бакалавриату', 'positive'), get_but('Написать магистратуре', 'positive')],
                            [get_but('Написать заочной форме', 'positive'), get_but('Другое', 'positive')]
                        ]
                    }
                    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
                    keyboard = str(keyboard.decode('utf-8'))
                    keyboard1 = {
                        "one_time": False,
                        "buttons": [
                            [get_but('Всем группам бакалавриата', 'primary')],
                            [get_but('1 курс', 'positive'), get_but('2 курс', 'positive')],
                            [get_but('3 курс', 'positive'), get_but('4 курс', 'positive')],
                            [get_but('Назад', 'negative')]
                        ]
                    }
                    keyboard1 = json.dumps(keyboard1, ensure_ascii=False).encode('utf-8')
                    keyboard1 = str(keyboard1.decode('utf-8'))
                    keyboard3 = {
                        "one_time": False,
                        "buttons": [
                            [get_but('Всем группам магистратуры', 'primary')],
                            [get_but('1 курсм', 'positive'), get_but('2 курсм', 'positive')],
                            [get_but('Назад', 'negative')]
                        ]
                    }
                    keyboard3 = json.dumps(keyboard3, ensure_ascii=False).encode('utf-8')
                    keyboard3 = str(keyboard3.decode('utf-8'))
                    keyboard4 = {
                        "one_time": False,
                        "buttons": [
                            [get_but('Всем группам заочной формы', 'primary')],
                            [get_but('1 курсз', 'positive'), get_but('2 курсз', 'positive'), get_but('3 курсз', 'positive'),],
                            [get_but('4 курсз', 'positive'), get_but('5 курсз', 'positive')],
                            [get_but('Назад', 'negative')]
                        ]
                    }
                    keyboard4 = json.dumps(keyboard4, ensure_ascii=False).encode('utf-8')
                    keyboard4 = str(keyboard4.decode('utf-8'))

                    keyboard5 = {
                        "one_time": False,
                        "buttons": [
                            [get_but('Стоп', 'negative')]
                        ]
                    }
                    keyboard5 = json.dumps(keyboard5, ensure_ascii=False).encode('utf-8')
                    keyboard5 = str(keyboard5.decode('utf-8'))

                    keyboard6 = {
                        "one_time": False,
                        "buttons": [
                            [get_but('Добавить группу', 'positive')],
                            [get_but('Добавить старосту', 'positive')],
                            [get_but('Добавить в белый список', 'positive')],
                            [get_but('Назад', 'negative')]
                        ]
                    }
                    keyboard6 = json.dumps(keyboard6, ensure_ascii=False).encode('utf-8')
                    keyboard6 = str(keyboard6.decode('utf-8'))

                    if user_id == msg['peer_id'] and user_id == admin_id:
                        print(user_id, text, fwd)
                        text1 = text.lower()
                        file13 = open('GrupName.txt', 'r', encoding='utf=8')
                        lines = file13.readlines()
                        file13.close()
                        if text1 == 'написать бакалавриату':
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Написать бакалавариату:',
                                'random_id': 0,
                                'keyboard': keyboard1
                            })
                        if text1 == 'написать магистратуре':
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Написать магистратуре:',
                                'random_id': 0,
                                'keyboard': keyboard3
                            })
                        if text1 == 'написать заочной форме':
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Написать заочной форме:',
                                'random_id': 0,
                                'keyboard': keyboard4
                            })
                        if text1 == 'старт' or text1=='start':
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Добрый день',
                                'random_id': 0,
                                'keyboard': keyboard
                            })
                        if text1 == 'другое':
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Другое',
                                'random_id': 0,
                                'keyboard': keyboard6
                            })
                        if text1 == '1 курс':
                            kurs(text1, 'бо', 1)
                        if text1 == '2 курс':
                            kurs(text1, 'бо', 2)
                        if text1 == '3 курс':
                            kurs(text1, 'бо', 3)
                        if text1 == '4 курс':
                            kurs(text1, 'бо', 4)
                        if text1 == '1 курсм':
                            kurs(text1, 'мо', 1)
                        if text1 == '2 курсм':
                            kurs(text1, 'мо', 2)
                        if text1 == '1 курсз':
                            kurs(text1, 'бз', 1)
                        if text1 == '2 курсз':
                            kurs(text1, 'бз', 2)
                        if text1 == '3 курсз':
                            kurs(text1, 'бз', 3)
                        if text1 == '4 курсз':
                            kurs(text1, 'бз', 4)
                        if text1 == '5 курсз':
                            kurs(text1, 'бз', 5)

                        if kursz[0] != '':
                            vsekurs(text, kursz[0], int(kursz[1]))
                            kursz = ['', '']

                        if text1 == '1 курс всем':
                            kursz = ['бо', '1']
                        if text1 == '2 курс всем':
                            kursz = ['бо', '2']
                        if text1 == '3 курс всем':
                            kursz = ['бо', '3']
                        if text1 == '4 курс всем':
                            kursz = ['бо', '4']
                        if text1 == '1 курсм всем':
                            kursz = ['мо', '1']
                        if text1 == '2 курсм всем':
                            kursz = [ 'мо', '2']
                        if text1 == '1 курсз всем':
                            kursz = [ 'бз', '1']
                        if text1 == '2 курсз всем':
                            kursz = [ 'бз', '2']
                        if text1 == '3 курсз всем':
                            kursz = [ 'бз', '3']
                        if text1 == '4 курсз всем':
                            kursz = [ 'бз', '4']
                        if text1 == '5 курсз всем':
                            kursz = [ 'бз', '5']


                        if strp != '':
                            vse(text, strp)
                            strp = ''
                            send_message(user_id, "Сообщение отправленно")

                        if text1 == 'всем группам бакалавриата':
                            strp = 'бо'
                            send_message(user_id, "Вводите сообщение:")

                        if text1 == 'всем группам магистратуры':
                            strp = 'мо'
                            send_message(user_id, "Вводите сообщение:")

                        if text1 == 'всем группам заочной формы':
                            strp = 'бз'
                            send_message(user_id, "Вводите сообщение:")

                        if text1 == 'назад':
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Назад',
                                'random_id': 0,
                                'keyboard': keyboard
                            })

                        if text1 == 'стоп':
                            flag = 0
                            flag1 = 0
                            flag2 = 0
                            file2 = open('StarostID.txt', 'r', encoding='utf=8')
                            starostid = file2.readlines()
                            strstarostid = ''
                            for t in range(len(starostid)):
                                strstarostid = strstarostid + starostid[t] + ' '
                            file2.close()
                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Вы остановили редактирование.',
                                'random_id': 0,
                                'keyboard': keyboard
                            })


                        if flag1 == 1:
                            arraytext = text1.split(' ')
                            for t in range(len(arraytext)):
                                if arraytext[t].isnumeric():
                                    file1 = open('StarostID.txt', 'r', encoding='utf=8')
                                    if arraytext[t] in file1.read():
                                        self.vk_session.method('messages.send', {
                                            'user_id': user_id,
                                            'message': f'Пользователь {arraytext[t]}, уже добавлен.',
                                            'random_id': 0
                                        })
                                    else:
                                        file = open('StarostID.txt', 'a', encoding='utf=8')
                                        file.write(f'{arraytext[t]}\n')
                                        file.close()

                                        self.vk_session.method('messages.send', {
                                            'user_id': user_id,
                                            'message': f'Пользователь {arraytext[t]}, добавлен в список старост.',
                                            'random_id': 0
                                        })
                                    file1.close()
                                else:
                                    self.vk_session.method('messages.send', {
                                        'user_id': user_id,
                                        'message': f'Вы ввели недопустимые символы',
                                        'random_id': 0
                                    })

                        if text1 == 'добавить старосту':
                            flag1 = 1

                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Вы начали редактировать список старост.',
                                'random_id': 0,
                                'keyboard': keyboard5
                            })

                        # if text1 == 'cписок групп':
                        #     stringp='Список групп:'
                        #     for t in range(len(lines)):
                        #         vert = lines[t].split(' ')
                        #         if 'год' in vert[0] or 'Заочная' in vert[0]:
                        #             self.vk_session.method('messages.send', {
                        #                 'user_id': user_id,
                        #                 'message': f'{stringp}',
                        #                 'random_id': 0
                        #             })
                        #             if '_год' in vert[0]:
                        #                 god=vert[0][:2]
                        #                 print(god)
                        #                 kurs=current_datetime.year - int(god) - 2000
                        #                 print(god)
                        #                 if current_datetime.month >= 9 :
                        #                     kurs= kurs + 1
                        #                 stringp=str(kurs) + ' курс' + '\n'
                        #             if 'Заочная' in vert[0]:
                        #                 stringp= 'Заочная форма обучения' + '\n'
                        #         else:
                        #             stringp = stringp + '\n' + vert[0]

                        if (len(flaging)!=0):
                            grupp = flaging.split()
                            for t in range(len(grupp)):
                                self.vk_session.method('messages.send', {
                                    'chat_id': grupp[t],
                                    'message': f'{text}',
                                    'random_id': 0
                                })
                            send_message(user_id, "Сообщение отправленно")
                            flaging = ''

                        grupnaz = ''
                        if flag2 == 0:
                            for t in range(len(lines)):
                                vert = lines[t].split(' ')
                                if vert[0].lower() in text.lower() and int(vert[1]) != 0:
                                    flaging =flaging + ' '+ vert[1]
                                    grupnaz = grupnaz + ' ' + vert[0]
                            if flaging != '':
                                send_message(user_id,"Вводите сообщение для:\n" + grupnaz)

                        if flag2 == 1:
                            arraytext = text.split(' ')
                            for t in range(len(arraytext)):
                                file1 = open('GrupName.txt', 'r', encoding='utf=8')
                                if arraytext[t].lower() in file1.read().lower():
                                    self.vk_session.method('messages.send', {
                                        'user_id': user_id,
                                        'message': f'Группа {arraytext[t]}, уже добавлена.',
                                        'random_id': 0
                                    })
                                else:
                                    file = open('GrupName.txt', 'a', encoding='utf=8')
                                    file.write(f'\n{arraytext[t]} 0')
                                    file.close()

                                    self.vk_session.method('messages.send', {
                                        'user_id': user_id,
                                        'message': f'Группа {arraytext[t]}, добавлен в список групп.',
                                        'random_id': 0
                                    })
                                file1.close()


                        if text1 == 'добавить группу' or text1 == 'добавить группы':
                            flag2 = 1

                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Вы начали добавлять в список групп.',
                                'random_id': 0,
                                'keyboard': keyboard5
                            })

                        if flag == 1:
                            arraytext = text1.split(' ')
                            for t in range(len(arraytext)):
                                if arraytext[t].isnumeric():
                                    file1 = open('List.txt', 'r', encoding='utf=8')
                                    if arraytext[t] in file1.read():
                                        self.vk_session.method('messages.send', {
                                            'user_id': user_id,
                                            'message': f'Пользователь {arraytext[t]}, уже добавлен.',
                                            'random_id': 0
                                        })
                                    else:
                                        file = open('List.txt', 'a', encoding='utf=8')
                                        file.write(f'{arraytext[t]}\n')
                                        file.close()

                                        self.vk_session.method('messages.send', {
                                            'user_id': user_id,
                                            'message': f'Пользователь {arraytext[t]}, добавлен в белый список.',
                                            'random_id': 0
                                        })
                                    file1.close()
                                else:
                                    self.vk_session.method('messages.send', {
                                        'user_id': user_id,
                                        'message': f'Вы ввели недопустимые символы',
                                        'random_id': 0
                                    })

                        if text1 == 'добавить в белый список':
                            flag = 1

                            self.vk_session.method('messages.send', {
                                'user_id': user_id,
                                'message': f'Вы начали редактировать белый список.',
                                'random_id': 0,
                                'keyboard': keyboard5
                            })
                    else:
                        file = open('ChatLog.txt', 'a', encoding='utf=8')
                        file.write(f'ID={user_id} ,text={text} ,{fwd}\n')
                        file.close()

                        print (user_id, text, fwd)




                        if Belspis == 1:
                            file1 = open('List.txt', 'r', encoding='utf=8')
                            if str(user_id) in file1.read():
                                print ('Пользователь прошел проверку на белый список')
                            else:
                                self.vk_session.method('messages.removeChatUser', {
                                    'user_id': user_id,
                                    'chat_id': msg['peer_id'] - 2000000000
                                })
                                self.vk_session.method('messages.send', {
                                    'chat_id': msg['peer_id'] - 2000000000,
                                    'message': f'Пользователь не входит в белый список.',
                                    'random_id': 0
                                })
                            file1.close()

                        if 'reply_message' in fwd:
                            fwd = fwd['reply_message']
                        else:
                            fwd = None
                        print(strstarostid)
                        print(user.vk_id)

                        if str(user.vk_id) in strstarostid:
                            text1 = text.lower()
                            if 'группа' in text1:
                                flagper = 0
                                file13 = open('GrupName.txt', 'r', encoding='utf=8')
                                lines = file13.readlines()
                                file13.close()
                                for t in range(len(lines)):
                                    vert = lines[t].split(' ')
                                    if text1[-9:] in vert[0].lower():
                                        if vert[1] != 0:
                                            print('3')
                                            vert[1] = str(msg['peer_id'] - 2000000000)
                                            lines[t] = vert[0] +' '+ vert[1] +'\n'
                                            print(vert)
                                            print(lines[t])
                                            file15 = open('GrupName.txt', 'w', encoding='utf=8')
                                            for r in range(len(lines)):
                                                file15.write(f'{lines[r]}')
                                            file15.close()
                                            self.vk_session.method('messages.send', {
                                                'chat_id': msg['peer_id'] - 2000000000,
                                                'message': f'Ваша беседа добавленна',
                                                'random_id': 0
                                            })
                                            flagper =1
                                        else:
                                            self.vk_session.method('messages.send', {
                                                'chat_id': msg['peer_id'] - 2000000000,
                                                'message': f'Такая группа уже добавленна.',
                                                'random_id': 0
                                            })
                                if flagper == 0:
                                    self.vk_session.method('messages.send', {
                                        'chat_id': msg['peer_id'] - 2000000000,
                                        'message': f'Вы не коректно указали группу \n Пример: \n Группа: 20-NNбо-1',
                                        'random_id': 0
                                    })

                        if user.vk_id == admin_id:
                            text1 = text.lower()

                            if text1 == 'выключить белый список':
                                Belspis = 0
                                self.vk_session.method('messages.send', {
                                    'chat_id': msg['peer_id'] - 2000000000,
                                    'message': f'Вы выключили белый список',
                                    'random_id': 0
                                })

                            if text1 == 'включить белый список':
                                Belspis = 1
                                self.vk_session.method('messages.send', {
                                    'chat_id': msg['peer_id'] - 2000000000,
                                    'message': f'Вы включили белый список',
                                    'random_id': 0
                                })

                            if text1 == 'стоп':

                                flag = 0

                                self.vk_session.method('messages.send', {
                                    'chat_id': msg['peer_id'] - 2000000000,
                                    'message': f'Вы остановили редактирование белого списка.',
                                    'random_id': 0
                                })

                            if flag == 1:
                                arraytext = text.split(' ')
                                for t in range(len(arraytext)):
                                    if arraytext[t].isnumeric():
                                        file1 = open('List.txt', 'r', encoding='utf=8')
                                        if text in file1.read():
                                            self.vk_session.method('messages.send', {
                                                'chat_id': msg['peer_id'] - 2000000000,
                                                'message': f'Пользователь {arraytext[t]}, уже добавлен.',
                                                'random_id': 0
                                            })
                                        else:
                                            file = open('List.txt', 'a', encoding='utf=8')
                                            file.write(f'{arraytext[t]}\n')
                                            file.close()

                                            self.vk_session.method('messages.send', {
                                                'chat_id': msg['peer_id'] - 2000000000,
                                                'message': f'Пользователь {arraytext[t]}, добавлен в белый список.',
                                                'random_id': 0
                                            })
                                        file1.close()
                                    else:
                                        self.vk_session.method('messages.send', {
                                            'chat_id': msg['peer_id'] - 2000000000,
                                            'message': f'Вы ввели недопустимые символы',
                                            'random_id': 0
                                        })

                            if text1 == 'добавить':
                                flag = 1

                                self.vk_session.method('messages.send', {
                                    'chat_id': msg['peer_id'] - 2000000000,
                                    'message': f'Вы начали редактировать белый список.',
                                    'random_id': 0
                                })

                            if 'обнулить' in text1:
                                arraytext = text1.split(' ')
                                for t in range(len(arraytext)):
                                    if arraytext[t].isnumeric():
                                        fwd_user = utils.get_user_by_id(arraytext[t])
                                        fwd_user.warns = 0
                                        fwd_user.save()

                                        user_name = self.vk_session.method('users.get', {'user_id': fwd_user.vk_id})[0]['first_name']
                                        self.vk_session.method('messages.send', {
                                            'chat_id': msg['peer_id'] - 2000000000,
                                            'message': f'{user_name}, с вас сняты все предупреждения!\nВсего предупреждений: {fwd_user.warns}/5',
                                            'random_id': 0
                                        })


                            if fwd:
                                print(fwd['conversation_message_id'])
                                if text1 == 'удалить':
                                    self.vk_session.method('messages.delete', {
                                        'cmids': fwd['conversation_message_id'],
                                        'delete_for_all': 1,
                                        'peer_id': msg['peer_id']
                                    })




                                if text1 == 'выгнать':
                                    self.vk_session.method('messages.removeChatUser', {
                                        'user_id': fwd['from_id'],
                                        'chat_id': msg['peer_id']-2000000000
                                    })
                                    self.vk_session.method('messages.delete', {
                                        'cmids': fwd['conversation_message_id'],
                                        'delete_for_all': 1,
                                        'peer_id': msg['peer_id']
                                    })

                                elif text1 == 'обнулить предупреждения':
                                    fwd_user = utils.get_user_by_id(fwd['from_id'])
                                    fwd_user.warns = 0
                                    fwd_user.save()

                                    user_name = self.vk_session.method('users.get', {'user_id': fwd_user.vk_id})[0][
                                        'first_name']

                                    self.vk_session.method('messages.send', {
                                        'chat_id': msg['peer_id'] - 2000000000,
                                        'message': f'{user_name}, с вас сняты все предупреждения!\nВсего предупреждений: {fwd_user.warns}/5',
                                        'random_id': 0
                                    })

                                elif text1 == 'предупреждение':
                                    fwd_user = utils.get_user_by_id(fwd['from_id'])
                                    fwd_user.warns += 1
                                    fwd_user.save()

                                    user_name = self.vk_session.method('users.get', {'user_id': fwd_user.vk_id})[0]['first_name']

                                    self.vk_session.method('messages.send', {
                                        'chat_id': msg['peer_id']-2000000000,
                                        'message': f'{user_name}, вам выдано предупреждение!\nВсего предупреждений: {fwd_user.warns}/5',
                                        'random_id': 0
                                    })

                                    if fwd_user.warns >= 5:
                                        self.vk_session.method('messages.removeChatUser', {
                                        'user_id': fwd_user.vk_id,
                                        'chat_id': msg['peer_id']-2000000000
                                    })
                                    self.vk_session.method('messages.delete', {
                                        'cmids': fwd['conversation_message_id'],
                                        'delete_for_all': 1,
                                        'peer_id': msg['peer_id']
                                    })
                        else:
                            file12 = open('Spam.txt', 'r', encoding='utf=8')
                            lines = file12.readlines()
                            for t in range(len(lines)):
                                if lines[t] in text:
                                    self.vk_session.method('messages.send', {
                                        'chat_id': msg['peer_id'] - 2000000000,
                                        'message': f'Пользователь написал слово из "спам" списка.',
                                        'random_id': 0
                                    })


                                    fwd_user = utils.get_user_by_id(user_id)
                                    fwd_user.warns += 1
                                    fwd_user.save()

                                    user_name = self.vk_session.method('users.get', {'user_id': fwd_user.vk_id})[0][
                                        'first_name']

                                    self.vk_session.method('messages.send', {
                                        'chat_id': msg['peer_id'] - 2000000000,
                                        'message': f'{user_name}, вам выдано предупреждение!\nВсего предупреждений: {fwd_user.warns}/5',
                                        'random_id': 0
                                    })

                                    if fwd_user.warns >= 5:
                                        self.vk_session.method('messages.removeChatUser', {
                                            'user_id': fwd_user.vk_id,
                                            'chat_id': msg['peer_id'] - 2000000000
                                        })

                                    self.vk_session.method('messages.delete', {
                                        'cmids': msg['conversation_message_id'],
                                        'delete_for_all': 1,
                                        'peer_id': msg['peer_id']
                                    })

                            file12.close()


    except Exception as e:
        print('Ошибка')


if __name__ == '__main__':
    VkBot().run()