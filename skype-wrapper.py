#!/usr/bin/env python
import subprocess
import os
import shutil
import stat
import re

skype_env = os.environ.copy()
#skype_env["PULSE_LATENCY_MSEC"] = "60"
skype_bin = '/usr/bin/skype'

def is_running(process):
	s = subprocess.Popen(["ps", "axw"], stdout=subprocess.PIPE)
	
	for x in s.stdout:
		if re.search(process, x):
			return True

	return False


if __name__ == '__main__':
	icons_map = [
		('6cbeda8e2c9f56d3ac75ccdf8d282a69', 'loading-1.png'),
		('0972e5fde53a4a87346ebb91c4c2b159', 'loading-2.png'),
		('dad77418071bead905e2dbe605715dcd', 'loading-3.png'),
		('f2fc4a539a7b9553f5b35241d1154e84', 'loading-4.png'),
		
		('37e170fc54e7355d9d298917e74f9ea9', 'online.png'),
		('602c84fa0f4d61c64f770495a500279e', 'away.png'),
		('bd2e3972c2a97520bbabac7e275d7b9f', 'dnd.png'),
		('ad07f7e1479ab81315ec8c6c23e19170', 'invisible.png'),
		('2d1ee5482260fd9cd180b32787792683', 'offline.png'),

		('0fce05395e6040b3fd0838935b3aa115', 'online-message-1.png'),
		('643eb41f209ab21cec8e0016869d77f5', 'away-message-1.png'),
		('42d0fbcc94c821e2232e615577380538', 'dnd-message-1.png'),
		('1c4299179b726cdc6f35079415c591ca', 'invisible-message-1.png'),
		('a1cfc02624e979f3abb9650e1702c70a', 'offline-message-1.png'),

		('c2ee5f08e8df31fd4dcef88f95ed4a16', 'online-message-2.png'),
		('daa1b2b05d5c4ad0617edbae8b4652cd', 'away-message-2.png'),
		('54775fa41d44a47f19cb6520aacdacf4', 'dnd-message-2.png'),
		('7132b01bc26074968e487c1f6bc7e92e', 'invisible-message-2.png'),
		('5c89584aebe7a707fd11439b57dd60f3', 'offline-message-2.png'),

		('aea96408f206d4388540fd1cd3356574', 'online-message-3.png'),
		('d350bfcdb00a5802a8ee236ade74aeaa', 'away-message-3.png'),
		('c39a8b146b7ece25430f0e522db05a3d', 'dnd-message-3.png'),
		('dfae7fc1982010897caf25bf5252f4c5', 'invisible-message-3.png'),
		('4fb7a30c39fb0b95f300952ad4df27dc', 'offline-message-3.png'),

		('af754bab33124c9c4d9c0bbafbdad5a4', 'online-message-4.png'),
		('db908c42e0fc75d6f147f40c58018efe', 'away-message-4.png'),
		('12edeb29a258ad03efea60d284915a5b', 'dnd-message-4.png'),
		('e5ebfdd9dceabe1db3940b5b914b614b', 'invisible-message-4.png'),
		('17a2882e43eba94396d2070600f4a9c7', 'offline-message-4.png'),

		('2ad68f9fa3b206fa4416d357cb824006', 'online-message-5.png'),
		('5768209d6793270698137ed2fa06482a', 'away-message-5.png'),
		('118451255b9deb867a46f1f3f83136b1', 'dnd-message-5.png'),
		('057644540e0d8c2f95510d34ba62d1f5', 'invisible-message-5.png'),
		('7e4f1122b0100d9e72817d3a1b6bcf41', 'offline-message-5.png'),

		('0d96a65d843060dab4836712307a256b', 'online-message-6.png'),
		('0d0cac64aec0e0f871367a6c5b9a0a0a', 'away-message-6.png'),
		('f7ba77ccc5c3e6b18673031845708a42', 'dnd-message-6.png'),
		('cf3964a66e999b9496236d44aba66fa1', 'invisible-message-6.png'),
		('bf2cdd61102d7629699e062ceee3eb6f', 'offline-message-6.png'),

		('460a6dfd3fc7bbd4ca0043fdc15304a2', 'online-message-7.png'),
		('992c516b5d81365691fbd12316ee5289', 'away-message-7.png'),
		('3ede8d0af1863ba806900731f4a422c2', 'dnd-message-7.png'),
		('86623faa12e1d62e147b372326a120b6', 'invisible-message-7.png'),
		('8de9250315c868c51ed6c0404847aedd', 'offline-message-7.png'),

		('47f2365681392e0042137afaa4d3f2a0', 'online-message-8.png'),
		('857e74ec10534f4b330773091490ea53', 'away-message-8.png'),
		('cb8451bfa5891c2f5aba6bd779aa72e3', 'dnd-message-8.png'),
		('5c32c2810a12d44e57b11f0cc08fcd1f', 'invisible-message-8.png'),
		('94f64c1b13a2e45520e6e469a369ff2b', 'offline-message-8.png'),

		('e0a92a2377195909d6437909d9851f53', 'online-message-9.png'),
		('46d4fb1438d466418dae167b2582c58d', 'away-message-9.png'),
		('1f398923152e421ae929499aef839d81', 'dnd-message-9.png'),
		('39a77a303ff1cad03a08c394cf8e3455', 'invisible-message-9.png'),
		('4015bf7d07bdea10086b51c23feaa0b4', 'offline-message-9.png'),

		('4905a21912d8d5803f345d06ab56e88b', 'online-message-10.png'),
		('5928f8a678494eb017181ebb00695682', 'away-message-10.png'),
		('fd56304306a9b229dbdaf4cf7dc4cbc7', 'dnd-message-10.png'),
		('c083094322ffc728a53f83dfe24194de', 'invisible-message-10.png'),
		('287ee46e101cabf27ff0509d79bbf636', 'offline-message-10.png')
	]

	if is_running(skype_bin):
		print 'Skype already running'
		exit(1)

	pid = subprocess.Popen([skype_bin], env=skype_env).pid
	print pid
	
	substr = "sni-qt_skype_{0}".format(pid)

	finished = False
	folder_name = ""

	while not finished:
		for name in os.listdir("/tmp/"):
			if name.startswith(substr):
				folder_name = name
				finished = True

	icons_folder = "/tmp/" + folder_name + "/icons/hicolor/24x24/apps/"
	os.makedirs(icons_folder)

	subst_icons_folder = os.path.dirname(os.path.realpath(__file__)) + '/icons/'

	for (uid, subst_icon) in icons_map:
		skype_icon = icons_folder + 'skype_{0}_{1}.png'.format(pid, uid)
		shutil.copy(subst_icons_folder + subst_icon, skype_icon)
		os.chmod(skype_icon, stat.S_IRUSR)
