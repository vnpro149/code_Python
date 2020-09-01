from nornir import InitNornir

nr = InitNornir('config.yml')

from nornir.plugins.tasks.networking import netmiko_send_config

from nornir.plugins.functions.text import print_result

result = nr.run(netmiko_send_config, config_commands=["int loop 10","ip add 10.10.10.10 255.255.255.0"])

print_result(result)
