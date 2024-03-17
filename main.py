from ultralytics import YOLO
from twilio.rest import Client

# Twilio credentials
account_sid = 'AC73bd2bb7f676aa89b86f607a6494dc65'
auth_token = '2e048ead2dc1f607a1de7c528be0d6ec'
twilio_phone_number = '+16106283400'
recipient_phone_number = '+916380442011'

def send_notification():
    """
    Send a notification message using Twilio.
    """
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="An incident has been detected. Please check the surveillance footage.",
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print("Notification sent:", message.sid)

def process_predictions(result, snatch_threshold=3):

    if isinstance(result, list):
        print("Error: Unexpected format of result object.")
        return
    
    # Check if snatchings occurred
    snatchings = len(result.pred)

    print(snatchings,"hello")
    
    # Send notification if snatchings exceed the threshold
    if snatchings > 3:
        send_notification()

def main():
    # Initialize YOLO model
    model = YOLO("our_model.pt")

    # Predict on image source
    result = model.predict(source="E:\iiitdm\WhatsApp Image 2024-03-16 at 08.07.13_4e0611c1.jpg", show=False)

    # Process the predictions
    process_predictions(result)

if __name__ == "__main__":
    main()
