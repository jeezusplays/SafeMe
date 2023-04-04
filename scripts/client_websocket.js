function connectToWebSocket() {
    // Create a WebSocket object
    const socket = new WebSocket('ws://localhost/ws');
  
    // Event listener for when the WebSocket connection is opened
    socket.addEventListener('open', function (event) {
      console.log('WebSocket connection is now open');
    });
  
    // Event listener for when a message is received from the WebSocket server
    socket.addEventListener('message', function (event) {
      console.log('Received message from WebSocket server:', event.data);
    });
  
    // Event listener for when the WebSocket connection is closed
    socket.addEventListener('close', function (event) {
      console.log('WebSocket connection has been closed');
    });
  
    // Event listener for when there is an error with the WebSocket connection
    socket.addEventListener('error', function (event) {
      console.error('WebSocket connection error:', event);
    });
  
    // Function to send a message to the WebSocket
    function sendMessage(message) {
      if (socket.readyState === WebSocket.OPEN) {
        socket.send(message);
        console.log('Sent message to WebSocket server:', message);
      } else {
        console.error('WebSocket connection is not open. Cannot send message.');
      }
    }
  
    // Return the WebSocket object and sendMessage function as an object
    return {
      socket: socket,
      sendMessage: sendMessage
    };
  }