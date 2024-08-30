import sys 
import os 
from st2common.runners.base_action import Action
import asyncio
import ssl
import asyncio

from datetime import datetime
import json
import ssl
import zlib
#import pyodbc
from nats.aio.client import Client as NATS
from st2common.runners.base_action import Action

class SayHelloClass(Action):
    def run(self, message):
        print(f"Hello {message}")