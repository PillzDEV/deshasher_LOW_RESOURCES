#DESHASHER CREATED By -> https://github.com/PillzDEV

import hashlib
import os
import time
from colorama import Fore, init

os.system('cls' if os.name == 'nt' else 'clear')
init()

def main():
    hash_input = input(f"{Fore.CYAN}Hash:{Fore.RESET} ")
    
    if len(hash_input) == 0:
        print(f"{Fore.RED}Enter a hash!!{Fore.RESET}")
        main()
    else:
        hash_input = hash_input.strip()

    salt_input = input(f"{Fore.CYAN}Salt:{Fore.RESET} ")
    
    if len(salt_input) == 0:
        salt = None
    else:
        salt = salt_input.strip()
        
    active_dict = input(f"{Fore.CYAN}Dict path (You can drop here your dict):{Fore.RESET} ")
    if os.path.exists(active_dict):
        pass
    else:
        print(f"{Fore.RED}Invalid path: The specified path does not exist.{Fore.RESET}")
        print("")
        main()

    hash_type = detect_hash_type(hash_input)

    time_start = time.time()
    coincidence = bruteforce_hash(hash_type, hash_input, salt, active_dict)
    time_elapsed = round((time.time() - time_start), 2)

    if coincidence:
        with open('passwords.txt', 'a+') as f:
            f.write(f"\nHash: {hash_input} Salt: {salt} -> {coincidence}")
        print(f"{Fore.GREEN}Password found:{Fore.RESET} {coincidence} {Fore.RED}| {Fore.YELLOW}In {Fore.WHITE}{time_elapsed}s{Fore.RED} | {Fore.RESET} The password has been saved in passwords.txt")
        input(f"{Fore.CYAN}Press {Fore.RED}[ENTER]{Fore.CYAN} to restart the program{Fore.RESET}")
        main()

    else:
        print(f"{Fore.RED}Password not found :({Fore.RESET}")
        input(f"{Fore.CYAN}Press {Fore.RED}[ENTER]{Fore.CYAN} to restart the program{Fore.RESET}")
        main()

def detect_hash_type(hash_input: str) -> callable:
    match len(hash_input):
        case 128:
            return hashlib.sha512
        case 64:
            return hashlib.sha256
        case 40:
            return hashlib.sha1
        case 32:
            return hashlib.md5
        case _:
            print(f"{Fore.RED}INVALID Hash!!{Fore.RESET}")
            return main()

def bruteforce_hash(hash_type: callable, hash_input: str, salt: None, active_dict:str) -> str:
    if salt:
        with open(file=active_dict, mode="r", encoding="latin-1") as dict_file:
            for line in dict_file:
                line = line.strip()
                if (
                    hash_type(line.encode() + salt.encode()).hexdigest() == hash_input
                    or hash_type(salt.encode() + line.encode()).hexdigest() == hash_input
                    or hash_type(hash_type(line.encode()).hexdigest().encode() + salt.encode()).hexdigest() == hash_input
                ):
                    return line
    else:
        with open(file=active_dict, mode="r", encoding="latin-1") as dict_file:
            for line in dict_file:
                line = line.strip()
                if hash_type(line.encode()).hexdigest() == hash_input:
                    return line

    return None


if __name__ == '__main__':
    main()
