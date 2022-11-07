# Task 3

# TV controller

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

#     first_channel() - turns on the first channel from the list.
#     last_channel() - turns on the last channel from the list.
#     turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
#     next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
#     previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
#     current_channel() - returns the name of the current channel.
#     is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

 

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and methods described above.



CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:

    def __init__(self, CHANNELS) -> None:
        self.CHANNELS = CHANNELS
        self._current_channel = self.CHANNELS[0]


    def first_channel(self):
        self._current_channel = self.CHANNELS[0]
        return self._current_channel

    
    def last_channel(self):
        self._current_channel = self.CHANNELS[-1]
        return self._current_channel


    def turn_channel(self, channel: int):
        self._current_channel = self.CHANNELS[channel-1]
        return self._current_channel


    def next_channel(self):
        current_index = self.CHANNELS.index(self._current_channel)
        next_index = (current_index + 1) % len(self.CHANNELS)
        self._current_channel = self.CHANNELS[next_index]
        return self._current_channel


    def previous_channel(self):
        current_index = self.CHANNELS.index(self._current_channel)
        next_index = (current_index - 1) % len(self.CHANNELS)
        self._current_channel = self.CHANNELS[next_index]
        return self._current_channel


    def current_channel(self):
        return self._current_channel


    def is_exist(self, key):
        if type(key) == str:
            for channel in self.CHANNELS:
                if channel == key:
                    return 'Yes'
                else:
                    return 'No'
        elif type(key) == int:
            if 0 < key <= len(self.CHANNELS):
                return 'Yes'
            else:
                return 'No'


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"

assert controller.last_channel() == "TV1000"

assert controller.turn_channel(1) == "BBC"

assert controller.next_channel() == "Discovery"

assert controller.previous_channel() == "BBC"

assert controller.current_channel() == "BBC"

assert controller.is_exist(4) == "No"

assert controller.is_exist("BBC") == "Yes"
