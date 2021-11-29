from typing import List, Optional

from googletrans import Translator
from telegram import Bot, Message, MessageEntity, Update, User
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import LOGGER, dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler


@run_async
def do_translate(bot: Bot, update: Update, args: List[str]):
    short_name = "Created By @MidukkiBot 😬"
    msg = update.effective_message  # type: Optional[Message]
    lan = " ".join(args)
    to_translate_text = msg.reply_to_message.text
    translator = Translator()
    try:
        translated = translator.translate(to_translate_text, dest=lan)
        src_lang = translated.src
        translated_text = translated.text
        msg.reply_text(
            "Translated from {} to {}.\n {}".format(src_lang, lan, translated_text)
        )
    except exc:
        msg.reply_text(str(exc))


__help__ = """- /trn - as reply to a long message
"""
__mod_name__ = "Google Translate"

dispatcher.add_handler(DisableAbleCommandHandler("trn", do_translate, pass_args=True))
