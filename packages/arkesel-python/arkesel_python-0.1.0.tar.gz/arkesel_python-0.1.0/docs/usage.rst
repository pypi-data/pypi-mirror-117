=====
Usage
=====

First of all you should ensure that you have an account with Arkesel and hence you do have an API key saved in your .env file / environment.
If you don't have one then you can visit this `link <https://arkesel.com>`_  , create an acccount and login to proceed from there.

To use this Arkesel tool in your project::

    pip instsall arkesel_python


To call classes in your code::

    * from arkesel_python import ArkeselSMS
    * from arkesel_python import SmsInfo 
    * from arkesel_python import ArkeselOtp
    * from arkesel_python import Contacts




#. class ArkeselSMS has the following methods::

       sendSms
       scheduledSms
       webhookSms
       sandBox
       voiceSms
       send_group_sms

#. class ArkeselOTP has the following methods::

       sendOtp
       verifyOtp
   
#. class SmsInfo has the following methods::

       smsBalance 
       smsDetails 

#. class Contacts has the following methods::

        #. create_contact_group:

            create_contact_group(group_name: str):: python
            create_contact_group("TEST"):: python
                
                
        #. add_to_contact_group:

            add_contact_to_group(group_name: str, contacts: array):: python
            add_contact_to_group("TEST" , [{"phone_number":"0XXXXXXXXX"}]):: python
            




Sending Bulk SMS::


    
    def sendBulkText():
        letter = ArkeselSMS()
        print (letter.sendSms("user" , "example text" , ["0XXXXXXXXX"]))
    sendBulkText()

Sending Scheduled Bulk SMS::

    def sendBulkText():
        send = ArkeselSMS()
        print (send.scheduledSms('Trial','just trying this',['0XXXXXXXXX'],"2021-07-01 12:07 PM"))
    sendBulkText()

Sending Bulk SMS With Delivery Webhook::

    def sendWithWebhook():
        send = ArkeselSMS()
        print (send.webhookSms('Trial','just trying this',['0XXXXXXXXX'],"https://aptinc.com/sms/delivery_webhook"))