import telebot
import re
from copy import copy
import random
from threading import Thread
import requests
import urllib.request
import time
from datetime import datetime
from datetime import date
from datetime import time as tm
import time as sleep
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import docx
from docx import Document
from docx.shared import Inches
import shutil
from docxtpl import DocxTemplate
from bs4 import BeautifulSoup as bs
import dateutil
from openpyxl import load_workbook
from urllib.request import urlretrieve
from shutil import  make_archive
import os


token = "1285037918:AAFThCZD8y9r-hGvmO0NkOGwrhA_EAsaUx0"
bot = telebot.TeleBot(token)