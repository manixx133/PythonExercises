class pc:
    def __init__(self,processor,ram,hdd):
        self.processor = processor
        self.ram = ram
        self.hdd = hdd
        self.msg = 'PC has processor as '+self.processor+' and ram as '+self.ram
    @property
    def msg_property(self):
        return 'PC has processor as '+self.processor+' and ram as '+self.ram

pc1 = pc('Intel','16GB','500GB')
print(pc1.msg)
print('Change Processor from Intel to AMD and ram from 16GB to 32GB')
pc1.processor = 'AMD'
pc1.ram = '32GB'
print('Without Property Decorator:')
print(pc1.processor)
print(pc1.ram)
print(pc1.msg)
print('With Property Decorator:')
print('After Change:')
print(pc1.processor)
print(pc1.ram)
print(pc1.msg_property)