# general setup
number_of_expanders=8

#MCP setup parameters
ports=16
pin_base = 65
i2c_addr = 0x20

# create config file
expander_cfg=[]

print (type(i2c_addr))

for n in range(0,number_of_expanders):
    (next_pin_base,next_i2c_addr) = (pin_base+n*ports,i2c_addr+n)
    #print (next_pin_base,next_i2c_addr)
    expander_cfg.append((next_pin_base,hex(next_i2c_addr)))
    #print (type(next_i2c_addr))
print (expander_cfg)


# available configurations
expander_config = [(65,0x20),(81,0x21), (97,0x22), (113,0x23), (129,0x24), (145,0x25), (161,0x26), (177,0x27)]

# 16 pins for one expander
pins = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]


'''
wiringpi2.wiringPiSetup()

for config in expander_config:
	wiringpi2.mcp23017Setup(config)


for pin in pins:
	wiringpi2.pinMode(pin,1)
	wiringpi2.digitalWrite(pin,1)
'''