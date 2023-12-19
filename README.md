# TxGen
Transaction generator for mining BTCW


# How to use


# STEP1
```
-Click on the green code button in the upper right
-Download zip
-Unzip to your computer
-Install the latest version of Python: https://www.python.org/downloads/
```

# STEP2
```
-Open 'main.py' and edit your BTCW receive address and tx fee as shown below
    btcw_receive_address = "BTCW_RX_ADDRESS_HERE"
    tx_fee   = "0.0001"
```

# STEP3
```
-Start QT wallet, go to Setting->Options and click on "Open Configuration File"
-Open the file 'bitcoin-pow.conf' and paste the contents into the file that was opened by QT and save the file.
```

# STEP4
Edit the file RUN_TX_GEN.bat
```
@echo off
python "main.py"
pause
```

Replace the python above to point to where ever Windows installed Python on your computer. Example:
```
@echo off
C:\Python312\python.exe "main.py"
pause
```


# STEP5
```
-Close QT wallet
-Start QT wallet
```


# STEP6
```
Double click on the RUN_TX_GEN.bat to start sending transactions to your BTCW address
```