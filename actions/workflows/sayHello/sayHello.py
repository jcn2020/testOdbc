import sys 
import os 
from st2common.runners.base_action import Action
import asyncio
import ssl

class SayHelloClass(Action):
    def run(self, message):
        print(f"Hello {message}")