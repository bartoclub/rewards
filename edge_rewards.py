VK_CODE = {'backspace':0x08, 'tab':0x09, 'clear':0x0C, 'enter':0x0D, 'shift':0x10, 'ctrl':0x11, 'alt':0x12, 'pause':0x13, 'caps_lock':0x14, 'esc':0x1B, 'spacebar':0x20, ' ':0x20, 'page_up':0x21, 'page_down':0x22, 'end':0x23, 'home':0x24, 'left_arrow':0x25, 'up_arrow':0x26, 'right_arrow':0x27, 'down_arrow':0x28, 'select':0x29, 'print':0x2A, 'execute':0x2B, 'print_screen':0x2C, 'ins':0x2D, 'del':0x2E, 'help':0x2F, '0':0x30, '1':0x31, '2':0x32, '3':0x33, '4':0x34, '5':0x35, '6':0x36, '7':0x37, '8':0x38, '9':0x39, 'a':0x41, 'b':0x42, 'c':0x43, 'd':0x44, 'e':0x45, 'f':0x46, 'g':0x47, 'h':0x48, 'i':0x49, 'j':0x4A, 'k':0x4B, 'l':0x4C, 'm':0x4D, 'n':0x4E, 'o':0x4F, 'p':0x50, 'q':0x51, 'r':0x52, 's':0x53, 't':0x54, 'u':0x55, 'v':0x56, 'w':0x57, 'x':0x58, 'y':0x59, 'z':0x5A, 'win':0x5B, 'numpad_0':0x60, 'numpad_1':0x61, 'numpad_2':0x62, 'numpad_3':0x63, 'numpad_4':0x64, 'numpad_5':0x65, 'numpad_6':0x66, 'numpad_7':0x67, 'numpad_8':0x68, 'numpad_9':0x69, 'multiply_key':0x6A, 'add_key':0x6B, 'separator_key':0x6C, 'subtract_key':0x6D, 'decimal_key':0x6E, 'divide_key':0x6F, 'F1':0x70, 'F2':0x71, 'F3':0x72, 'F4':0x73, 'F5':0x74, 'F6':0x75, 'F7':0x76, 'F8':0x77, 'F9':0x78, 'F10':0x79, 'F11':0x7A, 'F12':0x7B, 'F13':0x7C, 'F14':0x7D, 'F15':0x7E, 'F16':0x7F, 'F17':0x80, 'F18':0x81, 'F19':0x82, 'F20':0x83, 'F21':0x84, 'F22':0x85, 'F23':0x86, 'F24':0x87, 'num_lock':0x90, 'scroll_lock':0x91, 'left_shift':0xA0, 'right_shift ':0xA1, 'left_control':0xA2, 'right_control':0xA3, 'left_menu':0xA4, 'right_menu':0xA5, 'browser_back':0xA6, 'browser_forward':0xA7, 'browser_refresh':0xA8, 'browser_stop':0xA9, 'browser_search':0xAA, 'browser_favorites':0xAB, 'browser_start_and_home':0xAC, 'volume_mute':0xAD, 'volume_Down':0xAE, 'volume_up':0xAF, 'next_track':0xB0, 'previous_track':0xB1, 'stop_media':0xB2, 'play/pause_media':0xB3, 'start_mail':0xB4, 'select_media':0xB5, 'start_application_1':0xB6, 'start_application_2':0xB7, 'attn_key':0xF6, 'crsel_key':0xF7, 'exsel_key':0xF8, 'play_key':0xFA, 'zoom_key':0xFB, 'clear_key':0xFE, '+':0xBB, ',':0xBC, '-':0xBD, '.':0xBE, '/':0xBF, '`':0xC0, ';':0xBA, '[':0xDB, '\\':0xDC, ']':0xDD, "'":0xDE, '`':0xC0, 0:0x30, 1:0x31, 2:0x32, 3:0x33, 4:0x34, 5:0x35, 6:0x36, 7:0x37, 8:0x38, 9:0x39}
WORDS = ["aback", "abaft", "ably", "aboon", "about", "above", "abuse", "accel", "access", "action", "acute", "admit", "adopt", "adown", "adult", "afar", "afoot", "afore", "afoul", "after", "again", "agape", "agent", "agogo", "agone", "agree", "ahead", "ahem", "ahoy", "ahull", "ajax", "alas", "alife", "alike", "aline", "alive", "allow", "aloft", "alone", "along", "aloof", "aloud", "alter", "always", "amen", "amid", "amiss", "amply", "amuck", "anew", "anger", "angry", "anti", "apace", "apart", "apple", "apply", "aptly", "apud", "arear", "argue", "arise", "around", "aside", "askew", "atop", "august", "author", "avoid", "award", "aware", "away", "awful", "back", "badly", "bally", "bang", "basic", "basis", "beach", "become", "before", "begin", "below", "better", "birth", "black", "blah", "blame", "blind", "block", "blood", "board", "bout", "brain", "brave", "bread", "break", "brief", "bring", "broad", "brown", "browse", "build", "burst", "buyer", "called", "canada", "canny", "carry", "catch", "cause", "center", "chain", "chair", "change", "cheap", "check", "chest", "chez", "chief", "child", "china", "ciao", "civil", "claim", "class", "clean", "clear", "climb", "clock", "close", "coach", "coast", "come", "common", "count", "county", "course", "court", "cover", "coyly", "crazy", "cream", "create", "credit", "crime", "cross", "crowd", "crown", "crud", "cycle", "dahn", "daily", "damn", "dance", "darn", "dead", "death", "deep", "depth", "design", "dimly", "direct", "dirty", "ditto", "doon", "doubt", "down", "draft", "drama", "dream", "dress", "drily", "drink", "drive", "dryly", "dully", "duly", "during", "early", "earth", "easy", "egad", "eina", "else", "empty", "enemy", "energy", "enjoy", "enter", "entry", "equal", "error", "estate", "even", "event", "events", "ever", "exact", "exist", "extra", "fact", "faint", "fair", "faith", "false", "family", "fast", "fatly", "fault", "feyly", "field", "fifth", "fight", "final", "first", "fitly", "flat", "flip", "floor", "focus", "force", "fore", "format", "forte", "forth", "forums", "frame", "france", "frank", "fresh", "friend", "from", "front", "fruit", "full", "fully", "funny", "future", "gaily", "gain", "garden", "gayly", "giant", "glass", "godly", "good", "gosh", "grand", "grant", "grass", "great", "green", "gross", "group", "groups", "guess", "guide", "half", "haply", "happy", "hard", "harsh", "having", "health", "heart", "heavy", "heck", "hell", "hella", "hence", "henry", "here", "high", "hist", "hiya", "hmmm", "hmph", "home", "honk", "horse", "hotel", "hotels", "hotly", "house", "human", "hunh", "icily", "ideal", "idly", "image", "images", "imply", "index", "infra", "inner", "input", "intl.", "into", "island", "issue", "issues", "japan", "jeez", "jildi", "jinx", "joint", "jolly", "jones", "judge", "just", "knife", "large", "late", "latest", "laugh", "laura", "laxly", "layer", "learn", "leave", "legal", "lento", "lets", "level", "lewis", "light", "like", "limit", "listed", "little", "live", "living", "local", "london", "long", "loose", "lord", "loud", "lowly", "lucky", "lunch", "madly", "magic", "major", "making", "mang", "march", "market", "marry", "match", "maybe", "member", "memory", "meow", "metal", "minor", "mobile", "model", "money", "mong", "month", "months", "moral", "motor", "mouth", "movies", "much", "music", "mwah", "naked", "nasty", "naval", "near", "never", "newly", "nice", "nigh", "night", "nobly", "noise", "nome", "north", "notice", "novel", "number", "nurse", "nyet", "occur", "oddly", "offa", "offer", "offers", "office", "often", "okay", "once", "online", "only", "onto", "oops", "order", "other", "others", "ouch", "ought", "outa", "outer", "over", "owner", "panel", "paper", "part", "party", "past", "peace", "people", "period", "person", "peter", "phase", "phew", "phone", "photos", "phut", "piano", "piece", "pilot", "pitch", "place", "plain", "plane", "plant", "plate", "please", "plonk", "plumb", "point", "policy", "poof", "pooh", "post", "posted", "pound", "power", "press", "price", "prices", "pride", "prime", "prior", "prize", "proof", "proud", "prove", "public", "pugh", "queen", "queer", "quick", "quiet", "quite", "rabbit", "racial", "racing", "racism", "racist", "radio", "radius", "raise", "raised", "raises", "ramen", "random", "range", "ranged", "ranger", "ranges", "ranked", "rapid", "rarely", "rather", "rating", "ratio", "ratios", "reach", "reader", "ready", "real", "really", "reason", "rebels", "recall", "recent", "recipe", "record", "redeem", "redly", "reduce", "refer", "refers", "refine", "reform", "refuge", "refund", "refuse", "regain", "regard", "regime", "region", "regret", "reject", "relate", "relax", "relied", "relief", "relies", "remain", "remedy", "remind", "remote", "remove", "render", "rental", "rented", "repair", "repeat", "reply", "report", "rescue", "reside", "resist", "resort", "result", "resume", "retail", "retain", "retire", "return", "reveal", "review", "reward", "right", "rights", "river", "roman", "rough", "round", "route", "royal", "rugby", "rural", "sadly", "safety", "save", "scale", "scene", "school", "scope", "score", "search", "second", "secus", "select", "seller", "selly", "sense", "series", "serve", "server", "shall", "shape", "share", "sharp", "sheep", "sheer", "sheet", "shift", "shily", "shirt", "shock", "shoo", "shoot", "short", "should", "shyly", "sight", "silly", "simon", "since", "single", "sixth", "skill", "sleek", "sleep", "slow", "slyly", "small", "smart", "smile", "smith", "smoke", "snap", "so-so", "social", "solid", "solo", "solve", "soon", "sorry", "sound", "source", "south", "space", "spang", "spare", "speak", "speed", "spend", "spite", "split", "sport", "sports", "squad", "srsly", "staff", "stage", "stand", "stark", "start", "state", "states", "status", "steam", "steel", "steep", "stick", "still", "stock", "stone", "stop", "store", "stores", "stour", "street", "study", "stuff", "style", "sugar", "super", "sure", "sweet", "system", "table", "tally", "tanto", "tara", "taste", "teach", "terry", "than", "thank", "that", "theme", "then", "there", "thick", "thing", "things", "think", "third", "this", "thread", "thro", "throw", "thru", "thus", "tight", "till", "title", "today", "tomoz", "total", "touch", "tough", "tower", "track", "trade", "train", "travel", "treat", "trend", "trial", "truly", "trust", "truth", "twice", "uncle", "under", "union", "united", "unity", "unto", "upon", "upper", "upset", "urban", "urgh", "usual", "utter", "vague", "valid", "value", "verry", "very", "vice", "video", "visit", "vital", "voice", "wall", "waly", "wanly", "waste", "watch", "water", "wetly", "wham", "when", "where", "while", "white", "whiz", "whoa", "whole", "wide", "window", "with", "within", "woman", "word", "world", "worry", "would", "write", "wrong", "young", "youth", "yuck"]

import sys
import time
import random
import win32api
import win32con
import win32gui
import win32process

class RewardsPlayer():
	def __init__(self):
		self.browser_title = "original"
		self.browser_hwnds = []
		self.done = []
	
	def callback(self, hwnd, extra):
		if win32gui.IsWindowVisible(hwnd):
			window_title = win32gui.GetWindowText(hwnd)
			if "Edge" in window_title:
				self.browser_hwnds += [hwnd]

	def get_browser_to_front(self, window):
		win32gui.SetForegroundWindow(window)
		time.sleep(0.5)
	
	def move_cursor_randomly(self, max_distance):
		distance = random.randint(0, max_distance)
		pos = win32api.GetCursorPos()
		x_dir = random.uniform(-1, 1)
		y_dir = random.uniform(-1, 1)
		for move in range(distance):
			new_pos = (pos[0]+int(move*x_dir), pos[1]+int(move*y_dir))
			win32api.SetCursorPos(new_pos)
			time.sleep(0.0001)
	
	def key_down(self, key):
		win32api.keybd_event(VK_CODE[key], 0, 0, 0)
		time.sleep(0.05)
	
	def key_up(self, key):
		win32api.keybd_event(VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
		time.sleep(0.05)
	
	def key_press(self, key):
		try:
			if key == ' ':
				time.sleep(0.2)
			self.key_down(key)
			self.key_up(key)
		except Exception as e:
			time.sleep(0.1)
	
	def select_address_bar(self):
		self.key_down('ctrl')
		self.key_press('l')
		self.key_up('ctrl')
	
	def check_esc_and_close(self):		
		if win32api.GetAsyncKeyState(VK_CODE['esc']):
			sys.exit()
	
	def get_new_word(self):
		text = None
		while (text is None):
			random_number = random.randint(0, len(WORDS)-1)
			text = WORDS[random_number]
			
			if text not in self.done:
				self.done += [text]
				break
		
		return text

	def search_terms(self):
		win32gui.EnumWindows(self.callback, None)
		if len(self.browser_hwnds) == 0:
			sys.exit()

		words_count = 40
		for word_index in range(words_count):
			for browser_hwnd in self.browser_hwnds:
				player.get_browser_to_front(browser_hwnd)
				self.select_address_bar()
				self.key_press('backspace')
				if word_index == words_count-1:
					text = "rewards.bing.com/pointsbreakdown"
				else:
					text = self.get_new_word()
				for index, character in enumerate(text):
					self.check_esc_and_close()
					self.key_press(character)
				self.key_press('del')
				self.key_press('enter')

			if random.randint(0, 500) < 250:
				player.move_cursor_randomly(200)
			else:
				time.sleep(0.5)

	def open_browser(self, count):
		self.key_down('win')
		self.key_press(count+1)
		self.key_up('win')
		time.sleep(5)
		self.key_down('ctrl')
		self.key_press('n')
		self.key_up('ctrl')
		time.sleep(5)
		self.key_down('ctrl')
		self.key_down('shift')
		self.key_press('i')
		self.key_up('shift')
		self.key_up('ctrl')
		time.sleep(5)
	
	def open_windows(self):
		for index in range(1):
			self.open_browser(index)

if __name__ == "__main__":
	player = RewardsPlayer()
	player.open_windows()
	player.search_terms()
