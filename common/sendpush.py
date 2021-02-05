import requests
import logging
import common.constants


def send_push(subject: str, message: str) -> bool:
    logging.info('Pushing notification to PushBullet device')
    response = requests.post(common.constants.PUSH_URL,
                             headers={'Access-Token': common.constants.PUSH_TOKEN,
                                      'Content-type': 'application/json'},
                             json={'body': message,
                                   'title': subject,
                                   'type': 'note'})
    if response.status_code == requests.codes.ok:
        logging.info('Push notification sent successfully')
    else:
        logging.warning('Unable to send push notification: ' + response.json())
    return True


if __name__ == '__main__':
    send_push('Alerte pluie', 'Entre 15h30 et 16h30 : Précipitations modérées')