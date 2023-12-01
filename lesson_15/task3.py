# # TV controller

# # Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# # first_channel() - turns on the first channel from the list.
# # last_channel() - turns on the last channel from the list.
# # turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# # next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# # previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# # current_channel() - returns the name of the current channel.
# # exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

# # The default channel turned on before all commands is №1.

# # Your task is to create the TVController class and methods described above.

class TVController:
    
    def __init__(self,channels):
        self.channels = channels
        self.current_channel = channels[0]

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1] 

    def turn_channel(self, n):
        self.current_channel = self.channels[n-1]
        return self.current_channel

    def next_channel(self):
        i = self.channels.index(self.current_channel)
        if i < len(self.channels) - 1:
            self.current_channel = self.channels[i + 1] 
        else:
            self.current_channel = self.channels[0]
        return self.current_channel

    def previous_channel(self):
        i = self.channels.index(self.current_channel)
        if i > 0:
            self.current_channel = self.channels[i -1]
        else:
            self.current_channel = self.channels[-1]
        return self.current_channel

    def is_current_channel(self):
        return self.current_channel

    def exists(self, channel):
        if type(channel) == int:
            if channel <= len(self.channels) and channel > 0:
                return "Yes"
            else:
                return "No"
        elif type(channel) == str:
            if channel in self.channels:
                return "Yes"
            else:
                return "No"  

channels = ['BBC', 'Discovery', 'TV1000'] 
controller = TVController(channels)   
print(controller.first_channel() == "BBC") 
print(controller.last_channel() == "TV1000") 
print(controller.turn_channel(1) == "BBC") 
print(controller.next_channel() == "Discovery") 
print(controller.previous_channel() == "BBC") 
print(controller.is_current_channel() == "BBC") 
print(controller.exists(4) == "No") 
print(controller.exists("BBC") == "Yes") 




