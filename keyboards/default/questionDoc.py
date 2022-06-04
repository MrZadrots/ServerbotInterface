from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

subtopic1Que = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("До какого числа нужно подать документы")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы через сайт")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы лично")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы по почте")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как подать документы через Госуслуги")
subtopic1Que.add(b1)

b1 = KeyboardButton("Как изменить поданное заявление")
subtopic1Que.add(b1)
