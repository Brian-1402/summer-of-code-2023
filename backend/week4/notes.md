```
mailto:ee1211108@iitd.ac.in
subject=DevClub Summer of Code 2022: Domain Name Request
body=
Name:
Entry Number:
GitHub Username:
PublicIP Address:
```

## Setting up Azure

### Creating account

- Went to [Azure student account section](https://azure.microsoft.com/en-in/free/students/), and using IITD credentials, for me they asked card details. this was quite the headache cost most of the cards I had were debit cards and apparently they won't accept that even though "debit and credit cards" are mentioned there. So finally got it working by using the only credit card I had.

### Creating VM

- This was slightly tense coz there were a LOT of settings to put when making the VM. In the end, chose appropriate values, saved the private key, and all set up.

### Connecting to VM

- The command for ssh connecting is `ssh -i <ssh_key_path> <username>@<IP_address>`.

- Some issues were there tho. When initially connecting, it shows the HOST fingerprint, and [we're supposed](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/ssh-from-windows#:~:text=You%20should%20always%20validate%20the%20hosts%20fingerprint) to confirm that by going to Azure Portal, VM, run command to check the host fingerprint and cross check. In my case they did not match, which was suspicious. But I went through with it anyway, I wasn't able to find anything else to do with it. Maybe later I should try changing the ssh key or something, if that's possible.

#### VS Code remote SSH

- [Guide](https://code.visualstudio.com/docs/remote/ssh-tutorial). I used the "config file" route.

- [This](https://stackoverflow.com/a/69626365) is how to connect using the ssh key, it wasn't immediately obvious to me. Oh and no need for double backslash as mentioned in the answer, regular backslash works too.

- This was an issue because after launching, the connection would hang and show reconnecting and I wouldn't even be able to separately ssh from a terminal even. The issue was because VS Code was using up the entire 1GB RAM.

- Seems like the issue is caused by the [python extensions](https://stackoverflow.com/a/72991121) which is a bummer because those are the ones I needed only. Maybe can try using without them we'll see. Besides, you're supposed to not be dependent on things like autocomplete and linting etc.

- [This article](https://medium.com/good-robot/use-visual-studio-code-remote-ssh-sftp-without-crashing-your-server-a1dc2ef0936d) shows that there are some built-in extensions which use a lot of resources and could be unnecessary, like the typescript support. This info could be useful in the future.

- When the VS Code server starts to hang and you're not able to access even normal ssh, try killing the VS Code server instance using [this command](https://stackoverflow.com/a/57494961).

- Now decided to fully shift development to this VS Code remote ssh workspace.