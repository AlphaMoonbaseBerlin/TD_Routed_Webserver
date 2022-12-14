'''Info Header Start
Name : cookie
Author : Admin@DESKTOP-RTI312L
Version : 0
Build : 2
Savetimestamp : 2022-12-14T22:53:08.376042
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''
import json
from dataclasses import dataclass

@dataclass
class Cookie:
    key : str
    value : str 
    same_site : str = "Strict"
    max_age : int = 2592000