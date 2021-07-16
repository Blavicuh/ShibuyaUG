class Hashfix(object): 
 game_file = "gamesave"

 hash_offset = 32
 hash_length = 32
 body_offset = hash_offset + hash_length

 file = open(game_file, 'rb')
 data = bytearray(file.read() )
 file.close()

 body = data[body_offset:]
 hash = bytearray(hashlib.sha256(body).digest())

 for i in range (0, hash_length):
     data[hash_offset + i] = (hash [31-i] ^ oxff)

     out = open(game_wile, 'wb')
     out.write(data)
     out.close()

    pass




