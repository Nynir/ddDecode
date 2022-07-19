# ddDecode v.1.0.0 - utility for decoding decimal dump files

### Note 1: You can do this via CyberChef! This functionality was needed on a system without access to CyberChef.
### Note 2: currently only functions on Linux devices

I wrote this code because I needed a quick and easy way to decode decimal dump files without installing anything extra. I hope it helps you. I originally wrote it to solve a specific case on the job, but decided to re-create it on my own time to further develop the capability.

## Decimal Dump

What is a decimal dump? A decimal dump is a lot like a hex dump except the data isn't in hex, rather it's stored as decimal values. It looks something like this:

```
[137,80,78,255, . . . ]
```

The values can range from 1 - 255 and are comma separated, usually encapsulated by brackets. The code does remove brackets as it isn't part of the data but you may often see the data surrounded by them.

## How to run

To run from the commandline you need to reference the full filepath of the file you want to decode:

```
[foo@bar ~]$ python ddDecode/main.py -f C:\Users\nynir\Documents\encoded_file
```
