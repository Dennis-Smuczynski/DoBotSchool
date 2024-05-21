import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from lib.interface import Interface

bot = Interface("COM3")

print('Bot status:', 'connected' if bot.connected() else 'not connected')

print(bot.get_device_name())

