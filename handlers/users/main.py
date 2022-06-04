from aiogram import types
import logging
from aiogram.dispatcher.filters.builtin import Command, CommandStart
from aiogram.types import message, reply_keyboard, user
from aiogram.types import CallbackQuery
from loader import dp, bot
from data.config import ADMINS

from asyncpg import Connection, Record
from asyncpg.exceptions import UniqueViolationError
#from utils.db_api.DBCommands import DBCommands
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from keyboards.default.topic import topicMenu
from keyboards.default.subtopic import subtopicDoc,subtopicCalendar
from keyboards.default.questionDoc import subtopic1Que

#from states.stateBot import FSMAdder




@dp.message_handler()
async def bot_message(message: types.Message):

    #Subtopics
    if message.text == "Подача документов":
        await message.answer(text= message.text, reply_markup=subtopicDoc)
    if message.text == "Календарь приема":
        await message.answer(text=message.text, reply_markup=subtopicCalendar)

    #Questions for 1 subtopic
    if message.text == "Как подать документы":
        await message.answer(text=message.text, reply_markup=subtopic1Que)
