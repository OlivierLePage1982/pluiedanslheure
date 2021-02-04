import requests
import logging
import common.constants


def send_push(subject: str, message: str) -> bool:
    logging.info('Pushing notification to PushBullet device')
    response = requests.post(common.constants.push_url,
                             headers={'Access-Token': common.constants.push_token,
                                      'Content-type': 'application/json'},
                             json={'body': message,
                                   'title': subject,
                                   'type': 'note'})
    logging.info(response.json())
    return True


if __name__ == '__main__':
    send_push('Alerte pluie', 'Entre 15h30 et 16h30 : Précipitations modérées')