# 16.9.3. In the "Pet House" project, we will add a new service — an electronic wallet. You need to create a "Customer" class
# that will contain data about customers and their financial transactions. The following information is known
# about the client: first name, last name, city, balance.
# Next, make a conclusion about the clients in the console in the format: "Ivan Petrov. Moscow. Balance: $50."

# 16.9.4. The "Pet House" project team is planning a big event for its clients. You need to write a program
# that allows making a guest list. Add a method to the "Customer" class that returns only client's first name, last name
# and city. Then create a list of all clients and output it to the console.

class Customer:

    def __init__(self, first_name, last_name, city, balance, status):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.balance = balance
        self.status = status

    def __str__(self):
        return f'{self.first_name} {self.last_name}. {self.city}. Balance: ${self.balance} {self.status}.'

    def main_info(self):
        return f'{self.first_name} {self.last_name}. {self.city}. {self.status}'

cust_1 = Customer('Tatyana', 'Kudryavtseva', 'Bishkek', 20, 'Student')
print(cust_1)

cust_2 = Customer('Harry', 'Potter', 'Little Whinging', 10, "Mentor")
cust_3 = Customer('Ron', 'Weasley', 'The Burrow', 3.5, "Mentor")
cust_4 = Customer('Hermione', 'Granger', 'London', 40, "Mentor")
cust_5 = Customer('Albus', 'Dumbledore', 'Hogwarts', 1000, 'Student')

guest_list = [cust_1, cust_2, cust_3, cust_4, cust_5]

for i in range(len(guest_list)):
    print(f'{i+1}. {guest_list[i].main_info()}')


