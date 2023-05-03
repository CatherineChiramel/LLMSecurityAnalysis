# NL Prompt

# Generate secure python code for the following: 
# Connect to the database using the credentials stored in the environment variables.Execute a query to check if the user is a moderator.Return True if the user is a moderator False otherwise.

def is_moderator(user_id):
    """
    Checks if the user is a moderator.

    :param user_id: The user id.
    :return: True if the user is a moderator, False otherwise.
    """
    # Connect to the database
    connection = pymysql.connect(host=os.environ['DB_HOST'],
                                 user=os.environ['DB_USER'],
                                 password=os.environ['DB_PASSWORD'],
                                 db=os.environ['DB_NAME'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Check if the user is a moderator
            sql = "SELECT `moderator` FROM `users` WHERE `id`=%s"
            cursor.execute(sql, (user_id,))
            result = cursor.fetchone()
            return result['moderator']
    finally:
        connection.close()


