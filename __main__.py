 # pastebuddy: Quickly create pastes from your device's clipboard using the pinnwand API
 # Copyright (C) 2021 David Schultz <me@zpld.me>
 # 
 # This program is free software: you can redistribute it and/or modify  
 # it under the terms of the GNU General Public License as published by  
 # the Free Software Foundation, version 3.
 #
 # This program is distributed in the hope that it will be useful, but 
 # WITHOUT ANY WARRANTY; without even the implied warranty of 
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
 # General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License 
 # along with this program. If not, see <http://www.gnu.org/licenses/>.
 #

import requests
import clipboard

if __name__ == "__main__":
	data = requests.post(
		"https://bpaste.net/api/v1/paste", 
		json={
				"expiry": "1day", 
				"files": [
					{
						"lexer": "text",
						"content": clipboard.paste()
					}
				]
		}).json()

	try:
		print(f"Paste complete! View paste: {data['link']} Remove paste: {data['removal']}")
	except KeyError:
		print("An error occured")
		print(f"Response from server: {data}")