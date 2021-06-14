import pymysql 

class PybaDatabase:
    def __init__(self):
        # Local
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "12345"
        self.database = "testdb"
        self.connection = self.createConnection()
        self.cursor = self.createCursor()

        # Heroku
        """self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "12345"
        self.database = "videoappdb"
        self.connection = self.createConnection()
        self.cursor = self.createCursor()"""

    def createConnection(self):
        con = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            passwd = self.password,
            database = self.database,
            charset = "utf8mb4",
            cursorclass = pymysql.cursors.DictCursor,
        )
        return con

    def createCursor(self):
        con = self.connection
        cursor = None
        if con is not None:
            cursor = con.cursor()
        else:
            print("app is disconnected from database")

        return cursor

    # PARA SELECT
    def executeQuery(self, sql):
        cursor = self.cursor
        result = None
        if cursor is not None:
            cursor.execute(sql)
            result = cursor.fetchall()

        return result

    # PARA INSERT, DELETE, UPDATE u otros. Regresa True o False.
    def executeNonQueryBool(self, sql):
        cursor = self.cursor
        con = self.connection
        sucess = False
        if cursor is not None:
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                sucess = True
            
        return sucess

    # PARA INSERT, DELETE, UPDATE u otros. Regresar el número afectado.
    def executeNonQueryRows(self, sql):
        cursor = self.cursor
        con = self.connection
        sucess = False
        if cursor is not None:
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
            
        return rows
