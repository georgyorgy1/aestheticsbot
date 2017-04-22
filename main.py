import discord
import asyncio
import random
from roaster import art

bot = discord.Client();
filew = open("roaster.txt", "w");
#filer = open("roaster.txt", "r");

@bot.event
async def on_ready():
    print("Bot is now online. Enjoy!");

@bot.event
@asyncio.coroutine
async def on_message(message):
    if message.content.startswith('$aesthetics'):
        print("Sending A E S T H E T I C S");
        await bot.send_message(message.channel, random.choice(open('roaster.txt').readlines()));
    if message.content.startswith('$submit'):
        str_content = message.content[len('$submit'):].strip();
        filew.write(str_content);
        filew.close();

def main():
    email = "";
    password = "";
    token = "";
    bot_start = input("Start bot as?(u/t): ");
    if bot_start == "u":
        email = input("Enter email: ");
        password = input("Enter password: ");
        bot.run(email, password);
    elif bot_start == "t":
        token = input("Enter token: ");
        bot.run(token);
    else:
        print("Invalid. Shutting down.....");
        quit();

main();