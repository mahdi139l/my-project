def strong_password(length=12):
    chars= str.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

print(strong_password())


#کد هک وای فای