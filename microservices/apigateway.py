# Kong API gateway
# Get user
# [GET] /user/{userID}

# Update user
# [PUT] /user/update/{userID}

# Add location
# [POST] /location

# Get all user latest location
# [GET] /location/latest

# Receive alerts
# [WebSocket] /get/alerts

# Get alerts
# [AMQP] {country}.{city}.alert

# Send status
# [WebSocket] /user/status

# Send status
# [POST] /user/status

# Get family status
# [WebSocket] /{familyID}/users/status

# Get member status
# [AMQP] *.{familyID}.status

# Get user status
# [GET] /affected/{disasterID}