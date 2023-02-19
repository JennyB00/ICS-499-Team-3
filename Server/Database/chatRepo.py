import mysql.connector


class ChatRepo:
    def get_all_chat(cursor: mysql.connector.connection.MySQLCursor):
        query = "SELECT * FROM chat"
        cursor.execute(query)
        results = []
        for (chatID, creator) in cursor:
            results.append({"chatID": chatID})
            results.append({"creator": creator})
        return results
