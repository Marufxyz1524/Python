class Phone:
    price = 6000
    brand = 'Apple'
    color = ['Blue','Orange','Black']
    features = ['camera','AiLearn','video']

    def call(self):
        print("Calling one person")

    def send_sms(self,phone,sms):
        text  = f'send to {phone} note {sms}: '
        return text 
my_phone = Phone()
print(my_phone.color)
result = my_phone.send_sms(179276100,'I forgot to messge you')    
print(result)

