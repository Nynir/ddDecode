# ddDecode v.1.0.0 - utility for decoding decimal dump files

### Note: currently only functions on Linux devices.. working on fixing that

I wrote this code because I needed a quick and easy way to decode decimal dump files without installing anything extra. I hope it helps you.

## Decimal Dump

What is a decimal dump? A decimal dump is a lot like a hex dump except the data isn't in hex, rather it's stored as decimal values. It looks something like this:

```
[137,80,78,255, . . . ]
```

The values can range from 1 - 255 and are comma separated, usually encapsulated by brackets. The code does remove brackets as it isn't part of the data but you may often see the data surrounded by them.

## How to run

To run from the commandline you need to reference the full filepath of the file you want to decode:

```
[foo@bar ~]$ python ddDecode/main.py -f 'C:\Users\nynir\Documents\encoded_file'
```

## Future plans
- Currently only works on Linux because of the OS commands. I spent a while trying to get python to do what the OS commands do and wasn't having much luck, so until I fix that it'll be limited to Linux
- Optimization is something that needs to be worked on, going to be working on that after making the code more accessible
- GUI option maybe? That would make it easier to specify the file, by dragging and dropping
- Might make it into a larger suite that decodes more filetypes
