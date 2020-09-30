from typing import Dict, List


class Command:
	@staticmethod
	def parse(schema: Dict, input: List[str]) -> Dict:
		"""
		Parses command input to separate elements
		:param schema: dict of optional flags and kwargs {title: str, short: str}
		:param input: list of strings for the command
		:return: Dict of args, flags and kwargs
		"""
		match = {
			"flags": schema["flags"] if "flags" in schema else [],
			"kwargs": schema["kwargs"] if "kwargs" in schema else [],
		}
		# TODO: consider how this is not currently checking the validity of flags and kwargs
		# NOTE: would it be worth making a CommandSchema class or something like that?

		result = {
			"args": [],
			"flags": [],
			"kwargs": {},
		}

		# TODO: gobble elements to fill the above
		arg_list = iter(input)

		# Iterate Elements
		while(True):
			entry = next(arg_list, None)

			# List End
			if entry is None:
				break

			# Parse Named
			if entry.startswith("--"):
				# TODO: find title in match
				pass

			# Parse Abbreviated
			elif entry.startswith("-"):
				# TODO: find short in match
				pass

			# Positional Argument
			else:
				result["args"].append(entry)

		return result
		# TODO: potentially raises if kwarg key is not followed by value
