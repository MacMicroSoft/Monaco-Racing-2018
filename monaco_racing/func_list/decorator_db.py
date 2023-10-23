import time
import functools
import sqlite3
from monaco_racing.models import db


class DatabaseError(Exception):
    pass


def retry_database(max_retries=3, delay=1):
    """
    :param max_retries: maximum number retries
    :param delay: Delay between attempts (seconds).
    :return: Decorator
    """
    def database_decorator(func):
        """
        :param func: function which use db connection
        :return: Checked database connection with Exception
        """
        functools.wraps(func)

        def wrapper_content(*args, **kwargs):
            for retry in range(max_retries + 1):
                conn = db.connect()
                try:
                    result = func(conn, *args, **kwargs)
                    conn.commit()
                    return result
                except (sqlite3.
                        DatabaseError) as e:
                    conn.rollback()
                    if retry < max_retries:
                        print(f"Attempt {retry + 1} failed. Retrying in {delay} seconds...")
                        time.sleep(delay)
                    else:
                        raise DatabaseError(f"Max retries exceeded for function {func.__name__} with error {e}")
                finally:
                    conn.close()
            return wrapper_content
        return database_decorator
