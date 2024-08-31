import textwrap
import webbrowser

from colorama import Fore, Style, init

"""
==========================================
Dork Me 
Created on: Aug 29, 2023
Author: Isa Ebrahim -- 0xrar.net
==========================================
"""

init(autoreset=True)
b = Fore.BLUE
g = Fore.GREEN
y = Fore.YELLOW
r = Fore.RED


def banner():
    bnr = """ 
    {}  __   __   __            __   ___ 
    {} |  \ /  \ |__) |__/     |\/| |__  
    {} |__/ \__/ |  \ |  \     |  | |___ 
    {} By Isa Ebrahim -- 0xrar.net
    """.format(
        b, g, r, y
    )
    print(textwrap.dedent(bnr))


def help():
    global help_output
    global options_output

    help_output = """
    Command         Description
    -------         -----------
    help            see the help command
    q               exit the script
    """

    options_output = """
    Options
    --------------------------------
    [1]> Directory Listing
    [2]> Exposed Configuration files
    [3]> Exposed Database files
    [4]> Exposed log files
    [5]> Backup and old files
    [6]> Install / Setup files
    [7]> Other Files (pdf,xlsx,etc)
    [8]> Open Redirects
    """


help()


def main():
    target = input("Pick a Target: ")

    print(textwrap.dedent(options_output))
    print("to see the list of options & commands use the command: help")

    dorks = {
        "dlisting": f"site:{target}+intitle:index.of",
        "conf_files": f"site:{target}+filetype:xml+|+filetype:conf+|+filetype:cnf+|+filetype:reg+|+filetype:inf+|+filetype:rdp+|+filetype:cfg+|+filetype:txt+|+filetype:ora+|+filetype:ini",
        "db_files": f"site:{target}+filetype:sql+|+filetype:dbf+|+filetype:mdb",
        "log_files": f"site:{target}+filetype:log+|filetype:txt",
        "backup_files": f"site:{target}+filetype:bkf+|+filetype:bkp+|+filetype:bak+|+filetype:old+|+filetype:backup",
        "setup_files": f"site:{target}+inurl:readme+|+inurl:license+|+inurl:install+|+inurl:setup+|+inurl:config",
        "other_files": f"site:{target}+filetype:pdf+|+filetype:xlsx+|+filetype:docx",
        "oredir": f"site:{target}+inurl:redir+|+inurl:url+|+inurl:redirect+|+inurl:return+|+inurl:src=http+|+inurl:r=http"
    }

    url = "https://google.com/search?q="

    while True:
        op_input = input("Pick an option: ")

        match op_input:
            case "help":
                print(textwrap.dedent(help_output))
                print(textwrap.dedent(options_output))

            case "q":
                print("Quitting...")
                exit(1)

            case "1":
                webbrowser.open_new_tab(url + dorks["dlisting"])
                print(f'Dork used: {dorks["dlisting"]}')
            case "2":
                webbrowser.open_new_tab(url + dorks["conf_files"])
                print(f'Dork used: {dorks["conf_files"]}')
            case "3":
                webbrowser.open_new_tab(url + dorks["db_files"])
                print(f'Dork used: {dorks["db_files"]}')
            case "4":
                webbrowser.open_new_tab(url + dorks["log_files"])
                print(f'Dork used: {dorks["log_files"]}')
            case "5":
                webbrowser.open_new_tab(url + dorks["backup_files"])
                print(f'Dork used: {dorks["backup_files"]}')
            case "6":
                webbrowser.open_new_tab(url + dorks["setup_files"])
                print(f'Dork used: {dorks["setup_files"]}')
            case "7":
                webbrowser.open_new_tab(url + dorks["other_files"])
                print(f'Dork used: {dorks["other_files"]}')
            case "8":
                webbrowser.open_new_tab(url + dorks["oredir"])
                print(f'Dork used: {dorks["oredir"]}')
            case _:
                print('You seem lost? use the command: help')


if __name__ == "__main__":
    banner()
    main()
