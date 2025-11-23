from model import User


class Controller:
    def __init__(self, map_widget, listbox, labels):
        self.users = []
        self.markers = []
        self.map_widget = map_widget
        self.listbox = listbox
        self.labels = labels

    def add_user(self, name, location, posts, img_url):
        user = User(name, location, posts, img_url)
        self.users.append(user)

        marker = self.map_widget.set_marker(user.coords[0], user.coords[1], text=user.name)
        self.markers.append(marker)

        self.update_listbox()


    def delete_user(self):
        index = self.listbox.index("active")

        self.markers[index].delete()
        self.markers.pop(index)

        self.users.pop(index)
        self.update_listbox()

    def edit_user(self, name, location, posts, img_url):
        index = self.listbox.index("active")
        user = self.users[index]

        user.name = name
        user.location = location
        user.posts = posts
        user.img_url = img_url
        user.coords = user.get_coordinates()


        self . update_listbox









# def add_user(users_data: list) -> None:
#     name: str = entry_name.get()
#     location: str = entry_lokalizacja.get()
#     posts:int=int(entry_posty.get())
#     img_url: str = entry_img_url.get()
#     users_data.append(User(name=name, location=location, posts=posts, img_url=img_url))
#     print(users_data)
#     user_info(users_data)
#     #czyszczenie formularza
#     entry_name.delete(0, END)
#     entry_lokalizacja.delete(0, END)
#     entry_posty.delete(0, END)
#     entry_img_url.delete(0, END)
#     entry_name.focus()
#
#
# def user_info(users_data: list):
#     listbox_lista_obiektow.delete(0, END)
#     for idx,user in enumerate(users_data):
#         listbox_lista_obiektow.insert(idx, f'{user.name} {user.location} {user.posts} posty')
#
#
#
#
#
#
# def delete_user(users_data: list):
#     i = listbox_lista_obiektow.index(ACTIVE)
#     users_data[i].marker.delete()
#     users_data.pop(i)
#     user_info(users_data)
#
#
# def user_details(users_data: list):
#     i = listbox_lista_obiektow.index(ACTIVE)
#     label_imie_szczegoly_obiektu_wartosc.config(text=users_data[i].name)
#     label_lokalizacja_szczegoly_obiektu_wartosc.config(text=users_data[i].location)
#     label_posty__szczegoly_obiektu_wartosc.config(text=users_data[i].posts)
#     map_widget.set_position(users_data[i].coords[0], users_data[i].coords[1])
#     map_widget.set_zoom(10)
#
#
# def edit_user(users_data: list):
#     i = listbox_lista_obiektow.index(ACTIVE)
#     entry_name.insert(0, users_data[i].name)
#     entry_lokalizacja.insert(0, users_data[i].location)
#     entry_posty.insert(0, users_data[i].posts)
#     entry_img_url.insert(0, users_data[i].img_url)
#
#     button_dodaj_obiekt.config(text='Zapisz zmiany', command=lambda: update_user(users_data, i))
#
# def update_user(users_data: list, i):
#     users_data[i].name = entry_name.get()
#     users_data[i].location = entry_lokalizacja.get()
#     users_data[i].posts = entry_posty.get()
#     users_data[i].img_url = entry_img_url.get()
#
#     users_data[i].coords=users_data[i].get_coordinates()
#     users_data[i].marker.set_position(users_data[i].coords[0], users_data[i].coords[1])
#     users_data[i].marker.set_text(text=users_data[i].name)
#
#     user_info(users_data)
#
#     button_dodaj_obiekt.config(text="Dodaj obiekt", command=lambda:add_user(users))
#
#     entry_name.delete(0, END)
#     entry_lokalizacja.delete(0, END)
#     entry_posty.delete(0, END)
#     entry_img_url.delete(0, END)
#     entry_name.focus()