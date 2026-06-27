# AES-128 implementation for educational visualization.
# Implementasi inti dibuat manual, tidak memakai library kriptografi.

S_BOX = [
0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]

INV_S_BOX = [0] * 256
for i, v in enumerate(S_BOX):
    INV_S_BOX[v] = i

RCON = [
[0x00,0x00,0x00,0x00],
[0x01,0x00,0x00,0x00], [0x02,0x00,0x00,0x00], [0x04,0x00,0x00,0x00],
[0x08,0x00,0x00,0x00], [0x10,0x00,0x00,0x00], [0x20,0x00,0x00,0x00],
[0x40,0x00,0x00,0x00], [0x80,0x00,0x00,0x00], [0x1b,0x00,0x00,0x00],
[0x36,0x00,0x00,0x00]
]

SAMPLES = {
    'manual': {'label': 'Input Manual', 'plain_hex': '', 'plain_text': '', 'key': '', 'cipher': '', 'expected_plain': ''},
    'std': {
        'label': 'Contoh 1 - AES Standard Test Vector',
        'plain_hex': '00112233445566778899AABBCCDDEEFF',
        'plain_text': '',
        'key': '000102030405060708090A0B0C0D0E0F',
        'cipher': '69C4E0D86A7B0430D8CDB78070B4C55A',
        'expected_plain': '00112233445566778899AABBCCDDEEFF'
    },
    'hex1': {
        'label': 'Contoh 2 - Data Hex 1',
        'plain_hex': 'AABBCCDDEEFF00112233445566778899',
        'plain_text': '',
        'key': '11223344556677889900AABBCCDDEEFF',
        'cipher': 'C7EE066C38BB1C0797619CAD8A2BCA6A',
        'expected_plain': 'AABBCCDDEEFF00112233445566778899'
    },
    'hex2': {
        'label': 'Contoh 3 - Data Hex 2',
        'plain_hex': '0123456789ABCDEFFEDCBA9876543210',
        'plain_text': '',
        'key': '0F1571C947D9E8590CB7ADD6AF7F6798',
        'cipher': 'FF0B844A0853BF7C6934AB4364148FB9',
        'expected_plain': '0123456789ABCDEFFEDCBA9876543210'
    },
    'text1': {
        'label': 'Contoh 4 - Teks 16 Byte',
        'plain_hex': '54657374414553313238426C6F636B21',
        'plain_text': 'TestAES128Block!',
        'key': '2B7E151628AED2A6ABF7158809CF4F3C',
        'cipher': '3DD76534AC7B2D0125DF5EEC60D445B9',
        'expected_plain': '54657374414553313238426C6F636B21'
    },
    'text2': {
        'label': 'Contoh 5 - Teks 15 Byte + 00',
        'plain_hex': '4B524950544F47524146493230323600',
        'plain_text': 'KRIPTOGRAFI2026',
        'key': '000102030405060708090A0B0C0D0E0F',
        'cipher': '97079C23B917D87E354CC9C3772FB780',
        'expected_plain': '4B524950544F47524146493230323600'
    }
}

def xor_words(a, b):
    return [x ^ y for x, y in zip(a, b)]

def rot_word(w):
    return w[1:] + w[:1]

def sub_word(w):
    return [S_BOX[x] for x in w]

def bytes_to_state(data):
    return [[data[r + 4*c] for c in range(4)] for r in range(4)]

def state_to_bytes(state):
    return [state[r][c] for c in range(4) for r in range(4)]

def clone_state(state):
    return [row[:] for row in state]

def hex_byte(x):
    return f"{x:02X}"

def state_hex(state):
    return [[hex_byte(v) for v in row] for row in state]

def word_hex(w):
    return ''.join(hex_byte(x) for x in w)

def bytes_hex(data):
    return ''.join(hex_byte(x) for x in data)

def validate_hex_32(value, field):
    value = value.strip().replace(' ', '').upper()
    if len(value) != 32:
        raise ValueError(f"{field} harus tepat 32 karakter hex / 16 byte.")
    try:
        return list(bytes.fromhex(value))
    except ValueError as exc:
        raise ValueError(f"{field} hanya boleh berisi karakter hex 0-9 dan A-F.") from exc

def normalize_plaintext(value, input_type):
    value = value.strip()
    if input_type == 'hex':
        return validate_hex_32(value, 'Plaintext')
    if len(value) > 16:
        raise ValueError('Plaintext teks maksimal 16 karakter.')
    data = value.encode('utf-8')
    if len(data) > 16:
        raise ValueError('Plaintext UTF-8 maksimal 16 byte. Gunakan karakter ASCII agar aman.')
    return list(data + bytes(16 - len(data)))

def key_expansion(key_bytes):
    words = [key_bytes[i:i+4] for i in range(0, 16, 4)]
    details = []
    for i in range(4, 44):
        temp = words[i-1][:]
        info = {'index': i, 'prev': word_hex(temp), 'w_im4': word_hex(words[i-4])}
        if i % 4 == 0:
            rw = rot_word(temp)
            sw = sub_word(rw)
            rc = RCON[i // 4]
            temp = xor_words(sw, rc)
            info.update({
                'operation': 'g() = RotWord → SubWord → XOR Rcon',
                'rotword': word_hex(rw),
                'subword': word_hex(sw),
                'rcon': word_hex(rc),
                'after_g': word_hex(temp)
            })
        else:
            info.update({'operation': 'W[i-4] XOR W[i-1]', 'rotword': '-', 'subword': '-', 'rcon': '-', 'after_g': word_hex(temp)})
        new_word = xor_words(words[i-4], temp)
        words.append(new_word)
        info.update({'source': f"W[{i-4}] XOR temp", 'result': word_hex(new_word)})
        details.append(info)
    round_keys = [bytes_to_state(sum(words[4*r:4*r+4], [])) for r in range(11)]
    return words, round_keys, details

def add_round_key(state, round_key):
    return [[state[r][c] ^ round_key[r][c] for c in range(4)] for r in range(4)]

def sub_bytes(state):
    return [[S_BOX[state[r][c]] for c in range(4)] for r in range(4)]

def inv_sub_bytes(state):
    return [[INV_S_BOX[state[r][c]] for c in range(4)] for r in range(4)]

def shift_rows(state):
    out = clone_state(state)
    for r in range(1, 4):
        out[r] = state[r][r:] + state[r][:r]
    return out

def inv_shift_rows(state):
    out = clone_state(state)
    for r in range(1, 4):
        out[r] = state[r][-r:] + state[r][:-r]
    return out

def gmul(a, b):
    p = 0
    for _ in range(8):
        if b & 1:
            p ^= a
        hi = a & 0x80
        a = (a << 1) & 0xFF
        if hi:
            a ^= 0x1B
        b >>= 1
    return p

def mix_columns(state):
    out = [[0]*4 for _ in range(4)]
    for c in range(4):
        a0,a1,a2,a3 = [state[r][c] for r in range(4)]
        out[0][c] = gmul(a0,2) ^ gmul(a1,3) ^ a2 ^ a3
        out[1][c] = a0 ^ gmul(a1,2) ^ gmul(a2,3) ^ a3
        out[2][c] = a0 ^ a1 ^ gmul(a2,2) ^ gmul(a3,3)
        out[3][c] = gmul(a0,3) ^ a1 ^ a2 ^ gmul(a3,2)
    return out

def inv_mix_columns(state):
    out = [[0]*4 for _ in range(4)]
    for c in range(4):
        a0,a1,a2,a3 = [state[r][c] for r in range(4)]
        out[0][c] = gmul(a0,14) ^ gmul(a1,11) ^ gmul(a2,13) ^ gmul(a3,9)
        out[1][c] = gmul(a0,9) ^ gmul(a1,14) ^ gmul(a2,11) ^ gmul(a3,13)
        out[2][c] = gmul(a0,13) ^ gmul(a1,9) ^ gmul(a2,14) ^ gmul(a3,11)
        out[3][c] = gmul(a0,11) ^ gmul(a1,13) ^ gmul(a2,9) ^ gmul(a3,14)
    return out

def record_op(name, before, after, note=''):
    return {'name': name, 'before': state_hex(before), 'after': state_hex(after), 'note': note}

def encrypt_block(plain_bytes, key_bytes):
    words, round_keys, key_details = key_expansion(key_bytes)
    steps = []
    state = bytes_to_state(plain_bytes)
    initial_state = clone_state(state)
    before = clone_state(state)
    state = add_round_key(state, round_keys[0])
    steps.append({'round': 'Initial Round', 'operations': [record_op('AddRoundKey dengan RK0', before, state, 'State plaintext di-XOR dengan cipher key awal.') ]})
    for rnd in range(1, 10):
        ops = []
        before = clone_state(state); state = sub_bytes(state); ops.append(record_op('SubBytes', before, state, 'Substitusi byte memakai S-Box AES.'))
        before = clone_state(state); state = shift_rows(state); ops.append(record_op('ShiftRows', before, state, 'Baris 1, 2, 3 digeser kiri 1, 2, 3 posisi.'))
        before = clone_state(state); state = mix_columns(state); ops.append(record_op('MixColumns', before, state, 'Perkalian matriks di GF(2^8) dengan polinomial 0x11B.'))
        before = clone_state(state); state = add_round_key(state, round_keys[rnd]); ops.append(record_op(f'AddRoundKey dengan RK{rnd}', before, state, 'XOR state dengan round key.'))
        steps.append({'round': f'Round {rnd}', 'operations': ops})
    ops = []
    before = clone_state(state); state = sub_bytes(state); ops.append(record_op('SubBytes', before, state))
    before = clone_state(state); state = shift_rows(state); ops.append(record_op('ShiftRows', before, state))
    before = clone_state(state); state = add_round_key(state, round_keys[10]); ops.append(record_op('AddRoundKey dengan RK10', before, state, 'Final round tidak menggunakan MixColumns.'))
    steps.append({'round': 'Round 10 / Final Round', 'operations': ops})
    cipher = state_to_bytes(state)
    return build_result('encrypt', initial_state, cipher, words, round_keys, key_details, steps)

def decrypt_block(cipher_bytes, key_bytes):
    words, round_keys, key_details = key_expansion(key_bytes)
    steps = []
    state = bytes_to_state(cipher_bytes)
    initial_state = clone_state(state)
    before = clone_state(state)
    state = add_round_key(state, round_keys[10])
    steps.append({'round': 'Initial Decryption', 'operations': [record_op('AddRoundKey dengan RK10', before, state, 'Ciphertext di-XOR dengan round key terakhir.') ]})
    for rnd in range(9, 0, -1):
        ops = []
        before = clone_state(state); state = inv_shift_rows(state); ops.append(record_op('InvShiftRows', before, state, 'Baris digeser kanan sesuai indeks baris.'))
        before = clone_state(state); state = inv_sub_bytes(state); ops.append(record_op('InvSubBytes', before, state, 'Substitusi balik memakai Inverse S-Box.'))
        before = clone_state(state); state = add_round_key(state, round_keys[rnd]); ops.append(record_op(f'AddRoundKey dengan RK{rnd}', before, state))
        before = clone_state(state); state = inv_mix_columns(state); ops.append(record_op('InvMixColumns', before, state, 'Perkalian matriks invers di GF(2^8).'))
        steps.append({'round': f'Decryption Round {rnd}', 'operations': ops})
    ops = []
    before = clone_state(state); state = inv_shift_rows(state); ops.append(record_op('InvShiftRows', before, state))
    before = clone_state(state); state = inv_sub_bytes(state); ops.append(record_op('InvSubBytes', before, state))
    before = clone_state(state); state = add_round_key(state, round_keys[0]); ops.append(record_op('AddRoundKey dengan RK0', before, state, 'Final decryption round tanpa InvMixColumns.'))
    steps.append({'round': 'Final Decryption Round 0', 'operations': ops})
    plain = state_to_bytes(state)
    return build_result('decrypt', initial_state, plain, words, round_keys, key_details, steps)

def build_result(mode, initial_state, output_bytes, words, round_keys, key_details, steps):
    text = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in output_bytes)
    return {
        'mode': mode,
        'initial_state': state_hex(initial_state),
        'output_hex': bytes_hex(output_bytes),
        'output_text': text.rstrip('\x00').rstrip('.'),
        'words': [{'index': i, 'hex': word_hex(w), 'bytes': [hex_byte(x) for x in w]} for i, w in enumerate(words)],
        'key_details': key_details,
        'round_keys': [{'name': f'RK{i}', 'matrix': state_hex(rk)} for i, rk in enumerate(round_keys)],
        'steps': steps
    }

def aes_process(mode, input_value, input_type, key_hex):
    key_bytes = validate_hex_32(key_hex, 'Key')
    if mode == 'encrypt':
        data = normalize_plaintext(input_value, input_type)
        return encrypt_block(data, key_bytes)
    if mode == 'decrypt':
        data = validate_hex_32(input_value, 'Ciphertext')
        return decrypt_block(data, key_bytes)
    raise ValueError('Mode harus encrypt atau decrypt.')

if __name__ == '__main__':
    for sid, sample in SAMPLES.items():
        if sid == 'manual':
            continue
        res = aes_process('encrypt', sample['plain_text'] or sample['plain_hex'], 'text' if sample['plain_text'] else 'hex', sample['key'])
        print(sample['label'], res['output_hex'])
