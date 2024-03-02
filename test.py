import encryption.Enigma as En
roter1 = En.Roter("АБВ","АБВ")
roter2 = En.Roter("", "абв")

roters = [roter1, roter2]

enig = En.Enigma(roters)


enig.encrypt("БАБАВ", roters)