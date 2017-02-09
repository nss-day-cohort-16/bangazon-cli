class Customer():

    def __init__(self, customer_name, street_address, city, state, postal_code, phone_number):
        self.customer_name = customer_name 
        self.street_address = street_address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone_number = phone_number
        self.status = False

    def get_customer_name(self):
        return self.customer_name

    def get_street_address(self):
        return self.street_address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_postal_code(self):
        return self.postal_code

    def get_phone_number(self):
        return self.phone_number

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = new_status
        return self.status