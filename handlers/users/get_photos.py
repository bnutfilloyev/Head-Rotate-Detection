from aiogram.types import Message, ContentType
import numpy as np
import cv2

from data.config import CHANEL
from utils.checker import image_main
from loader import dp, bot
from utils.detecor_mediapipe import detector

text_template = "<b>Result: </b>{}" \
                "\n\n" \
                "<b>Rotation Vector: </b>\n<code>{}</code>" \
                "\n\n" \
                "<b>Translation Vector: </b>\n<code>{}</code>"


# dlib detector
# @dp.message_handler(content_types=ContentType.PHOTO)
# async def get_photo(msg: Message):
#     photo = await msg.photo[-1].download("photos/{}.jpg".format(msg.photo[-1].file_id))
#     image = cv2.imread(photo.name)
#     result, pose, flag = image_main(image, image.shape[0], image.shape[1])
#     image = cv2.imencode(".jpg", result)[1].tobytes()
#     await msg.answer_photo(image, caption=text_template.format(flag, pose[0], pose[1]))
#     # await bot.send_photo(CHANEL, image, caption=text_template.format(flag, pose[0], pose[1]))
#     await msg.answer("<b>Rotation Vector Sum:</b>"
#                      "\n<code>{rotation}</code>"
#                      "\n\n<b>Translation Vector Sum:</b>"
#                      "\n<code>{translation}</code>".format(rotation=np.sum(pose[0]), translation=np.sum(pose[1])))


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo(msg: Message):
    photo = await msg.photo[-1].download("photos/{}.jpg".format(msg.photo[-1].file_id))
    result = detector(photo.name)
    if result is None:
        await msg.answer("Image is Valid!")
        return
    image = cv2.imencode(".jpg", result[0])[1].tobytes()
    await bot.send_photo(CHANEL, image, caption=result[-1])
    await msg.answer_photo(image, caption=result[-1])
