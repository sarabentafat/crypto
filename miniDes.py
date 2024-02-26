def generate_keys(key):
    # Define the P-Boxes
    p10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p8 = [6, 3, 7, 4, 8, 5, 10, 9]

    # Perform the initial P10 permutation on the key
    key = [key[p10[i]-1] for i in range(10)]

    # Split the key into left and right halves
    left, right = key[:5], key[5:]

    # Perform a left shift on each half
    left = left[1:] + left[:1]
    right = right[1:] + right[:1]

    combined = left + right
    key1 = [combined[p8[i]-1] for i in range(8)]

    # Perform another left shift on each half
    left = left[2:] + left[:2]
    right = right[2:] + right[:2]
    combined = left + right
    key2 = [combined[p8[i]-1] for i in range(8)]
   
    return key1, key2

def mini_des_8bit(key1, key2, plaintext):
    # Define the S-Boxes
    s0 = [
        [[0, 1], [0, 0], [1, 1], [1, 0]],
        [[1, 1], [1, 0], [0, 1], [0, 0]],
        [[0, 0], [1, 0], [0, 1], [1, 1]],
        [[1, 1], [0, 1], [1, 1], [1, 0]]
    ]

    s1 = [
        [[0, 0], [0, 1], [1, 0], [1, 1]],
        [[1, 0], [0, 0], [0, 1], [1, 1]],
        [[1, 1], [0, 0], [0, 1], [1, 0]],
        [[1, 0], [0, 1], [0, 0], [1, 1]]
    ]

    # Define the P-Boxes and E/P
    ip = [2, 6, 3, 1, 4, 8, 5, 7]
    ip_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    ep = [4, 1, 2, 3, 2, 3, 4, 1]
    p4 = [2, 4, 3, 1]

    # Initial permutation
    plaintext = [plaintext[ip[i]-1] for i in range(8)]

    # Split the plaintext into left and right halves
    left, right = plaintext[:4], plaintext[4:]

    # Perform the F function on the right half with key1
    right_expanded = [right[ep[i]-1] for i in range(8)]
    right_key_mix = [right_expanded[i] ^ key1[i] for i in range(8)]
    right_substituted = s0[right_key_mix[0]*2 + right_key_mix[1]] + s1[right_key_mix[2]*2 + right_key_mix[3]]
    right_permuted = [item for sublist in right_substituted for item in sublist]
    right_permuted = [right_permuted[p4[i]-1] for i in range(4)]

    # Swap the left and right halves
    left, right = right, [left[i] ^ right_permuted[i] for i in range(4)]
    print("R1:", right)

    # Perform the F function on the right half with key2
    right_expanded = [right[ep[i]-1] for i in range(8)]
    right_key_mix = [right_expanded[i] ^ key2[i] for i in range(8)]
    right_substituted = s0[right_key_mix[0]*2 + right_key_mix[1]] + s1[right_key_mix[2]*2 + right_key_mix[3]]
    right_permuted = [item for sublist in right_substituted for item in sublist]
    right_permuted = [right_permuted[p4[i]-1] for i in range(4)]

    # Combine the left and right halves
    result = left + [left[i] ^ right_permuted[i] for i in range(4)]
    print("R2:", result[4:])

    # Perform the final permutation
    ciphertext = [result[ip_inv[i]-1] for i in range(8)]

    return ciphertext

key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
key1, key2 = generate_keys(key)

print("Key 1:", key1)
print("Key 2:", key2)

plaintext = [0, 1, 1, 1, 0, 0, 1, 0]
ciphertext = mini_des_8bit(key1, key2, plaintext)

print ('#'*100)
print("===> Ciphertext:", ciphertext)
print ('#'*100)