import flet as ft
from contact_manager import ContactManager, PersonalContact, BusinessContact
#
class ContactManagerApp:
    def __init__(self):
        self.contact_manager = ContactManager()
        self.app = None  # We'll set this in the setup_ui method

    def setup_ui(self, page: ft.Page):
        self.app = page
        self.app.title = "Contact Manager"
        self.app.theme_mode = ft.ThemeMode.LIGHT
        self.app.padding = 20

        self.contact_list = ft.ListView(expand=1, spacing=10, padding=20)
        self.update_contact_list()

        self.name_input = ft.TextField(label="Name", expand=1)
        self.phone_input = ft.TextField(label="Phone", expand=1)
        self.email_input = ft.TextField(label="Email", expand=1)
        self.extra_input = ft.TextField(label="Birthday/Company", expand=1)
        self.contact_type = ft.Dropdown(
            label="Contact Type",
            options=[
                ft.dropdown.Option("personal"),
                ft.dropdown.Option("business")
            ],
            expand=1
        )

        input_row = ft.Row([self.name_input, self.phone_input, self.email_input, self.extra_input, self.contact_type])
        
        add_button = ft.ElevatedButton("Add Contact", on_click=self.add_contact)
        update_button = ft.ElevatedButton("Update Contact", on_click=self.update_contact)
        delete_button = ft.ElevatedButton("Delete Contact", on_click=self.delete_contact)

        button_row = ft.Row([add_button, update_button, delete_button], alignment=ft.MainAxisAlignment.CENTER)

        self.app.add(
            ft.Column([
                ft.Text("Contact Manager", size=24, weight=ft.FontWeight.BOLD),
                input_row,
                button_row,
                self.contact_list
            ])
        )

    def update_contact_list(self):
        self.contact_list.controls.clear()
        for i, contact in enumerate(self.contact_manager.get_contacts()):
            self.contact_list.controls.append(
                ft.ListTile(
                    title=ft.Text(contact.name),
                    subtitle=ft.Text(f"{contact.phone} | {contact.email}"),
                    trailing=ft.Text(contact.get_contact_type()),
                    on_click=lambda _, i=i: self.select_contact(i)
                )
            )
        self.app.update()

    def add_contact(self, e):
        name = self.name_input.value
        phone = self.phone_input.value
        email = self.email_input.value
        extra = self.extra_input.value
        contact_type = self.contact_type.value

        if contact_type == "personal":
            contact = PersonalContact(name, phone, email, extra)
        else:
            contact = BusinessContact(name, phone, email, extra)

        self.contact_manager.add_contact(contact)
        self.update_contact_list()
        self.clear_inputs()

    def update_contact(self, e):
        selected_index = getattr(self, 'selected_index', None)
        if selected_index is not None:
            name = self.name_input.value
            phone = self.phone_input.value
            email = self.email_input.value
            extra = self.extra_input.value
            contact_type = self.contact_type.value

            if contact_type == "personal":
                contact = PersonalContact(name, phone, email, extra)
            else:
                contact = BusinessContact(name, phone, email, extra)

            self.contact_manager.update_contact(selected_index, contact)
            self.update_contact_list()
            self.clear_inputs()

    def delete_contact(self, e):
        selected_index = getattr(self, 'selected_index', None)
        if selected_index is not None:
            self.contact_manager.delete_contact(selected_index)
            self.update_contact_list()
            self.clear_inputs()

    def select_contact(self, index):
        contact = self.contact_manager.get_contacts()[index]
        self.name_input.value = contact.name
        self.phone_input.value = contact.phone
        self.email_input.value = contact.email
        self.contact_type.value = contact.get_contact_type()
        
        if isinstance(contact, PersonalContact):
            self.extra_input.label = "Birthday"
            self.extra_input.value = contact.birthday
        else:
            self.extra_input.label = "Company"
            self.extra_input.value = contact.company

        self.selected_index = index
        self.app.update()

    def clear_inputs(self):
        self.name_input.value = ""
        self.phone_input.value = ""
        self.email_input.value = ""
        self.extra_input.value = ""
        self.contact_type.value = None
        self.selected_index = None
        self.app.update()

def main(page: ft.Page):
    app = ContactManagerApp()
    app.setup_ui(page)

if __name__ == "__main__":
    ft.app(target=main)

