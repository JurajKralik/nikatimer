import tkinter as tk

class CountdownApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Veronka Timer")
		self.root.geometry("250x80")
		self.root.attributes("-topmost", True)
		self.root.attributes("-toolwindow", True)  # Windows only

		self.timer_running = False
		self.initial_time = 0
		self.remaining_time = 0
		self.time_inputs_visible = False

		# Timer + buttons frame (horizontal)
		top_frame = tk.Frame(root)
		top_frame.pack(pady=5)

		self.label = tk.Label(top_frame, text="00:00", font=("Helvetica", 20), width=5)
		self.label.pack(side=tk.LEFT, padx=5)

		self.start_stop_btn = tk.Button(top_frame, text="Start", command=self.toggle_timer, width=6)
		self.start_stop_btn.pack(side=tk.LEFT, padx=2)

		self.reset_btn = tk.Button(top_frame, text="Reset", command=self.reset_timer, width=6)
		self.reset_btn.pack(side=tk.LEFT, padx=2)

		self.set_btn = tk.Button(top_frame, text="Set", command=self.toggle_inputs, width=6)
		self.set_btn.pack(side=tk.LEFT, padx=2)

		# Time input frame (below)
		self.input_frame = tk.Frame(root)

		tk.Label(self.input_frame, text="Min:").grid(row=0, column=0)
		self.minutes_entry = tk.Entry(self.input_frame, width=4)
		self.minutes_entry.insert(0, "0")
		self.minutes_entry.grid(row=0, column=1, padx=(0, 10))

		tk.Label(self.input_frame, text="Sec:").grid(row=0, column=2)
		self.seconds_entry = tk.Entry(self.input_frame, width=4)
		self.seconds_entry.insert(0, "30")
		self.seconds_entry.grid(row=0, column=3)

		self.set_timer()  # Initialize with default

	def toggle_inputs(self):
		if self.time_inputs_visible:
			self.input_frame.pack_forget()
			self.set_timer()
			self.time_inputs_visible = False
		else:
			self.input_frame.pack(pady=2)
			self.time_inputs_visible = True

	def set_timer(self):
		try:
			minutes = int(self.minutes_entry.get())
			seconds = int(self.seconds_entry.get())
			total = max(0, minutes * 60 + seconds)
			self.initial_time = total
			self.remaining_time = total
			self.update_display()
		except ValueError:
			self.label.config(text="Err")

	def toggle_timer(self):
		if not self.timer_running:
			if self.remaining_time <= 0:
				self.set_timer()
			self.timer_running = True
			self.set_btn.pack_forget()
			self.reset_btn.pack_forget()
			self.input_frame.pack_forget()
			self.time_inputs_visible = False
			self.start_stop_btn.config(text="Stop")
			self.update_timer()
		else:
			self.timer_running = False
			self.start_stop_btn.config(text="Start")
			self.reset_btn.pack(side=tk.LEFT, padx=2)
			self.set_btn.pack(side=tk.LEFT, padx=2)

	def reset_timer(self):
		self.remaining_time = self.initial_time
		self.update_display()
		self.timer_running = False
		self.start_stop_btn.config(text="Start")

	def update_timer(self):
		if self.timer_running and self.remaining_time > 0:
			self.remaining_time -= 1
			self.update_display()
			self.root.after(1000, self.update_timer)
		elif self.remaining_time == 0:
			self.label.config(text="Hotovó!")
			self.root.bell()
			self.timer_running = False
			self.start_stop_btn.config(text="Start")
			self.reset_btn.pack(side=tk.LEFT, padx=2)
			self.set_btn.pack(side=tk.LEFT, padx=2)

	def update_display(self):
		mins, secs = divmod(self.remaining_time, 60)
		self.label.config(text=f"{mins:02}:{secs:02}")

if __name__ == "__main__":
	root = tk.Tk()
	app = CountdownApp(root)
	root.mainloop()
