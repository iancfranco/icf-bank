with open("usuarios.txt", "r") as lusr:
  usuarios = lusr.read().splitlines()
with open("passwords.txt", "r") as pssw:
  passw = pssw.read().splitlines()
with open("ids.txt", "r") as lids:
  ids = lids.read().splitlines()
with open("saldo.txt", "r") as lsal:
  saldo = lsal.read().splitlines()
qt_usuarios = len(usuarios)-1
logged = False
for i in range(0, qt_usuarios):
  ids[i] = int(ids[i])
#
while logged != True:
    print("[Conta Bancária]")
    print("Realizar login:")
    user = input("Usuário: ")
    user_pass = input("Senha: ")
    if user in usuarios:
        for i in range(0,qt_usuarios):
            if usuarios[i] == user:
                user_id = i
        if user == usuarios[user_id] and user_pass == passw[user_id]:
            print("Logado com sucesso.")
            logged = True
    else:
        print("Usuário não encontrado no sistema.")

while logged == True:
    print("----------------------------------------")
    print("Sistema bancário.")
    print("Você está logado como:", user)
    print("ID:", ids[user_id])
    print("Saldo:", saldo[user_id])
    print("----------------------------------------")
    print("1 - Realizar Transferência")
    print("2 - Realizar Cobrança")
    print("3 - Pagar Cobranças")
    print("4 - Sair")
    print("----------------------------------------")
    temp_r = input("Qual operação deseja realizar? ")
    try:
        temp_r = int(temp_r)
    except ValueError:
        print("Você inseriu um valor inválido.")
        continue
    if temp_r == 1:
        print("----------------------------------------")
        print("Realizar transferência.")
        destino = input("Para qual usuário deseja fazer a transferência? ")
        destino_id = input("Qual o ID do usuário a receber a transferência? ")
        try:
            destino_id = int(destino_id)
        except ValueError:
            print("ID inválido, tente novamente.")
            continue
        for i in range(0, qt_usuarios):
            if destino == usuarios[i]:
                if destino_id == ids[i]:
                    destino_id_index = i
                    valor_transferencia = input("Qual valor deseja transferir? ")
                    try:
                        valor_transferencia = int(valor_transferencia)
                    except ValueError:
                        print("Valor inválido.")
                        continue
                    print(f"Você está prestes a transferir R${valor_transferencia} para {usuarios[destino_id_index]}.")
                    confirm_pass = input("Insira sua senha para confirmar: ")
                    if confirm_pass == passw[user_id]:
                        print("Realizando transferência...")
                        if valor_transferencia > saldo[user_id]:
                            print("Você não possui saldo o suficiente para realizar essa transferência.")
                            continue
                        else:
                            saldo[user_id] -= valor_transferencia
                            saldo[destino_id_index] += valor_transferencia
                            print("Transferência realizada com sucesso.")
                            print(f"Seu saldo agora é: R${saldo[user_id]}")
                    else:
                        print("Senha incorreta.")
                        continue
    elif temp_r == 2:
        print("----------------------------------------")
        print("Realizar cobrança.")
        destino = input("Para qual usuário deseja fazer a cobrança? ")
        destino_id = input("Qual o ID do usuário a receber a cobrança? ")
        try:
            destino_id = int(destino_id)
        except ValueError:
            print("ID inválido, tente novamente.")
            continue
        for i in range(0, qt_usuarios):
            if destino == usuarios[i]:
                if destino_id == ids[i]:
                    destino_id_index = i
                    valor_transferencia = input("Qual valor deseja cobrar? ")
                    try:
                        valor_transferencia = int(valor_transferencia)
                    except ValueError:
                        print("Valor inválido.")
                        continue
                    print(f"Você está prestes a cobrar R${valor_transferencia} para {usuarios[destino_id_index]}.")
                    confirm_pass = input("Insira sua senha para confirmar: ")
                    if confirm_pass == passw[user_id]:
                        print("Realizando cobrança...")
                        with open(f"cobrancas{destino_id}.txt") as file:
                          i = 0
                          for line in file:
                              i += 1
                              print(line)
                          print(i)
                        with open(f"cobrancas{destino_id}.txt", "a") as f:
                          f.write(f"Cobrança de R${valor_transferencia} enviada por {usuarios[user_id]}(ID:{user_id}). ID da cobrança: {i}.\n")
                          f.close()
                    else:
                        print("Senha incorreta.")
                        continue
    elif temp_r == 3:
        print("----------------------------------------")
        print("Pagar cobranças.")
        print("Cobranças atuais: ")
        with open(f"cobrancas{ids[user_id]}.txt", "r") as f:
            print(f.read())
            f.close()
        print("----------------------------------------")
        print("Qual cobrança deseja pagar? ")
        pagamento = input("Digite o ID da cobrança: ")
        try:
            pagamento = int(pagamento)
        except ValueError:
            print("ID inválido, tente novamente.")
        with open(f"cobrancas{ids[user_id]}.txt") as file:
          i = 0
          for line in file:
            if f"ID da cobrança: {pagamento}" in line:
              print("Cobrança encontrada.")
              print(line)
            else:
              i += 1
              
        
