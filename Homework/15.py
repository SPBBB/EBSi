# assign values by binary numbers.
WIFI = 0b0001
BLUETOOTH = 0b0010
GPS = 0b0100
CAMERA = 0b1000

# edit the values by binary operators.
config = WIFI | GPS
print("Initial config:", bin(config)) ## Initial config: 0b101

config |= BLUETOOTH # config = config | BLUETOOTH
print("After enabling Bluetooth:",bin(config))

print("GPS enabled?:",bool(config & GPS))

# 0b & 0b : and operator
config &= ~WIFI # config = config & !WIFI
print("After disabling Wi-fi:",bin(config))

