

import json


class FallingrainPipeline:
	
	def process_item(self, item, spider):
		print(json.dumps(item, indent=1))
		return item
