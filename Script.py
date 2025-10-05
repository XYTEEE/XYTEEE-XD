import os, sys
try:
    __import__("Public").key()
except Exception as e:
    exit(str(e))
 
