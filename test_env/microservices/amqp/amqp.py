# Set up amqp exchange with queues
# GDAC alert
# gdac.alert

# Log alert
# log.alert

# Localised alert
# {country}.{city}.alert

# Update user status
# [PUT] /disaster/update/user/{userID}

# Email user status
# [AMQP] {userID}.status

# Family member status
# [AMQP] {userID}.{familyID}.status

# Log event
# [AMQP] log.event

# Localised alert
# {country}.{city}.alert

from amqp_helper import Rabbitmq


if __name__ == '__main__':
    broker = Rabbitmq()
    broker._setup()
    ######################### ASSUME QUEUES ARE CREATED ON ACCOUNT CREATION ######################
    queues = [('gdacalert','gdac.alert'),
              ('logalert','log.alert'),
              ('logevent','log.event'),
              ('user_1','user.1.alert'),
              ('family_1','family.1.status'),
              ('family_all','family.*.status')
              ]
    broker.add_queue(queues)