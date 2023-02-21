# username | password | status | privUID |
import mysql.connector
class AccountsRepo:
    def get_all_accounts(cursor: mysql.connector.connection.MySQLCursor):
        query = ("SELECT * FROM accounts")
        cursor.execute(query)
        results = []
        for (username, password) in cursor:
            results.append({"Username":username})
	    results.append({"Password":password})
        return results
