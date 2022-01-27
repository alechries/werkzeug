from pyrogram import filters, Client
from pyrogram.types import Message
from wzpyrogram.validations import is_url
import re


class Filters:
    is_url = filters.create(lambda _, dp, message: is_url(message.text), "WerkzeugIsURL")
