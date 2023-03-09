#from user.person import Person
from company.company import Company

def main():
    name = input('Digite su nombre: ')
    age = int(input('Digite su edad: '))
    company1 = Company(name, age)
    print(company1)
    print(company1.person)
    print(company1.person.name)
    print(company1.person.age)
    print(company1.person.hello())

if __name__ == '__main__':
    main()