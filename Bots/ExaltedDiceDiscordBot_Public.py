import discord
import re
import random
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents=intents)
intents.message_content = True

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# ROLL COMMAND #
@bot.command()
async def roll(ctx, arg):
    cmdString = arg

    # /roll help

    if arg == "help":
        await ctx.send("Syntax: /roll d<numDice|required>!<difficulty|optional, default 7>s<specialty|optional> Example: /roll d3!6 rolls 3 ten sided dice at specified difficulty 6. If difficulty is not specified with the '!', it will default to 7. Adding an 's' at the end of the command will convert the roll to a specialty roll. ")
        return
    elif 'd' in arg:
        # Check if "s" is present in the argument #
        if 's' in arg:
            Specialty = True
        else:
            Specialty = False

        # Check if "!" is present in the arguement #
        match = re.search(r'!(\d+)', arg)
        if match:
            Difficulty = int(match.group(1))
        else:
            Difficulty = 7

        # Check if "d" is present in the argument/Check Dice
        match = re.search(r'd(\d+)', arg)
        if match:
            TotalDice = int(match.group(1))
        else:
            TotalDice = 7

        # Insert Dice Roller Here #
        DieList = []
        Die = 1

        # Construct the Die List #
        while Die <= TotalDice:
            Face = random.randint(1,10)
            DieList.append(Face)
            Die += 1

        # Count Ones, Successes, and Bonus Dice #
        Ones = 0
        Succ = 0
        BonusDice = 0
        # Iterate DieList using indices #
        for index in range(len(DieList)):
            if DieList[index] == 1: 
                Ones += 1  # Count Ones
            elif DieList[index] == 10:  # Count Tens
                if Specialty:  # If Specialty Roll, Roll an Extra Die
                    Face = random.randint(1, 10)
                    if Face >= Difficulty:
                        Succ += 1
                    DieList.append(Face)
                    BonusDice += 1  # Count Bonus Dice
                    Succ += 1  # Increment Success Count on a Specialty 10
                else:
                    Succ += 1 # Increment Success Count on a non Specialty 10
            elif DieList[index] >= Difficulty:  # Increment Success Count 
                Succ += 1

        # Check for Botch (Zero Successes and at least 1 One #
        Botch = False
        if Ones > 0 and Succ <= 0:
            Botch = True
        # Sort the Die List #
        DieList.sort()

        # Output the Die Results #
        BonusPrinted = False
        Output = ""
        for index in range(len(DieList)):
            Output =  Output + str(DieList[index]) + ", "
                

        # OUTPUT TO CHANNEL TEXT HERE.
        if Botch:
            await ctx.send(f"Dice rolled: {TotalDice + BonusDice} against Difficulty {Difficulty}: {Output}. You acheived {Succ} Successes. There were {BonusDice} Bonus Dice from Specialty 10's in this roll. This is a BOTCH!")
        else:
            await ctx.send(f"Dice rolled: {TotalDice + BonusDice} against Difficulty {Difficulty}: {Output}. You acheived {Succ} Successes. There were {BonusDice} Bonus Dice from Specialty 10's in this roll.")
    else: await ctx.send("Sorry, command not recognized.")
# Run the bot
bot.run('') # INSERT YOUR KEY IN THIS STRING. KEY OMITTED FROM CODE BECAUSE PRIVATE.




