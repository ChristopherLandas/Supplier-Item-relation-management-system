import pymysql.cursors

class database:

  def connect():
    try:
      connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Wcch21zff0s4',
        database='supplier_management',
        cursorclass=pymysql.cursors.DictCursor
      )
      return connection
    except:
      return None;

  def fetchData(sqlCommand: str, params: tuple = ()) -> list:
    '''Read function'''
    connection: pymysql.connections.Connection = database.connect()

    if(connection is None):
      return {}

    try:
      with connection.cursor() as cursor:
        cursor.execute(sqlCommand, params)
        return cursor.fetchall(); 
    except:
      return None
    finally:
      connection.close()
    
  def execNonQuery(sqlCommand: str, params: tuple = ()):
    '''Create/Insert function'''
    connection: pymysql.connections.Connection = database.connect()

    if(connection is None):
      return False

    try:
      with connection.cursor() as cursor:
        cursor.execute(sqlCommand, params)
        connection.commit();
        connection.close()
        return True
    except Exception as e:
      print(e)
      connection.close()
      return False

  def execScalar(sqlCommand: str, params: tuple = ()):
    """Get the first column of the first row of the record"""
    connection: pymysql.connections.Connection = database.connect()

    if(connection is None):
      return None

    try:
      with connection.cursor() as cursor:
        cursor.execute(sqlCommand, params)
        return next(iter(cursor.fetchone().values())); 
    except:
      return None
    finally:
      connection.close()