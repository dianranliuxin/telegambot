pip install python-telegram-bot --upgrade
import telegram<font></font>
<font></font>
# 替换为实际的 token<font></font>
bot = telegram.Bot(token='012345678:xxxxxxxxxxxxxxxxx-xxxxxxxxxx-xxxxxx')
bot.send_message(chat_id='@XXXXXX', text="新消息")
bot.send_message(chat_id='@XXXXXX', text='<a href="http://slowread.net/monitor-hostloc/">HOSTLOC 交易贴提醒</a>.', parse_mode=telegram.ParseMode.HTML)
bot.send_message(chat_id='@XXXXXX', text='<a href="'%20+%20href%20+%20'">' + title + '</a>.', parse_mode=telegram.ParseMode.HTML, disable_web_page_preview=True)
bot.send_message(chat_id=chat_id, text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.', parse_mode=telegram.ParseMode.HTML)
bot.send_photo(chat_id=chat_id,photo='<https://telegram.org/img/t_logo.png')
bot.sendPhoto(chat_id="_your channel name here... example: @Linuxgram", photo="<https://telegram.org/img/t_logo.png", caption="Sample photo")
