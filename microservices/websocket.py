# Send status FROM WEBSOCKET TO MICROSERVICE (S2)
# [POST] /user/status

# Get family status BETWEEN UI AND WEBSOCKET (S2)
# [WebSocket] /{familyID}/users/status

# Get family member status - listen to AMQP (S2)
# [AMQP] *.{familyID}.status

########################## THIS IS SUPPOSE TO BE TOGETHER ############################
# Receive alerts BETWEEN UI AND WEBSOCKET (S1)
# [WebSocket] /get/alerts
# Send status BETWEEN UI AND WEBSOCKET (S1&2)
# [WebSocket] /user/status
########################## THIS IS SUPPOSE TO BE TOGETHER ############################

# Get alerts - listen to AMQP (S1)
# [AMQP] {country}.{city}.alert