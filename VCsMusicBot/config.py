import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBiX2nj0WQ16urTdIoH9P0PcGftE6-DxsQpo22SPA-Tp22IPoATP6e83-Bollrh-VQQ4_gYfbbCpbI9AShZBM2OYoGvk-BCb0BwfnKsfIh1KMDaKd1MfppPOpIOUOZdO7KhiMpTrjc0qSM5Oybab2b_6MKMlJiXcGxDtNgRPumbZMFhwFMHagpK3TT79ISgH2y6gFcsdN6FPGd2KZ5crI-UjuvietVs3oHgwA8TwQX8rxWhU5GZU0LPLdPnuFvM-g8ZIjde38_2nbGZ-rT17h4ycXBDyTjRiBUBIVcd16wUozOsBt8KrWoAHRkgoT3unzR0dKXsv48GIA_OFqu0apNL3wA")
BOT_TOKEN = getenv("2118460714:AAHtk_nY6_4vq9Jnb3idtHAJ9VFu5_M7KtM")
BOT_NAME = getenv("@SVF_Music_Bot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/365e62866066531729897.jpg")
admins = {}
API_ID = int(getenv("5367954", ""))
API_HASH = getenv("f2e9b124aa5d365cc86658f8b77899a3")
BOT_USERNAME = getenv("@SVF_Music_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "")
PROJECT_NAME = getenv("PROJECT_NAME", "VCMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
ARQ_API_KEY = getenv("YRTQUQ-AQAMES-TWVYHO-IAQUTZ-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
