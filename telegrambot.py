import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler, MessageHandler, CallbackQueryHandler
from telegram.ext import Filters
from django_telegrambot.apps import DjangoTelegramBot
from strichcodebot.constants import *
from strichcodebot.commands import start, help
logger = logging.getLogger('django')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    dp = DjangoTelegramBot.getDispatcher('StrichcodeBot')
    commands = [start, help]
    for cmd in commands:
        name = cmd.command if hasattr(cmd, 'command') else cmd.__name__
        dp.add_handler(CommandHandler(name, cmd))
    dp.add_error_handler(error)
