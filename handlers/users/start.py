import logging
from loader import dp, bot
from aiogram import types
from keyboards.default.topic import topicMenu
from state.stateBot import FSMAdder
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from utils.requests import createToken,getToken

@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.answer(text="Вот, что ты можешь сделать",
                            reply_markup=topicMenu)



@dp.message_handler(text="/sendtoken")
async def cm_start(message: types.Message):
    await FSMAdder.token.set()
    user_name = message.from_user.full_name
    await bot.send_message(message.from_user.id,'Отправь мне свой токен из личного кабинета НГТУ')


@dp.message_handler(state=FSMAdder.token)
async def load_token(message = types.Message, state = FSMAdder.token):
    if str(message.text) != 'отмена' or str(message.text) != 'Отмена':
        logging.info(message.from_user)
        async with state.proxy() as data:
            data['tgId'] = message.from_user.id
            data['token'] = message.text
            logging.info(f'Data: {data}')
            logging.info(f'Message {message.from_user}')
        await state.finish()
        logging.info(data['token'])
        resultReq = createToken(data)
        logging.info(resultReq['msg'])

        if str(resultReq['msg']) == "Такой пользователь уже есть":
            await bot.send_message(message.from_user.id,"Вы уже отправляли токен. Повторная отправка невозможна.")
        elif str(resultReq['msg']) == "Пользователь добавлен":
            await bot.send_message(message.from_user.id,"Токен загружен")
        elif str(resultReq['msg']) == "Ошибка":
            await bot.send_message(message.from_user.id,"У нас произошла непредвиденная ошибка. Попробуй позже :)")
    else:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Отправка токена отменена')



@dp.message_handler(state="*",commands='отмена')
@dp.message_handler(Text(equals='отмена',ignore_case=True),state='*')
async def cancel_add_hanbler(message: types.Message,state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Отправка токена отменена')

