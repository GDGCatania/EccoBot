#!/usr/bin/python
import ConfigParser
import logging
import time as t
import mysql.connector as db
import telegram
import urllib2
import json
from datetime import timedelta, datetime

CONFIG_FILE = 'eccobot.cfg'
config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE)

LOG_FILE = config.get('log', 'name')
FORUM_URL = config.get('forum', 'url')
FORUM_FREQUENCY_S = config.get('forum', 'frequency_s')
DB_USER = config.get('db', 'user')
DB_PASSWORD = config.get('db', 'password')
DB_NAME = config.get('db', 'name')
TELEGRAM_TOKEN = config.get('telegram', 'token')
CHANNEL = config.get('telegram', 'channel')

# Enable logging
logging.basicConfig(filename=LOG_FILE,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
	level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Logger initialised')

logger.info('Initialise the DB connection')
#db_connection = db.connect(user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
#cursor = db_connection.cursor()

logger.info('Initialise the Telegram connection')
bot = telegram.Bot(token=TELEGRAM_TOKEN)

def message(message):
	"""Send an update to the chat"""
	bot.sendMessage(chat_id=CHANNEL, text=message, 
		parse_mode=telegram.ParseMode.MARKDOWN)

def getPostTime(post):
	time = post['relativeTime']
	time = time[0:10] + ' ' + time[11:19]
	time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
	return time

while True:
	check_time = datetime.now()
	response = urllib2.urlopen(FORUM_URL + '/api/recent/posts')
	
	posts = json.load(response)   
	
	for post in posts:
		title = post['topic']['title']
		url = FORUM_URL + '/topic/' + post['topic']['slug']
		time = getPostTime(post)

		# Subtracting one hour because running this in the UK. 
		# TODO: get time zone from timestamp
		if (check_time - time).total_seconds() - 3600 < float(FORUM_FREQUENCY_S) :
			message('Ciao! *Ecco* un nuovo post sul forum\n: *' + title + 
				'* at this link: ' + url)

	logger.info('I am going to sleep for a bit. Bye!')
	t.sleep(float(FORUM_FREQUENCY_S))
	logger.info('Waking up')
