#!/usr/bin/env python

"""
Joke Bot to return a list of telegram Bots/Channels on Telegram
"""

import logging
import os
from telegram.ext import Updater, CommandHandler
#from dotenv import load_dotenv

#uncomment port for heroku
PORT = int(os.environ.get('PORT', '8443'))
#load_dotenv()
#TOKEN = os.getenv('TOKEN')
TOKEN = os.environ["TOKEN"]


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='type /help for a list of commands')

def help(update, context):
    string = "Bot Commands:\n\n"
    string += "/bots\n"
    string += "/news\n"
    string += "/lifestyle\n"
    string += "/food\n"
    string += "/deals\n"
    string += "/transport\n"
    string += "/jobs\n"
    string += "/airfare\n"
    string += "/finance"
    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def bots(update, context):
    string = "Bots:\n\n"
    string += "@ShiokBot\n"
    string += "@Bus_Time_Bot\n"
    string += "@SGBusUncleBot\n"
    string += "@RainKorKorBot\n"
    string += "@SGMRT_Bot\n"
    string += "@SINGA_Bus_Bot\n"
    string += "@samanauntybot\n"
    string += "@BTOBuddy_Bot\n"
    string += "@TOTOHuatBot"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def news(update, context):
    string = "News:\n\n"
    string += "@LeeHsienLoong\n"
    string += "@TheStraitsTimes\n"
    string += "@CNALatest\n"
    string += "@MothershipSG\n"
    string += "@SGUpdate\n"
    string += "@SGTalk\n"
    string += "@GovSG\n"
    string += "@MustShareNews\n"
    string += "@ZaoBaoSG\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def lifestyle(update, context):
    string = "Lifestyle:\n\n"
    string += "@SGWeekend\n"
    string += "@SGWhereTo\n"
    string += "@DateIdeas\n"
    string += "@SGNewMovies\n"
    string += "@SGConcerts\n"
    string += "@SGFitnessHealth\n"
    string += "@SGParenthings\n"
    string += "@SGAskEveryone\n"
    string += "@SGNightLife\n"
    string += "@SGClubbing"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def food(update, context):
    string = "Food:\n\n"
    string += "@KiasuFoodies\n"
    string += "@MissTamChiak\n"
    string += "@SGFoodies\n"
    string += "@SGFoodDeals\n"
    string += "@ChopeDeals\n"
    string += "@SGFoodLobang\n"
    string += "@SGCoffeeLovers\n"
    string += "@SGBBT"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def deals(update, context):
    string = "Deals & Promos:\n\n"
    string += "@GoodLobang\n"
    string += "@SBSmarterWay\n"
    string += "@TheOfficialShopeeSG\n"
    string += "@BudgetBabes\n"
    string += "@SGStudentPromos\n"
    string += "@PelandoSG\n"
    string += "@Qoo10Deals\n"
    string += "@SGFreebie\n"
    string += "@SGCode\n"
    string += "@KiasuPolice"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def transport(update, context):
    string = "Transport:\n\n"
    string += "@SGMRT\n"
    string += "@SGCabPromos\n"
    string += "@SGHitch\n"
    string += "@SGRoadUpdates\n"
    string += "@SGCustom"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)


def jobs(update, context):
    string = "Jobs & Internships:\n\n"
    string += "@SingaporePartTimeJobs\n"
    string += "@SGInternships\n"
    string += "@SGInternship\n"
    string += "@PartTimers\n"
    string += "@SGPartTimers\n"
    string += "@SGQuickJobs\n"
    string += "@SGCareers\n"
    string += "@InternSG\n"
    string += "@SGRiceBowl\n"
    string += "@SGJOB4U"
    string += "@WerkWerkSG\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def airfare(update, context):
    string = "Airfare:\n\n"
    string += "@MileLion\n"
    string += "@SGTravelPromos\n"
    string += "@SGAirfarePromos\n"
    string += "@YouTripSG"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def finance(update, context):
    string = "Finance:\n\n"
    string += "@PersonalFinanceSG\n"
    string += "@DollarsAndSense\n"
    string += "@WokeSalaryMan\n"
    string += "@MoneySmartSingapore\n"
    string += "@SGBTO\n"
    string += "@CryptoSG\n"
    string += "@SGXInvest\n"
    string += "@SGMarketUpdates\n"
    string += "@TradingWithRayner\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text=string)

def donate(update, context):
    string = "BTC: 1ZR5ND0MBFAKEZXCBTCZQWAADRDESSZX"
    context.bot.send_message(chat_id=update.effective_chat.id, text=string)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    #updater = Updater("", use_context=True)
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("bots", bots))  
    dp.add_handler(CommandHandler("news", news))
    dp.add_handler(CommandHandler("lifestyle", lifestyle))
    dp.add_handler(CommandHandler("food", food))
    dp.add_handler(CommandHandler("deals", deals))
    dp.add_handler(CommandHandler("transport", transport))
    dp.add_handler(CommandHandler("jobs", jobs))
    dp.add_handler(CommandHandler("airfare", airfare))
    dp.add_handler(CommandHandler("finance", finance))
    dp.add_handler(CommandHandler("donate", donate))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    #comment this line to host on heroku
    #updater.start_polling()

    #Uncomment below lines for heroku
    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=TOKEN)
    updater.bot.setWebhook('APP URL' + TOKEN)

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
