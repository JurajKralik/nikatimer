import tkinter as tk

def convert_to_latex(expr):
	def parse_fraction(s):
		# Remove outer parentheses if present
		s = s.strip()
		if s.startswith("(") and s.endswith(")"):
			s = s[1:-1]

		# Find top-level '/' not inside parentheses
		level = 0
		for i, c in enumerate(s):
			if c == '(':
				level += 1
			elif c == ')':
				level -= 1
			elif c == '/' and level == 0:
				left = s[:i].strip()
				right = s[i+1:].strip()
				return f"\\frac{{{parse_fraction(left)}}}{{{parse_fraction(right)}}}"

		return s  # No top-level slash found

	latex_core = parse_fraction(expr.strip())
	return f"${latex_core}$"

def on_input_change(event=None):
	input_text = input_box.get("1.0", tk.END).strip()
	if input_text:
		output = convert_to_latex(input_text)
		output_box.delete("1.0", tk.END)
		output_box.insert(tk.END, output)

# GUI setup
root = tk.Tk()
root.title("Fraction to LaTeX Converter")

tk.Label(root, text="Input:").pack()
input_box = tk.Text(root, height=5, width=50)
input_box.pack()
input_box.bind("<KeyRelease>", on_input_change)

tk.Label(root, text="Output (LaTeX):").pack()
output_box = tk.Text(root, height=5, width=50)
output_box.pack()

root.mainloop()
