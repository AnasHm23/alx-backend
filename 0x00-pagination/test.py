#!/usr/bin/env python3
import base64

original_string = "anas"
print(f"orignal string: {original_string}")

bytes_string = original_string.encode("utf-8")
print(f"utf-8 format: {bytes_string}")

encoded_bytes = base64.b64encode(bytes_string)
print(f"bytes format: {encoded_bytes}")

encoded_string = encoded_bytes.decode("utf-8")
print(f"encoded string: {encoded_string}")
