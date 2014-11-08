#!/usr/bin/env python3
from OSC import OSCClient, OSCMessage
import time

client = OSCClient()
client.connect( ("localhost", 9001) )

for i in range(50):
	client.send( OSCMessage("/test/kick", [1] ) )
	time.sleep(0.1)
