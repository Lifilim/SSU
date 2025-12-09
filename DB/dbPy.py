import psycopg2
from psycopg2 import Error


def selectAll(cur, tableName):
    cur.execute(f"SELECT * FROM {tableName}")
    return cur.fetchall()

def getCoefficients(cur):
    tableName = "coefficients"
    return selectAll(cur, tableName)

def getRoomClasses(cur):
    tableName = "roomclasses"
    return selectAll(cur, tableName)

def getChecks(cur):
    tableName = "checks"
    return selectAll(cur, tableName)




def fullCoefficients():





def main():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",        # как в pgAdmin
            port=5432,               # как в pgAdmin
            dbname="hotels",         # ваша БД                  database="hotels",       # ваша БД
            user="postgres",         # ваш пользователь
            password=input()
        )
        # автокоммит удобно включить для простых скриптов
        conn.autocommit = True
        cur = conn.cursor()

        print(getCoefficients(cur))
        print(getRoomClasses(cur))


        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            print(cur.fetchone())

            # пример INSERT ... RETURNING
            cur.execute(
                "INSERT INTO RoomClasses (active, size, cost) "
                "VALUES (%s, %s, %s) RETURNING id;",
                (True, 10, 1000.0)
            )
            new_id = cur.fetchone()[0]
            print("Inserted RoomClass id:", new_id)

    except Error as e:
        print(f"Ошибка при подключении к PostgreSQL: {e}")
    finally:
        if conn:
            conn.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == "__main__":
    main()
