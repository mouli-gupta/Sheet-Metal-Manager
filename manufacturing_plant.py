import mysql.connector as mys

conn = mys.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="steel_manufacturing",
    auth_plugin="mysql_native_password"
)

if conn.is_connected():
    cursor = conn.cursor()
    print("Connected to MySQL.")
else:
    print("Error connecting to MySQL.")
    exit(1)

def print_table(rows):
    """Print column headers once, then each row."""
    if not rows:
        print("No records found.")
        return
    headers = [col[0] for col in cursor.description]
    # Header
    print(" | ".join(headers))
    print("-" * (len(headers) * 15))
    # Rows
    for row in rows:
        print(" | ".join(str(item) for item in row))

def show_products():
    try:
        cursor.execute("SELECT * FROM product")
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def delete_product():
    try:
        sno = int(input("Please enter the product number to delete: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("DELETE FROM product WHERE prodno = %s", (sno,))
        conn.commit()
        print(f"{cursor.rowcount} deleted.")
        show_products()
    except mys.Error as err:
        print("Error:", err)

def search_product():
    try:
        sno = int(input("Please enter the product number to search: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("SELECT * FROM product WHERE prodno = %s", (sno,))
        rec = cursor.fetchall()
        print_table(rec)
    except mys.Error as err:
        print("Error:", err)

def add_product():
    try:
        sno = int(input("Please enter the new product number: "))
        name = input("Please enter the product name: ")
        finish_type = input("Please enter the finish type: ")
        finish_color = input("Please enter the finish color if applicable, otherwise leave blank: ")
        material = input("Please enter the raw material: ")
        cp = int(input("Please enter the cost price: "))
        sp = int(input("Please enter the selling price: "))
        quantity = int(input("Please enter the quantity in stock: "))
        supplier = input("Please enter the supplier name: ")
        manufacturing_date = input("Please enter the manufacturing date (YYYY-MM-DD): ")
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute(
            "INSERT INTO product (prodno, name, finish_type, finish_color, material, cp, sp, quantity, supplier, manufacturing_date) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (sno, name, finish_type, finish_color, material, cp, sp, quantity, supplier, manufacturing_date)
        )
        conn.commit()
        print("Added.")
        show_products()
    except mys.Error as err:
        print("Error:", err)

def update_product():
    try:
        sno = int(input("Please enter the product number to update: "))
        new_sp = int(input("Please enter the new selling price: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("UPDATE product SET sp = %s WHERE prodno = %s", (new_sp, sno))
        conn.commit()
        print(f"{cursor.rowcount} updated.")
        show_products()
    except mys.Error as err:
        print("Error:", err)

def search_product_by_finish_type():
    ft = input("Please enter the finish type to search: ").strip()
    try:
        cursor.execute("SELECT * FROM product WHERE finish_type = %s", (ft,))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def search_product_by_finish_color():
    fc = input("Please enter the finish color to search: ").strip()
    try:
        cursor.execute("SELECT * FROM product WHERE finish_color = %s", (fc,))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def filter_products_by_price():
    try:
        low = int(input("Please enter the minimum selling price: "))
        high = int(input("Please enter the maximum selling price: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("SELECT * FROM product WHERE sp BETWEEN %s AND %s", (low, high))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def search_product_by_material():
    mat = input("Please enter the raw material to search: ").strip()
    try:
        cursor.execute("SELECT * FROM product WHERE material = %s", (mat,))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def filter_products_by_cost():
    try:
        low = int(input("Please enter the minimum cost price: "))
        high = int(input("Please enter the maximum cost price: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("SELECT * FROM product WHERE cp BETWEEN %s AND %s", (low, high))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def show_employees():
    try:
        cursor.execute("SELECT * FROM employee")
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def delete_employee():
    try:
        eno = int(input("Please enter the employee ID to delete: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("DELETE FROM employee WHERE empid = %s", (eno,))
        conn.commit()
        print(f"{cursor.rowcount} deleted.")
        show_employees()
    except mys.Error as err:
        print("Error:", err)

def search_employee():
    try:
        eno = int(input("Please enter the employee ID to search: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("SELECT * FROM employee WHERE empid = %s", (eno,))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def add_employee():
    try:
        eno = int(input("Please enter the new employee ID: "))
        name = input("Please enter the employee name: ")
        department = input("Please enter the department: ")
        post = input("Please enter the position or post: ")
        salary = int(input("Please enter the salary: "))
        age = int(input("Please enter the age: "))
        email = input("Please enter the email address: ")
        phone = input("Please enter the phone number: ")
        doj = input("Please enter the joining date (YYYY-MM-DD): ")
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute(
            "INSERT INTO employee (empid, name, department, post, salary, age, email, phone, doj) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (eno, name, department, post, salary, age, email, phone, doj)
        )
        conn.commit()
        print("Added.")
        show_employees()
    except mys.Error as err:
        print("Error:", err)

def search_employee_by_name():
    nm = input("Please enter the name to search: ").strip()
    try:
        cursor.execute("SELECT * FROM employee WHERE name LIKE %s", (f"%{nm}%",))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def filter_employees_by_salary():
    try:
        low = int(input("Please enter the minimum salary: "))
        high = int(input("Please enter the maximum salary: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("SELECT * FROM employee WHERE salary BETWEEN %s AND %s", (low, high))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def search_employee_by_post():
    pst = input("Please enter the position or post to search: ").strip()
    try:
        cursor.execute("SELECT * FROM employee WHERE post = %s", (pst,))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def filter_employees_by_age():
    try:
        low = int(input("Please enter the minimum age: "))
        high = int(input("Please enter the maximum age: "))
    except ValueError:
        print("Invalid input.")
        return
    try:
        cursor.execute("SELECT * FROM employee WHERE age BETWEEN %s AND %s", (low, high))
        rows = cursor.fetchall()
        print_table(rows)
    except mys.Error as err:
        print("Error:", err)

def update_employee():
    try:
        eno = int(input("Please enter the employee ID to update: "))
    except ValueError:
        print("Invalid input.")
        return
    print("Select field to update:")
    print("1 - Salary")
    print("2 - Position or post")
    sel = input("Please enter your selection: ").strip()
    if sel == '1':
        try:
            new_salary = int(input("Please enter the new salary: "))
        except ValueError:
            print("Invalid input.")
            return
        try:
            cursor.execute("UPDATE employee SET salary = %s WHERE empid = %s", (new_salary, eno))
            conn.commit()
            print(f"{cursor.rowcount} updated.")
        except mys.Error as err:
            print("Error:", err)
    elif sel == '2':
        new_post = input("Please enter the new position or post: ").strip()
        try:
            cursor.execute("UPDATE employee SET post = %s WHERE empid = %s", (new_post, eno))
            conn.commit()
            print(f"{cursor.rowcount} updated.")
        except mys.Error as err:
            print("Error:", err)
    else:
        print("Invalid selection.")
        return
    show_employees()

print("\n=== SHEET METAL MANUFACTURING PLANT ===\n")

while True:
    print("Main Menu:")
    print("O - Owner functions")
    print("P - Products")
    print("S - Employees")
    print("Q - Quit")
    choice = input("Please enter your selection: ").strip().upper()

    if choice == 'O':
        if input("Please enter the owner password: ") == '0987654321':
            print("Owner Menu:")
            print("1 - Show all employees")
            print("2 - Show all products")
            print("0 - Go back")
            sub = input("Please enter your selection: ").strip()
            if sub == '1':
                show_employees()
            elif sub == '2':
                show_products()
        else:
            print("Invalid password.")

    elif choice == 'P':
        print("\nProduct Management Menu:")
        print("1 - Show all products")
        print("2 - Delete a product")
        print("3 - Search for a product")
        print("4 - Add a new product")
        print("5 - Update a product")
        print("6 - Search products by finish type")
        print("7 - Search products by finish color")
        print("8 - Filter products by selling price range")
        print("9 - Search products by material")
        print("10 - Filter products by cost price range")
        print("0 - Go back")
        sel = input("Please enter your selection: ").strip()

        if sel == '1':
            show_products()
        elif sel == '2':
            delete_product()
        elif sel == '3':
            search_product()
        elif sel == '4':
            add_product()
        elif sel == '5':
            update_product()
        elif sel == '6':
            search_product_by_finish_type()
        elif sel == '7':
            search_product_by_finish_color()
        elif sel == '8':
            filter_products_by_price()
        elif sel == '9':
            search_product_by_material()
        elif sel == '10':
            filter_products_by_cost()

    elif choice == 'S':
        print("\nEmployee Management Menu:")
        print("1 - Show all employees")
        print("2 - Delete an employee")
        print("3 - Search for an employee")
        print("4 - Add a new employee")
        print("5 - Search employees by name")
        print("6 - Filter employees by salary range")
        print("7 - Update an employee")
        print("8 - Search employees by position or post")
        print("9 - Filter employees by age range")
        print("0 - Go back")
        sel = input("Please enter your selection: ").strip()

        if sel == '1':
            show_employees()
        elif sel == '2':
            delete_employee()
        elif sel == '3':
            search_employee()
        elif sel == '4':
            add_employee()
        elif sel == '5':
            search_employee_by_name()
        elif sel == '6':
            filter_employees_by_salary()
        elif sel == '7':
            update_employee()
        elif sel == '8':
            search_employee_by_post()
        elif sel == '9':
            filter_employees_by_age()

    elif choice == 'Q':
        print("Goodbye!")
        break

    else:
        print("Invalid selection.")
