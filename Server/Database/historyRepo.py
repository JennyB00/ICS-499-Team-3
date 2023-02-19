import mysql.connector
class HistoryRepo:
    def get_all_history(cursor: mysql.connector.connection.MySQLCursor):
        query = ("SELECT * FROM history")
        cursor.execute(query)
        results = []
        for (chatID, username, messageDate, messageString, messageFile) in cursor:
            results.append({"ChatID0":chatID})
	    results.append({"Username":username})
	    results.append({"MessageDate":messageDate})
            results.append({"MessageString":messageString})
	    results.append({"MessageFile":messageFile})
        return results
