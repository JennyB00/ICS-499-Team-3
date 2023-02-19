import mysql.connector
class ContactsRepo:
    def get_all_contacts(cursor: mysql.connector.connection.MySQLCursor):
        query = ("SELECT * FROM contacts")
        cursor.execute(query)
        results = []
        for (username, contact) in cursor:
            results.append({"Username":username})
	    results.append({"Contact":contact})
        return results
