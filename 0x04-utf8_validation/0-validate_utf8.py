#!/usr/bin/env python3
"""
UTF8 validation task
"""


def validUTF8(data):
    """
    valid UTF*
    """
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate through each byte in the data
    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte & mask1) == 0:
                # 1-byte character (ASCII)
                continue
            elif (byte & mask1) and (byte & mask2) == 0:
                # Invalid if starts with 10xxxxxx
                return False
            else:
                # Calculate the number of bytes
                num_ones = 0
                while (byte & mask1):
                    num_ones += 1
                    byte <<= 1
                if num_ones == 1 or num_ones > 4:
                    return False
                num_bytes = num_ones - 1
        else:
            # Check if it is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    # All characters should be properly completed
    return (num_bytes == 0)
