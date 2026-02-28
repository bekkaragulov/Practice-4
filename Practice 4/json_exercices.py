import json

# Открываем JSON файл
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Заголовок таблицы
print("Interface Status")
print("=" * 79)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)

# Проходим по интерфейсам в JSON
# Предположим, что JSON структура примерно такая:
# {"imdata": [{"l1PhysIf": {"attributes": {"dn": "...", "descr": "...", "speed": "...", "mtu": "..."}}}, ...]}
for item in data["imdata"]:
    interface = item["l1PhysIf"]["attributes"]
    dn = interface.get("dn", "")
    descr = interface.get("descr", "")
    speed = interface.get("speed", "")
    mtu = interface.get("mtu", "")
    
    # Вывод в формате таблицы
    print(f"{dn:<50} {descr:<20} {speed:<6} {mtu:<6}")