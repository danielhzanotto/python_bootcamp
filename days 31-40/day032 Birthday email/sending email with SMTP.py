import smtplib

my_email = "mmegaterio@gmail.com"
password = "zkyhcquwdplsxzkj"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="danielhaas94@gmail.com",
                        msg="Subject:Hello\n\nThis is the body")
