# importing required module
import winreg as wrg

# Store PATH of HKEY_LOCAL_MACHINE
PATH = wrg.HKEY_LOCAL_MACHINE

def disable_USB_ports():
	try:
		# Store path in USB_PORT_PATH
		USB_PORT_PATH = wrg.OpenKeyEx(PATH, r"SYSTEM\\CurrentControlSet\\Services\\USBSTOR\\")
		USB_PORT_KEY = wrg.CreateKeyEx(USB_PORT_PATH, "Start")
		
		wrg.SetValueEx(USB_PORT_KEY, "Start", 0, wrg.REG_DWORD, 4)
		if USB_PORT_KEY:
			wrg.CloseKey(USB_PORT_KEY)
			print("Ports Disabled")
	except:
		print("Ports Disable Failed")

def disable_bluetooth():
	try:
		# Store path in BLUETOOTH_PATH
		BLUETOOTH_PATH = wrg.OpenKeyEx(PATH, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ActionCenter\\QuickActions\\All\\SystemSettings_Device_BluetoothQuickAction\\")
		BLUETOOTH_KEY = wrg.CreateKeyEx(BLUETOOTH_PATH, "Type")

		wrg.SetValueEx(BLUETOOTH_KEY, "Type", 0, wrg.REG_DWORD, 1)
		if BLUETOOTH_KEY:
			wrg.CloseKey(BLUETOOTH_KEY)
			print("Bluetooth Disabled")
	except:
		print("Bluetooth Disable Failed")

def disable_command_prompt():
	try:
		# Store path in COMMAND_PROMPT_PATH
		COMMAND_PROMPT_PATH = wrg.OpenKeyEx(PATH, r"Software\\Policies\\Microsoft\\Windows\\System\\")
		COMMAND_PROMPT_KEY = wrg.CreateKeyEx(COMMAND_PROMPT_PATH, "DisableCMD")

		wrg.SetValueEx(COMMAND_PROMPT_KEY, "DisableCMD", 0, wrg.REG_DWORD, 1)
		if COMMAND_PROMPT_KEY:
			wrg.CloseKey(COMMAND_PROMPT_KEY)
			print("Command Prompt Disabled")
	except:
		print("Command Prompt disable Failed")

def disable_facebook():
	try:
		# Store path in WEBSITE_PATH
		WEBSITE_PATH = wrg.OpenKeyEx(PATH, r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\\ZoneMap\\Domains\\")
		WEBSITE_KEY = wrg.CreateKeyEx(WEBSITE_PATH, "http://www.facebook.com")

		wrg.SetValueEx(WEBSITE_KEY, "http://www.facebook.com", 0, wrg.REG_DWORD, 4)
		if WEBSITE_KEY:
			wrg.CloseKey(WEBSITE_KEY)
			print("Facebook disabled")
	except:
		print("Facebook disable Failed")


def main():
	print("Disabling Ports, Bluetooth, Command Prompt")
	disable_USB_ports()
	disable_bluetooth()
	disable_command_prompt()
	disable_facebook()
	print("Ports, Bluetooth, Command Prompt diabled.")

main()