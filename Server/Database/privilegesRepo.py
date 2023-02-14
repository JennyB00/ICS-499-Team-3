import mysql.connector
class PrivilegesRepo:
    def get_all_privileges(cursor: mysql.connector.connection.MySQLCursor):
        query = ("SELECT * FROM privileges")
        cursor.execute(query)
        results = []
        for (chatID, username, send, receive, addUser, deleteMessage, deleteChat) in cursor:
            results.append({"chatID":chatID})
        return results

# uid | accountUID | send | receive | addUser | deleteMessage | deleteChat