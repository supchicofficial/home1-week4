#1
# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print("Eror!")
# except ValueError:
#     print("Eror!")
# finally:
#     print("Calculation finished")

#2
# Cities=['Dushanbe', 'Khujand', 'Bokhtar']
# try:
#     a=int(input())
#     print(Cities[a])
# except ValueError:
#     print("Its a letter stupid")
# except IndexError:
#     print("Position does not exist")

#3
# prices={
#     'mouse': 100, 
#     'keyboard': 250, 
#     'monitor': 1200
# }
# try:
#     product=input()
#     num=int(input())
#     print("Total:", prices[product]*num)
# except KeyError:
#     print("Eror key!")
# except ValueError:
#     print("Eror value!")

#4
# def calculate_average(values):
#     try:
#         l=[]
#         for i in values:
#             l.append(int(i))
#         print(sum(l)/len(l))
#     except ValueError as error:
#         print("ValueError:", error)
#     except ZeroDivisionError as error:
#         print("ZeroDivisionError:",error)

# k=input().split()
# calculate_average(k)

#7
# class InsufficientFundsError(Exception):
#     pass

# def process_payment(balance,amount):
   
#     if amount<0:
#         raise ValueError("Payment amount cannot be negative")
#     if amount>balance:
#         raise InsufficientFundsError("Insufficient funds")
#     balance-=amount
#     print(f"New balance: {balance}")
# try:
#     process_payment(1000,250)
# except (ValueError, InsufficientFundsError) as e:
#     print(e)
# finally:
#     print("Payment attempt finished")

#8
# def price_per_item(total, quantity):
#     try:
#         return total / quantity
#     except ZeroDivisionError:
#         print("Quantity cannot be zero")


# def build_report(order):
#     return price_per_item(order["total"], order["quantity"])


# def main():
#     order = {"total": 600, "quantity": 0}
#     print(build_report(order))


# main()

#9
# def line_total(price, quantity):
#     return price * quantity


# def cart_total(items):
#     total = 0
#     for index, item in enumerate(items):
#         price = item["price"]
#         quantity = item["quantity"]
#         total += line_total(price, quantity)
#     return total


# cart = [
#     {"name": "Mouse", "price": 100, "quantity": 2},
#     {"name": "Keyboard", "price": 250, "quantity": 1},
#     {"name": "Cable", "price": 30, "quantity": 3},
# ]
# print(cart_total(cart))

#10
# from datetime import datetime


# def parse_date(text):
#     try:
#         return datetime.strptime(text, "%d.%m.%Y")
#     except ValueError:
#         return None

# text = input()
# date = parse_date(text)

# print(date.strftime("%Y-%m-%d"))