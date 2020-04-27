# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email 

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self.save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('*--- * --- * --- * --- * --- * --- * --- *')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('*--- * --- * --- * --- * --- * --- * --- *')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
               del self._contacts[idx]
               self.save()
               break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
               self._print_contact(contact)
               break
        else:
            self._not_found()

    def _not_found(self):
        print('************')
        print('¡No encontrado!')
        print('************')

    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                self.update_contact(idx)
                self.save()                
                break
        else:
            self._not_found() 

    def update_contact(self, idx):
            name = str(input('Actualiza el nombre del contacto: '))
            phone = str(input('Actualiza el teléfono del contacto: '))
            email = str(input('Actualiza el email del contacto: '))

            contact = Contact(name, phone, email)
            self._contacts[idx] = contact

    def save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name','phone','email') )

            for contact in self._contacts:
                writer.writerow( (contact.name, contact.phone, contact.email) )

def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)

        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tulizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contacto
            [s]alir 
        '''))

        if command == 'a':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el teléfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'ac':
            name = str(input('Escribe el nombre del contacto a actualizar: '))
            contact_book.update(name)            
        elif command == 'b':
            name = str(input('Escribe el nombre del contacto a buscar: '))
            contact_book.search(name)
        elif command == 'e':
            name = str(input('Escribe el nombre del contacto a eliminar: '))
            contact_book.delete(name)
        elif command == 'l':
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('comando no encontrado')                                        

if __name__ == '__main__':
    print('BIENVENIDO A LA AGENDA')
    run()