import aiogram
from aiogram.types import Message, ContentType
from aiogram.dispatcher import FSMContext

import cv2

from data.config import CHANEL
from utils.checker import image_main
from loader import dp, bot

text_template = "<b>Result: </b>{}" \
                "\n\n" \
                "<b>Rotation Vector: </b>\n<code>{}</code>" \
                "\n\n" \
                "<b>Translation Vector: </b>\n<code>{}</code>" \


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo(msg: Message):
    photo = await msg.photo[-1].download("photos/{}.jpg".format(msg.photo[-1].file_id))
    image = cv2.imread(photo.name)
    result, pose, flag = image_main(image, image.shape[0], image.shape[1])
    image = cv2.imencode(".jpg", result)[1].tobytes()
    await msg.answer_photo(image, caption=text_template.format(flag, pose[0], pose[1]))
    await bot.send_photo(CHANEL, image, caption=text_template.format(flag, pose[0], pose[1]))
