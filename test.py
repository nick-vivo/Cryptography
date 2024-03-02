import encryption.Enigma as En
roter1 = En.Roter("АБВ","123")
roter2 = En.Roter("123", "абв")

roters = [roter1, roter2]

enig = En.Enigma(roters)


enig.encrypt("БАБАВ", roters)