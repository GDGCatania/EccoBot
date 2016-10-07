# EccoBot
This bot periodically crawls a NodeBB forum and sends new posts to a specified telegram group

Why that strange name? Because when you see a new post, you will say: "ecco!" Thus, **EccoBot**. 


## Config file

File: `eccobot.cfg`

```
[forum]
url = http://forum.gdgcatania.org
frequency_s = 3600
categories = 

[db]
name = 
user = 
password = 

[telegram]
token = # Ask @BotFather
# How to get the chat-id
# Add the bot to a chat
# Visit the link below
# https://api.telegram.org/bot<TOKEN>/getUpdates
# Use relevant id from chat
channel = 

[log]
name = bot.log
```

Useful docs/links:

http://forum.gdgcatania.org/api/recent/posts

https://github.com/NodeBB/NodeBB/blob/72c75bd7813b2bb41dc175ce6f7fe9fa58eed006/src/routes/api.js

## TODO

- Read configuration from file
  - ~forum to crawl~
  - categories to watch
  - db config
  - ~telegram channel to use~
- Crawler
