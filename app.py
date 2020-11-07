#!/usr/bin/env python3

from aws_cdk import core

from blue_bot.blue_bot_stack import BlueBotStack


app = core.App()
BlueBotStack(app, "blue-bot")

app.synth()
