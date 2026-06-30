import sounddevice as sd

print("\n==============================")
print("ALL DEVICES")
print("==============================")

for i, d in enumerate(sd.query_devices()):

    print(f"\nID : {i}")
    print("Name :", d["name"])
    print("Host API :", sd.query_hostapis()[d["hostapi"]]["name"])
    print("Input :", d["max_input_channels"])
    print("Output :", d["max_output_channels"])