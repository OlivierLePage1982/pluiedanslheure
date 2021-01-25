import smtplib


def send_mail(subject: str, message: str) -> bool:
    with smtplib.SMTP('smtp.live.com') as server:
        server.starttls()
        server.login('olivier.le.page@outlook.fr', 'olivertwist82')
        from_address = 'olivier.le.page@outlook.fr'
        to_addresses = ['olivier.lp@gmail.com']
        msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s" % (from_address, ", ".join(to_addresses), subject, message)

        try:
            server.sendmail(from_address, to_addresses, msg)
        except smtplib.SMTPException as e:
            print(e)
            return False
        server.quit()
    return True


if __name__ == '__main__':
    send_mail('Alerte pluie', 'Entre 15h30 et 16h30 : Précipitations modérées'.encode('utf-8'))