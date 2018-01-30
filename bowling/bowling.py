

class BowlingGame(object):
    def __init__(self, total_frames=10):
        self.throws = []
        self.total_frames = total_frames
        self.game_cnt = 0
        self.cur_frame_score = None
        self.extra = 0 # 0, 1, 2
        self.extra_cnt = 0

    def roll(self, pins):
        if self.game_cnt == self.total_frames:
            raise IndexError('The game is completed')
        if not 0 <= pins <= 10:
            raise ValueError('Number of pins should be in [0; 10] range')
        if self.cur_frame_score and self.cur_frame_score + pins > 10:
            raise ValueError('Frame score cannot be more than 10')

        if not self.extra and self.game_cnt + 1 == self.total_frames:
            if pins == 10:
                self.extra = self.extra_cnt = 2
            elif self.cur_frame_score is not None and self.cur_frame_score + pins == 10:
                self.extra = self.extra_cnt = 1
                self.cur_frame_score = None
            elif self.cur_frame_score is None:
                self.cur_frame_score = pins
            else:
                self.game_cnt += 1

        elif self.extra_cnt:
            if self.extra_cnt == 2 and pins != 10:
                self.cur_frame_score = pins

            self.extra_cnt -= 1
            if self.extra_cnt == 0:
                self.game_cnt += 1

        else:
            if pins == 10:
                self.game_cnt += 1
            else:
                if self.cur_frame_score is None:
                    self.cur_frame_score = pins
                else:
                    self.game_cnt += 1
                    self.cur_frame_score = None

        self.throws.append(pins)

    def score(self):

        if self.game_cnt < self.total_frames:
            raise IndexError('Incomplete game can\'t be scored')

        throws = self.throws.copy()
        result = 0

        while throws[:-self.extra if self.extra else len(throws)]:
            pins = throws.pop(0)
            if pins == 10:
                result += 10 + throws[0] + throws[1]
                if len(throws) == 2:
                    throws = []
            elif pins + throws[0] == 10:
                result += 10 + throws[1]
                throws.pop(0)
            else:
                result += pins + throws.pop(0)

        return result
