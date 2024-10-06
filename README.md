# Enigma Machine
The Enigma machine is a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication.
It was employed extensively by Nazi Germany during World War II, in all branches of the German military. The Enigma machine was considered so secure that it was used to encipher the most top-secret messages.

## Mathematical analysis
Combining three rotors from a set of five, each of the 3 rotor settings with 26 positions, and the plugboard with ten pairs of letters connected, the military Enigma has 158,962,555,217,826,360,000 different settings (nearly 159 quintillion or about 67 bits).
- Choose 3 rotors from a set of 5 rotors = 5 x 4 x 3 = 60
- 26 positions per rotor = 26 x 26 x 26 = 17,57
- Plugboard = 26! / ( 6! x 10! x 2^10) = 150,738,274,937,25
- Multiply each of the above = 158,962,555,217,826,360,000

## Encryption path

```
 Reflector Rotor  Rotor  Rotor   ETW  (Plugboard)
      |      3      2      1
     ___    ___    ___    ___    ___    ___
    |   |  |   |  |   |  |   |  |   |  |   |
    |  -|--|---|--|---|--|---|--|---|--|---|-- < Input
    | | |  |   |  |   |  |   |  |   |  |   |
    | | |  |   |  |   |  |   |  |   |  |   |
    |  -|--|---|--|---|--|---|--|---|--|---|-- > Output
    |   |  |   |  |   |  |   |  |   |  |   |
     ---    ---    ---    ---    ---    ---
```

## Rotors
Rotor | Turnover position | ABCDEFGHIJKLMNOPQRSTUVWXYZ
--- | --- | ---
I | R | EKMFLGDQVZNTOWYHXUSPAIBRCJ
II | F | AJDKSIRUXBLHWTMCQGZNPYFVOE
III | W | BDFHJLCPRTXVZNYEIWGAKMUSQO
IV | K | ESOVPZJAYQUIRHXLNFTGKDCMWB
V | A | VZBRGITYUPSDNHLXAWMJQOFECK

## Reflectors
Reflector | ABCDEFGHIJKLMNOPQRSTUVWXYZ
--- | ---
UKW-A | EJMZALYXVBWFCRQUONTSPIKHGD
UKW-B | YRUHQSLDPXNGOKMIEBFZCWVJAT
UKW-C | FVPJIAOYEDRZXWGCTKUQSBNMHL

## Encryption
Example for rotors III, II and I, and rings «C», «U» и «Q» after press key «A».

![image](https://github.com/user-attachments/assets/30fb1726-a9c2-4b43-bd03-fc09aa6e9b9d)

## Usage
```bash
>>> python main.py -h
usage: main.py [-h] [-r] [-k KEY] [--reflector] [--plugboard]

options:
  -h, --help         show this help message and exit
  -r , --rotor       For example -r ROTOR_II -r ROTOR_I -r ROTOR_III.
                     Support: ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V.
                     Default ROTOR_I, ROTOR_II, ROTOR_III
  -k KEY, --key KEY  For example --key a --key b --key c. Default a, a, a     
  --reflector        For example UKW_B.
                     Support: UKW_A, UKW_B, UKW_C.
                     Default: UKW_B
  --plugboard        For example --plugboard AB --plugboard CD
```

```
>>> python main.py -r ROTOR_I -k A -r ROTOR_I -k A -r ROTOR_I -k A --plugboard AB --plugboard CD 

  _____         _
 | ____| _ __  (_)  __ _  _ __ ___    __ _       
 |  _|  | '_ \ | | / _` || '_ ` _ \  / _` |      
 | |___ | | | || || (_| || | | | | || (_| |      
 |_____||_| |_||_| \__, ||_| |_| |_| \__,_|      
                   |___/                    v1   
                             by: tarodictrl      

Write text: hello
Encrypted text: GMHWP
```
