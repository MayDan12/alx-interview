#!/usr/bin/env python3
"""
UTF8 validation task
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    num_bytes = 0

    # Masks to check the most significant bits (MSBs) in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Convert to the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If the byte is a single byte character (0xxxxxxx)
            if num_bytes == 0:
                continue

            # UTF-8 characters can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the num of bytes remaining in the current UTF-8 character
        num_bytes -= 1

    # All characters should be processed
    return num_bytes == 0
