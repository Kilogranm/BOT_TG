from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Чето")],
    [KeyboardButton(text="УРА"), KeyboardButton(text="ВОТ что это")]
],
    resize_keyboard=True

)

search_photo = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Поиск фото")]
],
    resize_keyboard=True

)


value = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="10"), KeyboardButton(text="20")],
    [KeyboardButton(text="50"), KeyboardButton(text="90")]
],
    input_field_placeholder="Введите количество или выберите(не больше 99)"

)
