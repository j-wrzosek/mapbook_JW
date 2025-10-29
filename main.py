users: list = [
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3},
    {'name': 'Asia', 'location': 'Krakow', 'posts': 5},
    {'name': 'Basia', 'location': 'Wroclaw', 'posts': 7},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twoj znajomy {user["name"]} z miejscowosci {user["location"]} opublikowal {user["posts"]} postow.')


while True:
    tmp_choice: int = int(input('wybierz opcje menu:'))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        print('wybarno funkcje wyswietlania aktywnosci znajomych')
        user_info(users)
    if tmp_choice == 2:
        print('wybrano funkcje dodawania znajomego')
    if tmp_choice == 3:
        print('wybrano funkcje usuwania znajomego')
    if tmp_choice == 4:
        print('wybrano funkcje aktualizacji znajomych')
