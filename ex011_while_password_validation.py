# 2. Senha válida
# Peça uma senha ao usuário. Continue pedindo até ele digitar a senha correta (ex: "python123").
# senha = "python2025"
while True:
    usuario = input("Enter password: ").strip().lower()
    if usuario != "python2025":
        print("INVALID PASSWORD. Try again.")
    if usuario == "python2025":
        print("Correct password! Welcome.")
        break
