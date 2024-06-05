import sys
import csv


def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


# add(['Anonymous','0000000000','someone@example.com','street, city'])


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data


# view()


def remove(i):
    def save(j):
        with open('data.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(j)

    newList = []
    phone = i

    with open('data.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            newList.append(row)

            for element in row:
                if element == phone:
                    newList.remove(row)
    save(newList)


# remove('0000000001')
# view()

def update(i):

    def updateNewlist(j):
        with open('data.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(j)

    newList = []
    phone = i[0]

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            newList.append(row)
            for element in row:
                if element == phone:
                    name = i[1]
                    phone = i[2]
                    email = i[3]
                    address = i[4]
                    data = [name, phone, email, address]
                    index = newList.index(row)
                    newList[index] = data

    updateNewlist(newList)


# sample = ['9876543210', 'joel', '9876543210', 'joel@gmail.com', 'vadodara, gujarat']
# update(sample)


def search(i):
    data = []
    phone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == phone:
                    data.append(row)
    print(data)
    return data
# search('9876543210')
