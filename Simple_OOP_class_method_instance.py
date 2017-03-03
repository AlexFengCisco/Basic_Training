'''
Created on Mar 2, 2017

@author: AlexFeng
'''
from types import MethodType

#-----a parent class---------------------------------
class Device(object):
   
    def __init__(self,mgt_ip_address,Host_name,):
        self.mgt_ip_address=mgt_ip_address
        self.host_name=Host_name
               
    def get_host_name(self):
        print self.host_name
        
    def get_mgt_ip_address(self):
        print self.mgt_ip_address
#-----a child class to demo inheritance-----------------        
class Switch(Device):
    def __init__(self,mgt_ip_address,Host_name,switch_mode):
        
        Device.__init__(self,mgt_ip_address,Host_name)  #------child class call parent class construction 
        self.switch_mode=switch_mode
     
    def get_switch_mode(self):
        print self.switch_mode
        
class Router(Device):
    def __init__(self,mgt_ip_address,Host_name,POS_support):
        Device.__init__(self,mgt_ip_address,Host_name)
        self.POS_support=POS_support
    def get_POS_support(self):
        print self.POS_support

#----------a grand son class to demo polymorphism  --------       
class V_Router(Router):
    def __init__(self,mgt_ip_address,Host_name,POS_support):
        Device.__init__(self,mgt_ip_address,Host_name)
        self.POS_support=POS_support
    def get_POS_support(self):
        print "Don't waste time , this is a virtual Router"

#------------------add a method to class Router , not for a real instance
def set_loop_back(self,loop_back_address):
    self.loop_back_address=loop_back_address
    
Device.set_loop_back=MethodType(set_loop_back,None,Device)

R1=Router('192.168.1.1','R1',"support")
R2=Router('192.168.1.2','R2',"not support")
R3=V_Router('192.168.1.4','R3',"support")

R1.get_host_name()
R2.get_mgt_ip_address()
R2.get_POS_support()
R3.get_POS_support()

R1.host_name='RR1'
R1.get_host_name()   

SW1=Switch('192.168.1.3','SW1','L2')
SW1.get_host_name()
SW1.get_switch_mode()

print dir(Device)
print dir(Switch)
print dir(SW1)
print dir(R2)
print SW1.host_name
print SW1.__doc__

SW1.set_loop_back('1.1.1.1')
print SW1.loop_back_address

print isinstance(R1,Router) 
print issubclass(Router, Device)
print isinstance(Router,Device) 