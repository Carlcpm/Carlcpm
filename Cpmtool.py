#!/usr/bin/python

import random
import urllib.parse
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

# Placeholder import for backend logic
from Carlcpm import Carlcpm

console = Console()

# Simulated login
def login():
    console.print("[bold cyan]LOGIN[/bold cyan]")
    email = Prompt.ask("[?] Enter Gmail")
    password = Prompt.ask("[?] Enter Password", password=True)
    console.print("[bold green]Logged in as:[/bold green]", email)
    time.sleep(1)

# Backend simulation functions (replace with real API logic later)
def set_player_money(amount):
    return True

def set_player_coins(amount):
    return True

def set_player_name(new_name):
    return True

def delete_account():
    return True

def clone_account():
    return True

# Banner function
def show_banner():
    console.print("""
[bold magenta]██████╗  ██████╗ ███╗   ███╗
██╔══██╗██╔═══██╗████╗ ████║
██████╔╝██║   ██║██╔████╔██║
██╔═══╝ ██║   ██║██║╚██╔╝██║
██║     ╚██████╔╝██║ ╚═╝ ██║
╚═╝      ╚═════╝ ╚═╝     ╚═╝[/bold magenta]
[bold yellow]      CARL★CPM2★TOOL[/bold yellow]
""")

# Menu function
def show_menu():
    console.print("""
[bold cyan][ MENU ][/bold cyan]
[1] Increase Money
[2] Increase Coins
[3] Change Name
[4] Delete Account
[5] Clone Account
[6] Exit
""")

# Run
login()

while True:
    show_banner()
    show_menu()
    try:
        service = IntPrompt.ask("[?] Choose a service")

        if service == 1:
            console.print("[bold yellow][?] Insert how much money do you want[/bold yellow]")
            amount = IntPrompt.ask("[?] Amount")
            console.print("[%] Saving your data: ", end=None)
            time.sleep(1)
            if 0 < amount <= 500_000_000:
                if set_player_money(amount):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                else:
                    console.print("[bold red]TRY AGAIN[/bold red]")
            else:
                console.print("[bold red]Invalid amount![/bold red]")

        elif service == 2:
            amount = IntPrompt.ask("[?] Insert how many coins")
            console.print("[%] Saving your data: ", end=None)
            time.sleep(1)
            if 0 < amount <= 100_000_000:
                if set_player_coins(amount):
                    console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
                else:
                    console.print("[bold red]TRY AGAIN[/bold red]")
            else:
                console.print("[bold red]Invalid coins amount![/bold red]")

        elif service == 3:
            name = Prompt.ask("[?] Enter new name")
            console.print("[%] Changing name: ", end=None)
            time.sleep(1)
            if set_player_name(name):
                console.print("[bold green]SUCCESSFUL (✔)[/bold green]")
            else:
                console.print("[bold red]TRY AGAIN[/bold red]")

        elif service == 4:
            console.print("[bold yellow]Deleting your account...[/bold yellow]")
            time.sleep(1)
            if delete_account():
                console.print("[bold green]ACCOUNT DELETED (✔)[/bold green]")
            else:
                console.print("[bold red]FAILED TO DELETE[/bold red]")

        elif service == 5:
            console.print("[bold yellow]Cloning account...[/bold yellow]")
            time.sleep(1)
            if clone_account():
                console.print("[bold green]CLONED SUCCESSFULLY (✔)[/bold green]")
            else:
                console.print("[bold red]FAILED TO CLONE[/bold red]")

        elif service == 6:
            console.print("[bold blue]Exiting tool...[/bold blue]")
            break

        else:
            console.print("[bold red]Invalid selection. Try again.[/bold red]")
            continue

    except KeyboardInterrupt:
        console.print("\n[bold red]Process interrupted![/bold red]")
        break
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        continue
    else:
        continue
    break

