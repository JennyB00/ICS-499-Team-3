import mysql.connector


class ChatRepo:
    def get_all_chat(cursor: mysql.connector.connection.MySQLCursor):
        query = "SELECT * FROM chat"
        cursor.execute(query)
        results = []
        for (chatID, creator) in cursor:
            results.append({"ChatID": chatID})
            results.append({"Creator": creator})
        return results
