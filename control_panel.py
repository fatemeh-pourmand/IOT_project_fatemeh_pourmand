
'''


Notes:
#at the first go to this function and complete it --->> def get_status_in_group ...with for & condition.. 
#pay attention == all_devicess, group_name,print(f"
#now..go to another function -->>  def get_status_in_device_type.= i cread empty Dic then for in all devices (self) after that chose device type and did  key value,finally return status  
        

Comments & questions:

'''

class Device:
    
    def __init__(self,location,group,device_type,device_name):
        self.location=location
        self.group=group
        self.device_type=device_type
        self.device_name=device_name 
        self.status='off'



    def turn_on(self):
        print('Done!!!')
        self.status='on'
        print(f"Done {self.status} successfully")

    def turn_off(self):
        print('off')
        self.status='off'
        print(f"off in '{self.status}' done successfully")
       
        
    def get_status(self):
        if self.status=='on':
            return True
        else:
            return False
        
        
        

class Sensor:
    
    def __init__(self,location,group,sensor_type,sensor_name):
        self.location=location
        self.group=group
        self.sensor_name=sensor_name
        self.sensor_type=sensor_type
                
        
    def read_data(self):
        return 25




class control_panel:
    
    def __init__(self):
        self.groups={}
        
    def create_group(self,group_name):
        if group_name not in self.groups:
            self.groups[group_name]=[]
            print(f'groups {group_name} created !!')
            
        else:
            print('your group name is duplicated')
        
    
    def add_device_to_group(self,group_name,device):
        if group_name in self.groups:
            
        
            self.groups[group_name].append(device)
            # groups['living_room'] -->[]
            print(f'your devic is added to {group_name}')
        else:
            print('you group is not exist....')
        
        
        
        
    def create_device(self,group_name,device_type,device_name):
        
        if group_name in self.groups:
            location='home'
            new_device=Device(location,group_name,device_type,device_name)
            
            self.groups[group_name].append(new_device)
            print(f"Device '{device_name}' of type '{device_type}' successfully appended to group '{group_name}'.")
            
        else:
            print(f"cannot add device. Group'{group_name}' dose not exist.")
        
        
        
        
    def create_multiple_device(self,group_name,device_type,device_number):
        if group_name in self.groups:
            
            for i in range(1,device_number+1):
                dv_name=f'{device_type}_{i}'
                self.create_device(group_name,device_type,dv_name)

            print(f'{device_number} devices created!!')
            
        else:
            
            print('....')
            
            
            
    def get_devices(self,group_name):
        
        devices=self.groups[group_name]
        return devices
        
        
        
    def trun_on_in_group(self,group_name):
        
        if group_name in self.groups:
            
            devices=self.get_devices(group_name)
            
            for device in devices:
                device.turn_on()
            
        else:
            print('....') 
            
            
            
    def turn_off_in_group(self,group_name):
     if group_name in self groups:
        for device in self.groups[group_name]:
            device.turn_off()
        
    
    
    def turn_on_all(self):
        for device in self.devices:
            device.turn_on()
            print('all devices turn on')
    
    def turn_off_all(self):
        for device in self.devices:
            device.turn_of()
            print('all devices turn off')
    
    
    def get_status_in_group(self,group_name): 
        
        for device in self.devices:
            if device.group == group_name:
                print(f"Device {device.name} is {device.status}")

            
    def get_status_in_device_type(self,dvice_type):
        statuse_dict = {}
        for device in self.devices:  
        if device.device_type == device_type: 
            status_dict[device.name] = device.status
    return status-dict
    
    
    #tabe ee bename create_device???
    
    def create_sensor(self):
        pass
    
    def create_multiple_sensor(self):
        pass
    

