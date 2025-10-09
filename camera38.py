#
#smart home system=control=door,lapms,lightsand now camera
#('device_type='camera) every devive has a =place,group,kind,name,pin
#when said camera use 38 =mean pin38
#lights & doors connect to pin 17,27 ,camera??? i dont have anything
#i need a condition
#i realized devices has ID or special pin with special condition and id number
#now we going to functions turn_on, turn_off


'''

APM:
salam , camera roye 38 gharar gereft va dorost hast , moafagh bashiid

'''





class Device:
    
    def __init__(self,location,group,device_type,device_name,pin):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'
        
        
        #sherkat dade beman
        self.mqtt_broker='jasdhash'
        self.port=37362  
        
        #on dastgahe pini --> 
        self.mqtt_client=pin
        
        self.connect_mqtt()
        self.setup_gpio()
        



    def connect_mqtt(self):
        mqtt.connect(self.mqtt_broker,self.port)
        
        
    def setup_gpio(self):
        
        if self.device_type=='lights':
            GPIO.setup(17,GPIO.OUT)
            
        elif self.device_type=='doors':
            GPIO.setup(27,GPIO.OUT)

        elif self.device_type=='camera' :
            GPIO.setup(38,GPIO.OUT)
            

    def turn_on(self):
        print('Done!!!')
        self.status='on'
        #oon devicer --> SHERKAT vasl bshe --> dastoopr bde --> sherkate b oon lampe vasl bshe
        #va oon lamp baram 'ROSHAN' kone
        mqtt.publish(self.mqtt_client,self.device_name,'TURN ON')
        
        

    def turn_off(self):
        print('off')
        self.status='off'
        #bayad inja bnvis-->sherkate begam agah in device 
        #shekrat elamp --> 'Khamoosh' kone
        mqtt.publish(self.mqtt_client,self.device_name,'TURN OFF')

        
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
camera1 = Device('home', 'living_room', 'security_cam', 'pin_38')

a1=Device('home','room','lights','lamps1001','w328376231863816326216')

camera1.turn_on()

camera1.turn_off()
