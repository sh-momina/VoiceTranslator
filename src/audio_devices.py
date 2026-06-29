import sounddevice as sd

print(sd.query_devices())

print("\n==============================")
print("Default Devices")
print("==============================")

print(sd.default.device)