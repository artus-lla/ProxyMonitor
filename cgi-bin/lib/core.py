#!/usr/bin/env python3

import sys, os, base64


def decodificar(cadena):
    return base64.b64decode(cadena)

if __name__ == "__main__":
    
    print(decodificar(b'YWRtaW4x').decode())

     
