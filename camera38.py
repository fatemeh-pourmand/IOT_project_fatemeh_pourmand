salam ostad camera 38 ro suport kone yani ham class mkhaid ham function? 
exmple:lapm,door,home,light, ...ye camera ham mikhaid bale??
ya dar class drvice function camera biaram ke 38 ro support kone?
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
        
        
#a1=..... (class --> device az tarighe ketabkhone)

a1=Device('home','room','lights','lamps1001','w328376231863816326216')

a1.turn_on()

a1.turn_off()
