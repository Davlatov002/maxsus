import telebot
import traceback
import time
from test1 import get_bnb_price
from test import generate_bsc_addresses
from main import generate_mnemonic_from_wordlist

# Telegram botni tokenini kiritish
TOKEN = "6698773907:AAFuir14I_PSE-jYN7-fvAD8PBLfQ5_wp84"
bot = telebot.TeleBot(TOKEN)

def habar():
    with open("list.txt", 'a') as f:
        bot.send_message(chat_id='1085840721', text=f"Botda ishga tushdi!!")
        try:
            while True:
            # for i in range(1):
                a = generate_mnemonic_from_wordlist()
                # a = 'word snow hope palace horn balcony rare bind salon denial forum mirror'
                print(a)
                b = generate_bsc_addresses(a)
                for i in b:
                    print(i)
                    # time.sleep(5)
                    try:
                        s = get_bnb_price(i)
                        if s != None:
                            if s > 0:
                                print(s)
                                d = f"{a} : {i} : {str(s)}"
                                f.write(d + "\n")
                                user_id = "1085840721"
                                bot.send_message(user_id, d)
                    except ConnectionError as e:
                        time.sleep(5)
                        print(f"Connection error: {e}")
        except Exception as e:
            print(f"Xatolik yuzaga keldi: {e}")
            print(traceback.format_exc())


# Bot yaratuvchisiga xabar yuborish
def send_message_to_bot_owner(exception_message):
    try:
        bot.send_message(chat_id='1085840721', text=f"Botda xatolik yuzaga keldi: {exception_message}")
    except Exception as e:
        print(f"Xatolik yuzaga keldi: {e}")

habar()
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        send_message_to_bot_owner(f"Bot ishlamay qoldi: {e}")
        print(f"Bot ishlamay qoldi: {e}")
        print(traceback.format_exc())
