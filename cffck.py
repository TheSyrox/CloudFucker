import subprocess

def run_msfconsole_commands(commands):
    try:
        msf_process = subprocess.Popen(['msfconsole'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for command in commands:
            msf_process.stdin.write(command + '\n')
        msf_process.stdin.close()
        output, errors = msf_process.communicate(timeout=15)
        return output, errors
    except Exception as e:
        return None, str(e)

def main():
    hostname = input("Lütfen hostname'i girin: ")
    
    commands = [
        "search Cloudflare http proxy",
        "use 0",
        f"set hostname {hostname}",
        "run"
    ]
    
    output, errors = run_msfconsole_commands(commands)
    
    if output:
        print("Metasploit çıktısı:")
        print(output)
    if errors:
        print("Hata mesajları:")
        print(errors)

if __name__ == "__main__":
    main()
