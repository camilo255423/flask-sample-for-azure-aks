from azure.servicebus import QueueClient, Message

CONNECTION = 'Endpoint=sb://YOUR_QUEUE_STRING'
# Create the QueueClient
queue_client = QueueClient.from_connection_string(CONNECTION, "taskqueue")

# Send a test message to the queue

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/send/<msg>')
def show_user(msg):
  message = Message(msg)
  queue_client.send(message)	
  return 'Message Sent: %s' % message

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
