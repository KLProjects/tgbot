from typing import Optional, List

from telegram import Message, Update, Bot, User
from telegram import MessageEntity
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.warns import warn


MAX_CHARS_PER_MESSAGE = "200"


@run_async
def warn_if_exceed(bot: Bot, update: Update):
    short_name = "Created By @MidukkiBot"
    msg = update.effective_message # type: Optional[Message]
    chat = update.effective_chat # type: Optional[Chat]
    if len(msg.text) > MAX_CHARS_PER_MESSAGE:
        return warn(msg.from_user, chat, "Exceeded SET character limit", msg)


def warn_if_not_photo(bot: Bot, update: Update):
    short_name = "Created By @MidukkiBot"
    msg = update.effective_message # type: Optional[Message]
    msg.reply_text("Please send as file.")


__help__ = "no one gonna help you"
__mod_name__ = "exceed cl"

dispatcher.add_handler(MessageHandler(Filters.text & Filters.group, warn_if_exceed))
dispatcher.add_handler(MessageHandler(Filters.photo & Filters.group, warn_if_not_photo))
