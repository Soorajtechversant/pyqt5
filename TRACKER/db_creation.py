import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tracker",
  password="Tracker@1",
  database="SystemTracker"

)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS TrackerDetails")
mycursor.execute("DROP TABLE IF EXISTS TrackerSummary")


sql = "CREATE TABLE TrackerSummary (tracker_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
      "date DATE, " \
      "start_time timestamp NULL DEFAULT NULL, " \
      "end_time timestamp NULL DEFAULT NULL," \
      "total_alphanumeric_keys INT DEFAULT NULL," \
      "total_special_keys INT DEFAULT NULL)"

mycursor.execute(sql)



sql = "CREATE TABLE TrackerDetails (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
      "Keys_pressed TEXT, " \
      "summary_id INT, " \
      "FOREIGN KEY(summary_id) REFERENCES TrackerSummary(tracker_id) ON DELETE CASCADE)"

mycursor.execute(sql)

mycursor.execute("SELECT * FROM TrackerSummary")

myresult = mycursor.fetchall()

print(myresult)

mycursor.execute("SELECT * FROM TrackerDetails")
myresult = mycursor.fetchall()
print(myresult)


