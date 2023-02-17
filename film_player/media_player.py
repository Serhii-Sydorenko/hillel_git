import time

class Player:

    def switch_state(self):
        if self.state == "play":
            self.state = "pause"
            self.save_last_time()
        elif self.state == "pause":
            self.state = "play"
            self.start_time = time.time()
        else:
            self.state = "stop"
            self.save_last_time()

    def change_quality(self):
        user_quality = input("Quality (720p, 1080p): ")
        self.quality = user_quality

    def switch_subtitles(self):
        if not self.subtitles:
            self.subtitles = True
        elif self.subtitles:
            self.subtitles = False

    def save_last_time(self):
        if not self.last_time:
            self.last_time = time.time() - self.start_time
        elif self.last_time:
            self.last_time += (time.time - self.start_time)

    def close_player(self):
        self.state = "stop"
        self.save_last_time()