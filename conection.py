import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="0000",
        db="foodwaste",
    )

    cur = conn.cursor()
    cur.execute("Show tables;")
    output = cur.fetchall()
    print(output)

    # To close the connection
    conn.close()


# Driver Code
if __name__ == "__main__":
    mysqlconnect()
