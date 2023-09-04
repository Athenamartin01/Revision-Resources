
ansible host-pattern -m <module> -a <module args>

ansible-doc -l 
<!-- list all modules--!>

useful modules:
- ansible.builtin.shell
- ansible.builtin.command
- ansible.builtin.apt
- ansible.builtin.systemd
- ansible.builtin.systemd_service
- ansible.builtin.file
- ansible.builtin.debug

ansible 127.0.0.1  -m apt -a "name=nginx start-present" -b
<!-- run nginx -->

ansible localhost -m apt ansible.builtin.file -a "path=/home/ubuntu/ansidir state=directory"
<!-- create directory -->

ansible 127.0.0.1 -m ansible.builtin.command -a "mkdir /fome/ubuntu/ansicmddir"  <not idempodent>

ansible localhost -m ansible.builtin.systemd_service -a "name=nginx state=restarted" -b
<!-- restart nginx -->