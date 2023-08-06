import click
import hashlib


@click.group()
def cli():
    pass


def raw_md5(text):
    h = hashlib.md5()
    h.update(text)
    return h.hexdigest()


@click.command()
@click.option("--text")
def md5(text):
    if not text:
        click.echo("`text` is required")
        return
    md5_value = raw_md5(text.encode("utf-8"))
    # print("md5_value:{}".format(md5_value.decode("utf-8")))
    click.echo("md5:")
    click.echo(md5_value)

    pass

cli.add_command(md5)


if __name__ == "__main__":
    cli()
