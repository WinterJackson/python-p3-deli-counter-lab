# lib/deli_counter.py

def line(queue):
    if not queue:
        return "The line is currently empty."
    else:
        line_info = "The line is currently:"
        for position, customer in enumerate(queue, start=1):
            line_info += f" {position}. {customer}"
        return line_info

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        serving_customer = queue.pop(0)
        print(f"Currently serving {serving_customer}.")

# Example usage
katz_deli = []

take_a_number(katz_deli, "Ada")
take_a_number(katz_deli, "Grace")
take_a_number(katz_deli, "Kent")

print(line(katz_deli))

now_serving(katz_deli)

print(line(katz_deli))

take_a_number(katz_deli, "Matz")

print(line(katz_deli))

now_serving(katz_deli)

print(line(katz_deli))
