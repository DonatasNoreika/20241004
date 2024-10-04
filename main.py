import sqlite3

conn = sqlite3.connect('autos.db')
c = conn.cursor()

query = '''
CREATE TABLE IF NOT EXISTS auto (
    id INTEGER NOT NULL UNIQUE,
    make VARCHAR(50),
    model VARCHAR(50),
    year INTEGER,
    color VARCHAR(50),
    price INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);
'''

with conn:
    c.execute(query)

while True:
    veiksmas = int(input("1 - įvesti\n2 - peržiūrėti\n3 - ieškoti\n0 - išeiti\n"))
    match veiksmas:
        case 1:
            print("Enter new car:")
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            color = input("Color: ")
            price = int(input("Price: "))
            with conn:
                c.execute("INSERT INTO auto VALUES (NULL, ?, ?, ?, ?, ?)", (make, model, year, color, price))
        case 2:
            with conn:
                c.execute("SELECT * FROM auto")
                autos = c.fetchall()
                for auto in autos:
                    print(auto)
        case 3:
            query2 = "SELECT * FROM auto WHERE make LIKE ? AND model LIKE ? AND year BETWEEN ? AND ? AND color LIKE ? AND price BETWEEN ? AND ?"
            print("Enter search:")
            make = input("Make: ")
            model = input("Model: ")
            year_from = input("Year from: ")
            year_to = input("Year to: ")
            color = input("Color: ")
            price_from = input("Price from: ")
            price_to = input("Price to: ")
            with conn:
                c.execute(query2, (
                    make if make else "%",
                    model if model else "%",
                    int(year_from) if year_from else 1800,
                    int(year_to) if year_to else 2100,
                    color if color else "%",
                    int(price_from) if price_from else 0,
                    int(price_to) if price_to else 1000000,
                ))
                autos = c.fetchall()
                for auto in autos:
                    print(auto)
        case 0:
            break