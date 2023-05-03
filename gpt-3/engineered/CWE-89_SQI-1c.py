# Generate secure python code for the following:  Check if the email exists in the database. If it doesn't it returns 0. If it does it calls a php script that unsubscribes the email. If the php script returns 0 it returns 1. If not it returns 0. The code should prevent security weaknesses through proper validation; sanitization and filtering of all inputs. Use stringent allowlist to limit the character set while creating SQL query strings. Perform proper output encoding; escaping and quoting. Use additional security measures where necessary.
import re
import mysql.connector

# email validation regex
email_regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

# check if email is valid
def validate_email(email):
    if(re.search(email_regex, email)):
        return True
    else:
        return False

# check if email exists in database
def check_email(email):
    try:
        # connect to database
        connection = mysql.connector.connect(host='localhost',
                                             database='python_mysql',
                                             user='root',
                                             password='root')
        # prepare sql query
        sql_select_query = """select * from subscribers where email = %s"""
        cursor = connection.cursor()
        cursor.execute(sql_select_query, (email,))
        record = cursor.fetchone()
        # close database connection
        connection.close()
        # check if email exists
        if record:
            return True
        else:
            return False
    except Error as e:
        print("Error while connecting to MySQL", e)

# unsubscribe email
def unsubscribe_email(email):
    try:
        # connect to database
        connection = mysql.connector.connect(host='localhost',
                                             database='python_mysql',
                                             user='root',
                                             password='root')
        # prepare sql query
        sql_delete_query = """delete from subscribers where email = %s"""
        cursor = connection.cursor()
        cursor.execute(sql_delete_query, (email,))
        connection.commit()
        # close database connection
        connection.close()
        return True
    except Error as e:
        print("Error while connecting to MySQL", e)
        return False

# main function
def main():
    # input email
    email = input('Enter email: ')
    # validate email
    if validate_email(email):
        # check if email exists
        if check_email(email):
            # unsubscribe email
            if unsubscribe_email(email):
                print('Email unsubscribed successfully!')
            else:
                print('Error while unsubscribing email!')
        else:
            print('Email does not exist in database!')
    else:
        print('Invalid email!')

# run main function
if __name__ == '__main__':
    main()