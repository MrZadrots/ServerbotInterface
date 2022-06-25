from aiogram import types
import logging
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import message, reply_keyboard, user
from aiogram.types import CallbackQuery
from loader import dp, bot
#from data.config import ADMINS

from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
#from utils.db_api.DBCommands import DBCommands
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
import final.answer
import final.data

from keyboards.default.topic import topicMenu
from keyboards.default.subtopic import subtopicDoc,subtopicCalendar, subtopicCategory, subtopicExams
from keyboards.default.questionDoc import subtopic1Que,subtopic2Que,subtopic3Que,subtopic4Que
from keyboards.default.questionCal import quesction1Cal,  quesction2Cal, quesction3Cal, quesction4Cal
from keyboards.default.questionsCat import quesction1Cat, quesction2Cat, quesction3Cat, quesction4Cat
from keyboards.default.questionExams import question1Exam, question2Exam, question3Exam
from keyboards.default.questionDir import question1Dir
from keyboards.default.questionChange import question1C
from keyboards.default.questionHome import question1Home


from utils.questionsList import questions
from utils.requests import req,getToken

Data = final.data.DATA()
route = []

@dp.message_handler()
async def bot_message(message: types.Message):
    global route
    #Subtopics
    if message.text == "Подача документов":
        msg = await message.answer(text=message.text, reply_markup=subtopicDoc)
        Data.set_part(1)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopicDoc)
        return
    if message.text == "Календарь приема":
        msg = await message.answer(text=message.text, reply_markup=subtopicCalendar)
        Data.set_part(2)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopicCalendar)
        return
    if message.text == "Особые категории":
        msg = await  message.answer(text=message.text, reply_markup=subtopicCategory)
        Data.set_part(3)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopicCategory)
        return
    if message.text == "Направление":
        msg = await message.answer(text=message.text, reply_markup=question1Dir)
        Data.set_part(4)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question1Dir)
        return
    if message.text == "Экзамены":
        msg = await message.answer(text=message.text, reply_markup=subtopicExams)
        Data.set_part(5)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopicExams)
        return
    if message.text == "Оценить шансы":
        msg = await message.answer(text=message.text, reply_markup=question1C)
        Data.set_part(6)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question1C)
        return
    if message.text == "Общежитие":
        msg = await message.answer(text=message.text, reply_markup=question1Home)
        Data.set_part(7)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question1Home)
        return

    #SUBTOPIC 1
    if message.text == "Как подать документы":
        msg = await message.answer(text=message.text, reply_markup=subtopic1Que)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopic1Que)
        return
    if message.text == "Необходимый перечень документов":
        msg = await message.answer(text=message.text, reply_markup=subtopic2Que)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopic2Que)
        return
    if message.text == "Заключить договор на обучение по контракту":
        msg = await message.answer(text=message.text, reply_markup=subtopic3Que)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(subtopic3Que)
        return

    if message.text == "Согласие":
        await message.answer(text=message.text, reply_markup=subtopic4Que)
        route.append(subtopic4Que)
        return

    #SUBTOPIC 2
    if message.text == "Основные даты":
        msg = await message.answer(text=message.text, reply_markup=quesction1Cal)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction1Cal)
        return
    if message.text == "Расписание вступительных испытаний":
        msg = await message.answer(text=message.text, reply_markup=quesction2Cal)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction2Cal)
        return
    if message.text == "Приказы о зачислении":
        msg = await message.answer(text=message.text, reply_markup=quesction3Cal)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction3Cal)
        return
    if message.text == "Заселение в общежитие":
        msg = await message.answer(text=message.text, reply_markup=quesction4Cal)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction4Cal)
        return
    #Subtopic 3
    if message.text == "Льготы":
         msg = await message.answer(text=message.text, reply_markup=quesction1Cat)
         await bot.delete_message(msg.chat.id, message.message_id)
         route.append(quesction1Cat)
         return
    if message.text == "Поступление БВИ":
        msg = await message.answer(text=message.text, reply_markup=quesction2Cat)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction2Cat)
        return
    if message.text == "Целевое обучение":
        msg = await message.answer(text=message.text, reply_markup=quesction3Cat)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction3Cat)
        return
    if message.text == "Индивидуальные достижения":
        msg = await message.answer(text=message.text, reply_markup=quesction4Cat)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(quesction4Cat)
        return
    #Subtopic 4
    if message.text == "Направления":
        msg = await message.answer(text=message.text, reply_markup=question1Dir)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question1Dir)
        return

    #Subtopic 5
    if message.text == "По ЕГЭ":
        msg = await message.answer(text=message.text, reply_markup=question1Exam)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question1Exam)
        return
    if message.text == 'Вступительные испытания':
        msg = await message.answer(text=message.text, reply_markup=question2Exam)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question2Exam)
        return
    if message.text == "Минимальные баллы":
        msg = await message.answer(text=message.text, reply_markup=question3Exam)
        await bot.delete_message(msg.chat.id, message.message_id)
        route.append(question3Exam)
        return
    if message.text == "Назад":
        if(len(route) == 0):
            msg = await message.answer(text="Назад", reply_markup=topicMenu)
        if(len(route) > 1):
            route.pop(len(route) - 1)
            msg = await message.answer(text="Назад", reply_markup=route[len(route) - 1])
        elif(len(route) == 1):
            route.pop(len(route) - 1)
            msg = await message.answer(text="Назад", reply_markup=topicMenu)
        await bot.delete_message(msg.chat.id, message.message_id)
        return


   


    if message.text in questions:
        logging.info(message.text)
        que = message.text + '?'

        token = getToken(message.from_user.id)
        logging.info(str(token))
        if str(token['msg']) == "Такого пользователя нет" or str(token['msg']) =="Ошибка":
            answer = req(que,'null')
            logging.info(answer[0]['answer'])
        else:
            logging.info("Зашли")
            answer = req(que, token['msg'])
            logging.info(answer[0]['answer'])
            


        await message.answer(text=answer[0]['answer'])
        #await message.answer(text="Я получил вопрос: " + que)
    else:
        token = getToken(message.from_user.id)
        answ = final.answer.get_answer(message.text, Data.get_part(), token) 
        # Отсылаем юзеру сообщение в его чат
        try:
            await message.answer(text=answ[0]['answer'])
        except:
            await message.answer("Я вас не понял, попробуйте переформулировать вопрос.")
        Data.set_part(-1)
