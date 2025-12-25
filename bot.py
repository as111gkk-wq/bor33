import telebot
from telebot import types
import os

# جلب التوكن من إعدادات Render (البيانات المحفوضة)
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# أمر /start مع أزرار
@bot.message_handler(commands=['start'])
def welcome(message):
    # إنشاء لوحة أزرار
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # تعريف الأزرار
    btn1 = types.InlineKeyboardButton("قناتي على تلجرام", url="https://t.me/YourChannel")
    btn2 = types.InlineKeyboardButton("الدعم الفني", callback_data='support')
    btn3 = types.InlineKeyboardButton("حول البوت", callback_data='about')
    
    # إضافة الأزرار للوحة
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, f"مرحباً {message.from_user.first_name}! كيف يمكنني مساعدتك؟", reply_markup=markup)

# التعامل مع ضغطات الأزرار (Callback)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "support":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="تواصل مع المطور: @YourUsername")
    elif call.data == "about":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="هذا البوت تمت برمجته بلغة بايثون ويعمل على استضافة Render.")

# تشغيل البوت
if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.infinity_polling()
