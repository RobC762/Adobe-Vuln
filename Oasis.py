import base64
import time
import random

def jitter():
    time.sleep(random.uniform(0.05, 0.2))

def check_environment():
    platforms = ["win32", "linux"]
    return random.choice(platforms)

def decode_payload(data):
    jitter()
    try:
        return base64.b64decode(data).decode("utf-8")
    except Exception:
        return None

def main():
    env = check_environment()
    print(f"Environment detected: {env}")

    # Encoded payload recovered from memory dump
    payload = "ZmluYWwtZmxhZy1PYXNpcw=="

    decoded = decode_payload(payload)

    if decoded:
        print("Payload decoded successfully:")
        print(decoded)
    else:
        print("Decode failed")

if __name__ == "__main__":
    main()
