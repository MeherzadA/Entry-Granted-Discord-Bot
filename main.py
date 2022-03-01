from PIL import Image, ImageDraw, ImageFont
import discord 
import traceback
import sys
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import os
from datetime import date
from keep_alive import keep_alive
import random

## requests module allows bot to make an hhtps request, and retrieve date from the API's
import requests 

#API returns json, so we need to import this module as well
import json


client = discord.Client()

## Helper function that we can call upon when we want to retrieve the doggo image from the API 
##    def fetch_doggo():
  ## Storing the response of the API in variable doggy (The link is from the API's website)
  ####    doggy = requests.get(https://dog.ceo/api/breeds/image/random)
  ####    json_data = json.loads(doggy.text)
   

@client.event
async def on_ready():
  print("We have INFLINTRATED THE BASE, WE ARE CURRENTLY logged in as {0.user}".format(client)) ## Callback to when the bot is ready to be used

@client.event
async def on_message(message): # Callback to when the bot recieves a message FROM ANYONE 
  channel = message.channel 
  
  if message.author == client.user:
    return    ## Makes it so that the bot won't do anything if the message is from the bot itself
  
  if message.content.startswith("h"): ## If the message starts with "$help"
    await channel.send("$hi - say hi \n$trash - I dare you to say I'm trash\n$test - Don't wake me up, please. I enjoy my REM\n$qr - doesnt work dont use it")

  if message.content.startswith("$hi"):## If the message starts with "$hello"
    await channel.send("Sup bro!") ## This is the bot's response if the user sends $hello
  


    
    



client = commands.Bot(command_prefix= "$") ## only this command is working, the $help and all the other stuff above is being ignored for some reason... 


@client.command(aliases = ["qrrandomOG", "rqrOG", "qrandomOG"])
async def randomqrOG(ctx, year, month, day):
  filename = "qrcodetemplatebetter.png"
  img = Image.open(filename)
  font_type = ImageFont.truetype("arial.ttf", 53)
  draw = ImageDraw.Draw(img)
  draw.text(xy=(100, 390), text ="You are granted entry", fill = (51, 62, 63), font = font_type)
  draw.text(xy=(100, 450), text ="     for: {}-{}-{}".format(year, month, day), fill = (51, 62, 63), font = font_type)
  img = img.save('new_img.png')
  img
  await ctx.send(file = discord.File('new_img.png'))











## Telling the program that if, in any of the bot commands, the user doesn't have enough required arguments, it will result in an error message
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Bro, input some more arguments dumbass.\nEx: ``$randomqr yo mama fat``\n``$qr firstname lastname``\nAlso, emojis don't work, so stop trying to use :hot_face: you aren't funny")

@client.command()
async def day(ctx):
  today = date.today()
  await ctx.send("Today's date is:")
  await ctx.send(today)

@client.command()
async def qrOG(ctx):
  today = date.today()
  filename = "qrcodetemplatebetter.png"
  img = Image.open(filename)
  font_type = ImageFont.truetype("arial.ttf", 53)
  draw = ImageDraw.Draw(img)
  draw.text(xy=(100, 390), text ="You are granted entry", fill = (51, 62, 63), font = font_type)
  draw.text(xy=(100, 450), text =(f"     for: {today}") , fill = (51, 62, 63), font = font_type)
  img = img.save('new_img.png')
  img
  await ctx.send(file = discord.File('new_img.png'))   


@client.command()
async def qr(ctx, firstname, lastname):
  today = date.today()
  today = str(today)
  filename = "NEWqrcodeBLANKtemplate.png"
  img = Image.open(filename)
  font_entry = ImageFont.truetype("arial.ttf", 60)
  font_firstnamelastname = ImageFont.truetype("arial.ttf", 37)
  font_date = ImageFont.truetype("arial.ttf", 31)
  draw = ImageDraw.Draw(img)
  draw = ImageDraw.Draw(img)
  
  imgwidth, imgheight = img.size
  w, h = font_entry.getsize("Entry granted")
  centerW1 = (imgwidth - w)/2
  
  wFirstName, hFirstname = font_firstnamelastname.getsize(firstname)
  wLastName, hLastname = font_firstnamelastname.getsize(lastname)
  combined =  wFirstName + wLastName
  centerW2 = (imgwidth - combined)/2

  wDate, hDate = font_date.getsize(today)
  centerW3 = (imgwidth - wDate)/2

  draw.text(xy=(centerW1, 363), text ="Entry granted", fill = (51, 62, 63), font = font_entry)

  draw.text(xy=(centerW2, 453), text =(f"{firstname} {lastname}") , fill = (51, 62, 63), font = font_firstnamelastname)
  
  draw.text(xy=(centerW3, 513), text =(f"{today}") , fill = (51, 62, 63), font = font_date)


  img = img.save('new_img.png')
  img
  await ctx.send(file = discord.File('new_img.png'))  




@client.command()
async def hlp(ctx):
  help = ("$qr — Get Your Daily QR Code Here!\n$randomqr — Create your own QR code text! (Very useless but shut up)\n$day — In case you just happen to forget the date and u can't be bothered to press the home screen on your phone, but can be bothered to type out a useless command!")

   ## Writing out the embed look and desciription, used color = ctx.author.color so that the color of the embed is the same as the user's pfp
  embed = discord.Embed(title = "**Commands**", description = help, color=ctx.author.color)

  ## Telling the program to try to DM the user the list of commands, but if user has DMs disabled, it'll ping the user in the server and tell them that they have DM's disabled
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send(f"I can't DM you, {ctx.author.mention}!\nRemember to turn on ``Allow direct messages from server members`` in your **Privacy and Safety** settings, and try again!")
  else:
    await ctx.send(f"A list of commands has been sent to you, {ctx.author.mention}!")

  

  




  


    
keep_alive()
client.run(os.environ["SUSSY"])        
