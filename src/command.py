import sys

class TerminalCommand:

	def __construct(name):
		self.name = name
		self.argument_list = []
		self.option_list = []

	def parse_args(args):
		options = []
		values = []
		args_list = iter(args)
		next(args_list)
		for arg in args_list:
			#if arg starts with dash
			# append to flags
		return (options, values)