from .autoclick import *
import click
import sys
from os import system

developer = {"name": "정지효 (Jung Ji-Hyo)", "email": "cord0318@gmail.com", "age": "13"}

def check_version():
    version = "0.0.5"
    click.echo("autoclick " + version)

cmd_list = ["set_autoclick_key (키 바꾸기)", "developer (개발자)", "friend (도와준 친구)"]

def print_menu():
    system("cls")
    for i in range(len(cmd_list)):
        click.echo(f"[{i}] " + cmd_list[i])

def cmd():
    print_menu()
    cmd = int(input("> "))
    if cmd == 0:
        try:
            system("cls")
            click.echo("바꾸실 키를 적어주세요. ex) <alt>+x <alt>+v")
            cmd = input("> ").split()
            auto_click = AutoClick().set_autoclick_key(cmd[0], cmd[1])
            click.echo("성공적으로 키를 바꾸었습니다!")
            exit()

        except Exception as e:
            click.echo("알수 없는 오류가 나타났습니다.\n오류 코드 : " + e)
            exit()
    elif cmd == 1:
        system("cls")
        for dev in developer:
            click.echo(f"{dev} : {developer[dev]}")
        click.echo("\n")
    elif cmd == 2:
        system("cls")
        click.echo("이 개발을 도와준 '위정우'에게 감사움을 표합니다.\n")

@click.option('--delay', "--start", type=click.FLOAT, default=0.04, help='Start AutoClick.')
@click.option("-v", '--version', is_flag=True, help="Show version of this Program.")
@click.option("--command", "--cmd", is_flag=True, help="Open the autoclick cmd.")
@click.command()
def main(delay, version, command):
    if version:
        check_version()
        sys.exit()
    if command:
        cmd()
        sys.exit()

    if delay:
        click.echo("Your delay : " + str(delay))
        click.echo("start autoclick . . .")
        auto_click = AutoClick(delay=delay)
        auto_click.run_autoclick()

if __name__ == '__main__':
    main()