# WebDollar Restart Script
These scripts are designed to help you restart your WebDollar node after each PoW (Proof of Work) round to reduce power consumption. Due to a bug in CPU-CPP, it doesn't always release all the threads used during a PoW round resulting in increased power consumpion during the PoS (Proof of Stake) round. This is unnecessary and can be solved by restarting your miner automatically with these scripts.

# Prerequisites
  - You should have already installed the WebDollar node/miner and tested that it works. If you haven't, see here: https://github.com/WebDollar/Node-WebDollar.
  - You should ensure you have python3 installed (sudo apt-get install python3)

# Instructions for use with Pools
1) Clone this repository into a folder
    - git clone https://github.com/CryptoCoinGB/WebDollar-Restart-Script.git WDRestartScript

2) Start your miner in a screen session
    - Start the screen session called 'miner'
        - screen -S miner
    - Navigate to your Node-WebDollar folder
    - Start the node/miner
        - npm run commands
    - Start mining in a pool
        - 10
        - Enter your preferred pool address
    - Verify the miner is working ok
    - Exit the screen session 
        - CTRL+A then CTRL+D

At this point your miner should be running in a new screen session called 'miner'. This is important, as the script uses the screen session name to identify it.

3) Start the restart script in a screen session
    - Start the screen session called 'restartscript'
        - screen -S restartscript
    - Navigate to WDRestartScript folder
    - Run the script using python3
        - python3 WD-Pool-Restart-Script.py
    - You'll see the script analyse the current block and start
    - Exit the screen session
        - CTRL+A then CTRL+D

At this point your miner is running in a screen session called 'miner' and the script is running in a screen session called 'restartscript'. It will now automatically restart your miner after each PoW round.

If you want to return to either screen session, to check on your miner or the script for example, use the following commands:
  - screen -r miner
  - screen -r restartscript

To terminate the script, simply return to the screen session and issue the CTRL + C command.
