import time
from faker import Faker
from art import text2art

fake = Faker()

# Arte ASCII
ascii_art = text2art("Doxerr")
print(ascii_art)

nameOnInternet = input("Escribe el nick de la persona que doxees: ").strip().lower()

print(
    "Que necesitas de la persona? \n1) Dirección \n2) Correo \n3) Número de teléfono \n4) Dirección IP \n5) DOXEO COMPLETO"
)
whatDoYouWannaKnow = input().strip().lower()

whitelist = [
    "snow", "aike", "eliasap", "irbought", "andrexus", "beki", "angibd"
]

data = {
    'name': fake.name(),
    'email': fake.email(),
    'phone_number': fake.phone_number(),
    'company': fake.company(),
    'job': fake.job(),
    'birthdate': fake.date_of_birth(),
    'address': fake.address(),
    'city': fake.city(),
    'state': fake.state(),
    'country': fake.country(),
    'postal_code': fake.postcode(),
    'latitude': fake.latitude(),
    'longitude': fake.longitude(),
    'credit_card_number': fake.credit_card_number(),
    'credit_card_expiry': fake.credit_card_expire(),
    'credit_card_provider': fake.credit_card_provider(),
    'ssn': fake.ssn(),
    'license_plate': fake.license_plate(),
    'iban': fake.iban(),
    'url': fake.url(),
    'text': fake.text(),
    'ip_address': fake.ipv4()
}

if nameOnInternet in whitelist:
    print("Persona no posible de vulnerable por protección")
else:
    if whatDoYouWannaKnow == "5" or whatDoYouWannaKnow == "doxeo completo":
        print("Información completa generada:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
    elif whatDoYouWannaKnow == "1" or whatDoYouWannaKnow == "dirección":
        print("Ubicación generada:")
        time.sleep(6)
        print("Letme think")
        time.sleep(3)
        print(f"Dirección: {data['address']}")
        time.sleep(2)
        print(f"Ciudad: {data['city']}")
        time.sleep(2)
        print(f"Estado: {data['state']}")
        time.sleep(2)
        print(f"País: {data['country']}")
        time.sleep(2)
        print(f"Latitud: {data['latitude']}")
        time.sleep(2)
        print(f"Longitud: {data['longitude']}")
    elif whatDoYouWannaKnow == "2" or whatDoYouWannaKnow == "correo":
        time.sleep(6)
        print("Letme think")
        time.sleep(3)
        print(f"Correo ENCONTRADO: {data['email']}")
    elif whatDoYouWannaKnow == "3" or whatDoYouWannaKnow == "número de teléfono":
        time.sleep(6)
        print("Letme think")
        time.sleep(3)
        print(f"Número de teléfono generado: {data['phone_number']}")
    elif whatDoYouWannaKnow == "4" or whatDoYouWannaKnow == "dirección ip":
        time.sleep(6)
        print("Letme think")
        time.sleep(3)
        print(f"Dirección IP generada: {data['ip_address']}")
    else:
        print("Opción no válida. Por favor, elige una opción correcta.")
