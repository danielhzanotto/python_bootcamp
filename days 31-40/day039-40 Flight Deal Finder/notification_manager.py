import smtplib

MY_EMAIL = ""
PASSWORD = ""


class SendEmail:
    def __init__(self):
        pass

    def send_email(self, info):

        self.message = f"ALERTA DE PRECO BAIXO!!! Somente R${info['price']},00 saindo de {info['cityCodeFrom']} para {info['cityTo']}-{info['cityCodeTo']} por {info['nightsInDest']} dias, de {info['local_departure']} ate {info['date_return']}."

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:BORA VIAJAR\n\n{self.message}")
