# Ansible-Playbooks

1.) How to Run Ansible playbooks

# ansible-playbook playbook.yml 

2.) To limit the execution to a single host or group of hosts

# ansible-playbook -l host_or_group playbook.yml 

3.if you want a different SSH user to connect to the remote server, you can include the argument -u 

# ansible-playbook -l host_or_group playbook.yml -u remote-user
