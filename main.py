import requests
import asyncio
import logging
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.filters import CommandStart