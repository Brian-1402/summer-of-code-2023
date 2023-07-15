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
