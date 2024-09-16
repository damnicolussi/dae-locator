import os
from dotenv import load_dotenv, dotenv_values
from telegram import *
from telegram.ext import *
import requests
import overpy

import lang as en

load_dotenv()

TOKEN = os.getenv('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    if lang in en.LANGUAGES:
        lang = update.effective_user.language_code
    else:
        lang = 'en'

    keyboard = [[KeyboardButton(text = en.button_text[lang], request_location=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text = en.start_message[lang],
        parse_mode='HTML',
        reply_markup=reply_markup,
        disable_web_page_preview=True   
    )

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    if lang in en.LANGUAGES:
        lang = update.effective_user.language_code
    else:
        lang = 'en'

    keyboard = [
        [
            InlineKeyboardButton(en.report_button[lang], url='https://share-eu1.hsforms.com/1yJynPcprTIe1rzWPf14QSA2djdd8'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=en.report_message[lang],
        parse_mode='HTML',
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    if lang in en.LANGUAGES:
        lang = update.effective_user.language_code
    else:
        lang = 'en'
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=en.help_message[lang],
        parse_mode='HTML',
        disable_web_page_preview=True
    )
    

async def handle_position(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = update.effective_user.language_code
    if lang in en.LANGUAGES:
        lang = update.effective_user.language_code
    else:
        lang = 'en'

    text = update.message.location

    origin_latitude = text.latitude
    origin_longitude = text.longitude

    n_defib = 0
    area = 100
    
    api = overpy.Overpass()
    response = en.response_init[lang]
    keyboard = []

    exclude_s = '- node(id:'

    for area in range(100, 1025, 100):
        if n_defib == 0:
            result = api.query(f"""
                        [out:json];
                        (node["emergency"="defibrillator"](around:{area},{origin_latitude},{origin_longitude}););
                        out;""")
        else:
            result = api.query(f"""
                        [out:json];
                        (node["emergency"="defibrillator"](around:{area},{origin_latitude},{origin_longitude}); {exclude_s}););
                        out;""")
        
        if len(result.nodes) == 0:
            continue
            
        else:
            for node in result.nodes:
                dae_lat = node.lat
                dae_lon = node.lon
                dae_id = node.id

                my_referer = {
                    'Referer': 'https://nominatim.openstreetmap.org/reverse',
                    'User-Agent': 'DAE Locator Bot/1.0 (https://github.com/damnicolussi/dae-locator)'
                }

                street = requests.get(f'https://nominatim.openstreetmap.org/reverse?lat={dae_lat}&lon={dae_lon}&addressdetails=1&format=json', headers=my_referer)
                street = street.json()["address"]

                distance = requests.get(f'https://routing.openstreetmap.de/routed-foot/route/v1/driving/{origin_longitude},{origin_latitude};{dae_lon},{dae_lat}', headers=my_referer)
                jsonDistance = distance.json()["routes"][0]['legs'][0]["distance"]
                distance = f'{int(jsonDistance)} m' if int(jsonDistance) < 1000 else f'{round(int(jsonDistance)/1000, 1)} km'

                try:
                    location = f'{street["road"]}, {street["village"]}'
                except KeyError:
                    try:
                        location = f'{street["road"]}, {street["city"]}'
                    except KeyError:
                        location = f'{street["road"]}, {street["town"]}'

                keyboard.append([InlineKeyboardButton(f'{location} - {distance}', url=f'https://www.google.it/maps/dir/{origin_latitude},{origin_longitude}/{dae_lat},{dae_lon}')])

                if n_defib == 0:
                    exclude_s += str(dae_id)
                else:
                    exclude_s += (',' + str(dae_id))

                n_defib += 1
                if n_defib >= 3: break
            
            if n_defib >= 3: break

    if n_defib == 0:
        response += en.response_not_found[lang]
    else:
        response += en.response_found[lang]
        
    reply_markup = InlineKeyboardMarkup(keyboard)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode='HTML', reply_markup=reply_markup)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    report_handler = CommandHandler('report', report)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(report_handler)

    application.add_handler(MessageHandler(filters.LOCATION, handle_position))

    application.add_error_handler(error)

    application.run_polling()
