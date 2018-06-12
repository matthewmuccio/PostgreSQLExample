#!/usr/bin/env python3


# A driver that connects to PostgreSQL database for us once we give it a database name.
import psycopg2
# Creates cursors for us dynamically using dictionaries
from psycopg2.extras import RealDictCursor


if __name__ == "__main__":
	# Connect and Cursor objects created.
	connection = psycopg2.connect("dbname=btc_prices")
	connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
	cursor = connection.cursor(cursor_factory=RealDictCursor)

	# Creates table krakenUSD with the given schema.
	cursor.execute(
		"""CREATE TABLE krakenUSD(
			pk SERIAL PRIMARY KEY,
			unix_time INTEGER,
			last_price FLOAT,
			trade_volume FLOAT
		);"""
	)

	# Close the cursor and database connection.
	cursor.close()
	connection.close()
	print("Program exited.")
